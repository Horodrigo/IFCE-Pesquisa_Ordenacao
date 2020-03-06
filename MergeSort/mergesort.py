# Aluno: Rodrigo Viana Castelo Branco
# Matrícula: 20172015020218
# Disciplina: Pesquisa e Ordenação 2020.1

import random
import timeit
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


def plotaImagem(x,y,xl = "Tamanho", yl = "tempo", name='graph.png'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name)


def mergeSort(array):
    if len(array) < 20:
        return sorted(array)
    result = []
    mid = int(len(array) / 2)
    y = mergeSort(array[:mid])
    z = mergeSort(array[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result


def shuffle_random(n):
    result = list(range(n))
    random.shuffle(result)
    return result


options = [1000, 10000, 30000, 60000]
results_random = []
results_reverse = []
for option in options:
    tempo =   timeit.timeit("mergeSort({})".format(shuffle_random(option)), setup="from __main__ import mergeSort",number=1)
    results_random.append(tempo)

plotaImagem(options, results_random, name ='aleatorioMerge.png')
