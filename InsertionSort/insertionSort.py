
# Aluno: Rodrigo Viana Castelo Branco
# Matrícula: 20172015020218
# Disciplina: Pesquisa e Ordenação 2020.1

import random
import timeit
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


def plotaImagem(x,y,xl = "Entradas", yl = "Saídas", name='graph.png'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name)


def selectionsort(to_sort):
    clone = to_sort.copy()
    length = len(clone)
    for count, _ in enumerate(clone):
        pivot = count
        for count2 in range(count+1, length-1):
            if clone[count2] < clone[pivot]:
                pivot = count2
        if clone[count] > clone[pivot]:
            clone[count], clone[pivot] = clone[pivot], clone[count]
    return clone


def shuffle_random(n):
    result = list(range(n))
    random.shuffle(result)
    return result


options = [1000, 10000, 30000, 60000]
results_random = []
results_reverse = []
for option in options:
    tempo =   timeit.timeit("selectionsort({})".format(shuffle_random(option)), setup="from __main__ import selectionsort",number=1)
    results_random.append(tempo)
    tempo =   timeit.timeit("selectionsort({})".format(list(range(option))[::-1]), setup="from __main__ import selectionsort",number=1)
    results_reverse.append(tempo)

plotaImagem(options, results_random, name ='aleatorio.png')
plotaImagem(options, results_reverse, name='reverso.png')
