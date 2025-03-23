#3 estrategias para trabalhar com pandas, pegar menos colunas, pensar estruturas de dados(melhor datatype possivel), fazer o chunk


import pandas as pd 
from multiprocessing import Pool,cpu_count
from tqdm import tqdm #importa o tqdm para a barra de processo

CONCURRENCY = cpu_count()

total_linhas = 100_000_000 # Number of known of  rows
chunksize = 10_000_000 # Setting the size of the chunk
filename = "data/measurements.txt" # Certifiyng that is the correct size

def process_chunk(chunk):
    #Agreggating the data inside of the chunck to use Pandas
    aggregated = chunk.groupby("station")["measure"].agg(["min","max","mean"]).reset_index()
    return aggregated

def create_df_with_pandas(filename, total_linhas, chunksize=chunksize):
    total_chunks = total_linhas // chunksize + (1 if total_linhas % chunksize else 0)
    results = []

    with pd.read_csv(filename, sep=';', header=None, names=['station', 'measure'], chunksize=chunksize) as reader:
        # Envolvendo o iterador com tqdm para visualizar o progresso
        with Pool(CONCURRENCY) as pool:
            for chunk in tqdm(reader, total=total_chunks, desc="Processando"):
                # Processa cada chunk em paralelo
                result = pool.apply_async(process_chunk, (chunk,))
                results.append(result)

            results = [result.get() for result in results]

    final_df = pd.concat(results, ignore_index=True)

    final_aggregated_df = final_df.groupby('station').agg({
        'min': 'min',
        'max': 'max',
        'mean': 'mean'
    }).reset_index().sort_values('station')

    return final_aggregated_df

if __name__ == "__main__":
    import time

    print("Iniciando o processamento do arquivo.")
    start_time = time.time()
    df = create_df_with_pandas(filename, total_linhas, chunksize)
    took = time.time() - start_time

    print(df.head())
    print(f"Processing took: {took:.2f} sec")

