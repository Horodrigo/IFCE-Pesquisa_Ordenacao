# Aluno: Rodrigo Viana Castelo Branco
# Matrícula: 20172015020218
# Disciplina: Pesquisa e Ordenação 2020.1

import random
import timeit
import math
import matplotlib as mpl
from itertools import accumulate
mpl.use('Agg')
import matplotlib.pyplot as plt

def desenhaGrafico(x, y, xl="Tamanho", yl="Tempo", name="out"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)


def generateList(size):
    lista = list(range(1, size + 1))
    shuffle(lista)
    return lista


def bucket_sort(list):
    largest = max(list)
    length = len(list)
    size = largest/length

    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(list[i]/size)
        if j != length:
            buckets[j].append(list[i])
        else:
            buckets[length - 1].append(list[i])

    for i in range(length):
        insertion_sort(buckets[i])

    result = []
    for i in range(length):
        result = result + buckets[i]

    return result


def insertion_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while (j >= 0 and temp < list[j]):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = temp


size = [15000,25000,35000,45000,55000]
time = []

for s in size:
    
    lista = generateList(s)
    time.append(timeit.timeit("bucket_sort({})".format(lista),
                              setup="from __main__ import bucket_sort", number=1))
    print(s)

desenhaGrafico(size, time, "Tamanho", "Tempo","bucketSort.png")
