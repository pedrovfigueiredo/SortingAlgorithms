# Análise e Projeto de Algoritmos 2017.1
# Pedro Henrique Villar de Figueirêdo

# Selection sort

def selectionSort(list):
    for i in range(0,len(list), 1):
        minIndex = -1

        for j in range(i, len(list), 1):
            if list[minIndex] > list[j]:
                minIndex = j

        temp = list[i]
        list[i] = list[minIndex]
        list[minIndex] = temp
    return list