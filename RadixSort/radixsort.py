# Aluno: Rodrigo Viana Castelo Branco
# Matrícula: 20172015020218
# Disciplina: Pesquisa e Ordenação 2020.1

import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint, shuffle
import timeit

def plot_grafico(x, y, z, file_name, label1, label2, xl = "Tamanho", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label= label1)
    ax.plot(x, z, label= label2)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)

    fig.savefig(file_name)

def geraLista(tam):
    lista = list(range(1, tam+1))
    shuffle(lista)
    return lista

def radixsort(lista):
    base = 1
    maior = max(lista)

    while maior/base > 0:
        indice = len(lista) + 1
        ocorrencias = [0] * indice

        for i in lista:
            ocorrencias[i] += 1

        aux = 0

        for i in range(indice):
            for j in range(ocorrencias[i]):
                lista[aux] = i
                aux += 1
        base *= 10


x = [20000,30000,40000,50000,60000]
y_aleatorio = []
y_reverso = []
tempo_aleatorio = []
tempo_reverso = []


for i in range(len(x)):
    y_aleatorio.append(geraLista(x[i]))
    lista_reversa = list(range(1, x[i]))
    lista_reversa = lista_reversa[::-1]
    y_reverso.append(lista_reversa)

for i in range(len(x)):
    tempo_aleatorio.append(timeit.timeit("radixsort({})".format(y_aleatorio[i], x[i]), setup="from __main__ import radixsort", number=1))
    tempo_reverso.append(timeit.timeit("radixsort({})".format(y_reverso[i], x[i]), setup="from __main__ import radixsort", number=1))

plot_grafico(x, tempo_aleatorio, tempo_reverso, "RadixSort.png", "aleatorioCounting", "reversoCounting")
