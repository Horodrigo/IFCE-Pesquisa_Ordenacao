
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

def insertionSort(elementList): 
  
    swappedNumber = 0
    for i in range(1, len(elementList)): 
  
        key = elementList[i] 
        j = i-1
        while j >= 0 and key < elementList[j] :
            swappedNumber = swappedNumber + 1    
            elementList[j + 1] = elementList[j] 
            j -= 1
        elementList[j + 1] = key 
    
    return swappedNumber


def shuffle_random(n):
    result = list(range(n))
    random.shuffle(result)
    return result


options = [1000, 10000, 30000, 60000]
results_random = []
results_reverse = []
for option in options:
    tempo =   timeit.timeit("insertionSort({})".format(shuffle_random(option)), setup="from __main__ import insertionSort",number=1)
    results_random.append(tempo)
    tempo =   timeit.timeit("insertionSort({})".format(list(range(option))[::-1]), setup="from __main__ import insertionSort",number=1)
    results_reverse.append(tempo)

plotaImagem(options, results_random, name ='aleatorioInsertion.png')
