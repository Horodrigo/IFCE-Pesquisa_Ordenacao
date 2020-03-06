# Aluno: Rodrigo Viana Castelo Branco
# Matrícula: 20172015020218
# Disciplina: Pesquisa e Ordenação 2020.1

import random
import timeit
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


def plotaImagem(x,y,xl = "Tamanho", yl = "Tempo", name='graph.png'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name)


def shellSort(elementList): 
   
    numberElement = len(elementList) 
    gap =  numberElement//2
    while gap > 0: 
  
        for i in range(gap, numberElement): 
            
            temp = elementList[i]
            j = i 
            while  j >= gap and elementList[j-gap] >temp: 
                
                elementList[j] = elementList[j-gap] 
                j = j - gap
            
            elementList[j] = temp 
        
        gap //= 2


def shuffle_random(n):
    result = list(range(n))
    random.shuffle(result)
    return result


options = [30000,40000,50000,60000,70000]
results_random = []
results_reverse = []
for option in options:
    tempo =   timeit.timeit("shellSort({})".format(shuffle_random(option)), setup="from __main__ import shellSort",number=1)
    results_random.append(tempo)

plotaImagem(options, results_random, name ='aleatorioShell.png')
