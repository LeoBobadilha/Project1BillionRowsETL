import pandas as pd
import numpy as np

#Function to create a DataFrame example of 100k rows and 20 cities
def criar_medidas(num_linhas=100000, num_cidades=20, semente=None):
    estado = np.random.RandomState(semente)
    cidades = [f"Cidade_{i}"for i in range(num_cidades)]
    dados = {
        "estacao": estado.choice(cidades, size=num_linhas),
        "medida": estado.uniform(-20,50, size=num_linhas).round(4)
    }
    df = pd.DataFrame(dados)
    return df

#Create an dataframe of example
df = criar_medidas(semente=0)

#Display type of data and usage of memory before conversion
print("Tipos de dados e uso de memoria antes da conversa")
print(df.dtypes)
print(df.memory_usage(deep=True))

#Save the initial memory usage
uso_memoria_inicial = df.memory_usage(deep=True).sum()

detalhes_memoria_antes = df.memory_usage(deep=True)

#transform type of data for eficient type
df["estacao"] = df ["estacao"].astype("category")
df["medida"] = pd.to_numeric(df["medida"], downcast="float")

#Display type of data and usage of memory after conversion
print("Tipos de dados e uso de memoria depois da conversao")
print(df.dtypes)
print(df.memory_usage(deep=True))

#Save the final memory of use
uso_memoria_final = df.memory_usage(deep=True).sum()

#Calculate the reduction of memory
reducao_total = 1 - (uso_memoria_final / uso_memoria_inicial)
reducao_estacao = 1 - (df.memory_usage(deep=True)["estacao"] / detalhes_memoria_antes["estacao"])
reducao_medida = 1 - (df.memory_usage(deep=True)["medida"] / detalhes_memoria_antes["medida"])

print(f"\nReducao total no uso de memoria: {reducao_total:.2f}")
print(f"\nReducao no uso de memoria para a coluna 'estacao': {reducao_estacao:.2f}")
print(f"\nReducao no uso de memoria para a coluna 'estacao': {reducao_medida:.2f}")

#Detail of usage of memory before and after the conversion
print("\nDetalhes do uso de memoria antes e depois da conversao")
print(detalhes_memoria_antes)

print("\nDetalhes do uso de memoria apos a conversao:")
print(df.memory_usage(deep=True))
