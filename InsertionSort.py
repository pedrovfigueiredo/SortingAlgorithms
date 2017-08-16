# Análise e Projeto de Algoritmos 2017.1
# Pedro Henrique Villar de Figueirêdo

# Insertion sort

def insertionSort(list):
    for i in range(1, len(list)):
        aux = list[i]
        j = i - 1
        while j >= 0 and list[j] > aux:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = aux

l = [54,26,93,17,77,31,44,55,20]
insertionSort(l)
print(l)