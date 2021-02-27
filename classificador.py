import pandas as pd
import matplotlib.pyplot as plt

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv"
filmes = pd.read_csv(uri)
filmes.columns = ["filmeId", "titulo", "generos"]

print(filmes.head())

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
notas = pd.read_csv(uri)
notas.columns = ["usuarioId", "filmeId", "nota", "momento"]

print(notas.head())

notas.nota.plot(kind='hist')
plt.show()