import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

notas = pd.Series([2,3,4,5,6])
print(notas)
#lista de valores e indices nao setados anteriormente
notas = pd.Series([2,3,4,5,6],index=["Patrick","Pedro","Wallace","Gabriel","Cosplay"])
print(notas)
print(notas**2)#ver as notas ao quadrado
#usamos index para determinar indices no caso nome para cada nota

# .mean() para media
# .std() para desvio padrao
# .describe() para descrever tudo sobre aqueles dados

print("Media: ",notas.mean())
print("Desvio padrao: ",notas.std())
print(notas.describe())

#Já um DataFrame é 
#uma estrutura bidimensional de dados, como uma planilha.


df = pd.DataFrame({'Aluno' : ["Patrick","Pedro","Wallace","Gabriel","Cosplay"],
                   'Faltas' : [3,4,2,1,4],
                   'Prova' : [2,7,5,10,6],
                   'Seminário': [8.5,7.5,9.0,7.5,8.0]})
print(df)
#printa o data frame
print(df.dtypes)
#mostra os tipos de dados do data frame
print(df.columns)
#mostra as colunas do data frame
print(df.Seminário)
# exemplo de printagem de apenas uma coluna
print(df.describe())
#informaçoes gerais de cada coluna
print(df.sort_values(by="Seminário"))
#ordenar os valores da coluna seminario de forma crescente
print(df.loc[3])
# .loc usado para pegar apenas os dados da pessoa q esta naquele indice
print(df[df["Seminário"]>8])
# usa-se dessa forma para mostrar apenas os valores maiores que 8
#na coluna seminario
print(df[(df["Seminário"] > 8.0) & (df["Prova"] > 3)])
# mesma coisa que o de cima porem agora mostra os alunos com 
# valores acima de 8 no seminario e de 3 na prova

df = pd.read_csv("patient.csv")
# pd.read le algum arquivo csv contendo um dataset,tem que estar no mesmo repositorio
print(df)
# por padrao ele mostra apenas as 5 primeiras linhas
print(df.head(n=10))
# esse padrao pode ser alterado usando .head(n=<numero de linhas>)
print(df.tail())
# por padrao mostra as 5 ultimas linhas do dataframe, mas pode ser alterado da mesma
# forma que o head

print(df["birth_year"].unique())
# lista em uma unica coluna os valores unicos daquela coluna
# do data frame usando df["nome da coluna"].unique()



#vizualizar dados em grafico