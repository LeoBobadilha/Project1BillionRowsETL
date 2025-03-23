from csv import reader 
from collections import defaultdict
import time 
from pathlib import Path

PATH_DO_TXT = "data\measurements.txt"

def processar_temperaturas(PATH_DO_TXT: Path):
    print("Iniciando o processamento do arquivo.")

    start_time = time.time() # Tempo de inicio

    temperatura_por_station = defaultdict(list) ## exemplo de defaultdict {hamburg:{15,17,35,41}} # eh importante pois dessa forma nao teria
                                                ## erros referente a inserir o mesmo valor dentro do dicionario

    with open(PATH_DO_TXT, 'r', encoding="utf-8") as file:
        _reader = reader(file, delimiter=';')
        for row in _reader:
            nome_da_station, temperatura = str(row[0]), float(row[1])
            temperatura_por_station[nome_da_station].append(temperatura)

    print("Dados carregados. Calculando estatisticas...")

    # Dicionario para armazenar os resultados calculados
    results = {}


    for station, temperatures in temperatura_por_station.items():
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)
        results[station] = (min_temp, mean_temp, max_temp)

    print("Estatistica calculada. Ordenando...")
    # Ordenando os resutlados pelo nome da estacao
    sorted_results = dict(sorted(results.items()))

    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}" for station, (min_temp, mean_temp, max_temp)in sorted_results.items()}

    end_time = time.time() #tempo de termino
    print(f"processamento concluido em {end_time - start_time:.2f} segundos.")

    return formatted_results

#Substitua "data/measurements10m.txt" pelo caminho correto do ser arquivo
if __name__ == "__main__": ## pra rodar o script somente se eu chamalo
    PATH_DO_TXT: Path = Path ("data/measurements.txt")
    #100m > 5 minutos
    resultados = processar_temperaturas(PATH_DO_TXT)
