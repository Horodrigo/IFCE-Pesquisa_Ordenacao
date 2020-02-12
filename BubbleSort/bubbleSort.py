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


def bubbleSort(to_sort):
    ponteiro = to_sort.copy()
    length = len(ponteiro)
    for contador, _ in enumerate(ponteiro):
        pivot = 0
        for contador2 in range(1, length-contador):
            if ponteiro[contador2] < ponteiro[pivot]:
                ponteiro[contador2], ponteiro[pivot] = ponteiro[pivot], ponteiro[contador2]
                pivot = contador2
    return ponteiro


def shuffle_random(n):
    result = list(range(n))
    random.shuffle(result)
    return result


options = [1000, 10000, 30000, 60000]
results_random = []
results_reverse = []
for option in options:
    tempo =   timeit.timeit("bubbleSort({})".format(shuffle_random(option)), setup="from __main__ import bubbleSort",number=1)
    results_random.append(tempo)
    tempo =   timeit.timeit("bubbleSort({})".format(list(range(option))[::-1]), setup="from __main__ import bubbleSort",number=1)
    results_reverse.append(tempo)

plotaImagem(options, results_random, name ='aleatorio.png')
plotaImagem(options, results_reverse, name='reverso.png')
