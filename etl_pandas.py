import pandas as pd 

#pandas substitui o script abaixo:

# with open(PATH_DO_TXT, 'r', encoding="utf-8") as file:
#        _reader = reader(file, delimiter=';')
#        for row in _reader:
#           nome_da_station, temperatura = str(row[0]), float(row[1])
#           temperatura_por_station[nome_da_station].append(temperatura)


df = pd.read_csv("data/measurements.txt",
                sep=";",
                header = None,
                names=["station","measure"]
                )

df_agg = df.groupby("station")
df_kpi = df_agg['measure'].agg({
    "min" : "min",
    "max" : "max",
    "mean" : "mean"
    })

df_sort = df.kpi.sort_values("station")
