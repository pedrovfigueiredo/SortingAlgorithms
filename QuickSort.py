# Análise e Projeto de Algoritmos 2017.1
# Pedro Henrique Villar de Figueirêdo

# Quick sort

def Partition(S):
    x = S[0]
    a = 1
    b = len(S) - 1
    while(True):
        while(S[b] > x):
            b -= 1
        while(S[a] < x):
            a += 1
        if a <= b:
            (S[a], S[b]) = (S[b], S[a])
        else:
            (S[0],S[b]) = (S[b], S[0])
            return b

def quickSort(S):
    if (len(S) > 1):
        q = Partition(S)
        S[:q] = quickSort(S[:q])
        S[q+1:] = quickSort(S[q + 1:])
    return S


l = [7,4,1,9,3,2]
print(quickSort(l))