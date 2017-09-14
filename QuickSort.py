# Análise e Projeto de Algoritmos 2017.1
# Pedro Henrique Villar de Figueirêdo

# Quick sort

def Partition(S):
    x = S[0]
    a = 1
    b = len(S) - 1
    while(a < b):
        while(S[a] <= x and a < b):
            a += 1
        while (S[b] > x):
            b -= 1
        if a < b:
            (S[a], S[b]) = (S[b], S[a])

    (S[0], S[b]) = (S[b], S[0])
    return b

def quickSort(S):
    if (len(S) > 1):
        q = Partition(S)
        S[:q] = quickSort(S[:q])
        S[q+1:] = quickSort(S[q + 1:])
    return S