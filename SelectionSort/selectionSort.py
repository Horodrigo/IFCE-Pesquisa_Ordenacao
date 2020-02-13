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


def selectionSort(listaElementos):
  numeroTroca = 0
  for i in range(len(listaElementos)): 
      
    minIndex = i 
    for j in range(i+1, len(listaElementos)): 
      numeroTroca = numeroTroca + 1
      if listaElementos[minIndex] > listaElementos[j]: 
        minIndex = j
            
    if minIndex != 1:
      listaElementos[i], listaElementos[minIndex] = listaElementos[minIndex], listaElementos[i]
  return numeroTroca


def shuffle_random(n):
    result = list(range(n))
    random.shuffle(result)
    return result


options = [100, 1000, 3000, 6000]
results_random = []
results_reverse = []
for option in options:
    tempo =   timeit.timeit("selectionSort({})".format(shuffle_random(option)), setup="from __main__ import selectionSort",number=1)
    results_random.append(tempo)
    tempo =   timeit.timeit("selectionSort({})".format(list(range(option))[::-1]), setup="from __main__ import selectionSort",number=1)
    results_reverse.append(tempo)

plotaImagem(options, results_random, name ='aleatorio.png')
plotaImagem(options, results_reverse, name='reverso.png')
