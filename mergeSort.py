# Análise e Projeto de Algoritmos 2017.1
# Pedro Henrique Villar de Figueirêdo

# Merge sort

def merge(S):
    i = 0
    j = int(len(S) / 2)
    W = []

    while i < int(len(S) / 2) and j < int(len(S)):
        if S[i] <= S[j]:
            W.append(S[i])
            i += 1
        else:
            W.append(S[j])
            j += 1

    while i < int(len(S) / 2):
        W.append(S[i])
        i += 1

    while j < int(len(S)):
        W.append(S[j])
        j += 1

    return W


def mergeSort(S):
    if len(S) > 1:
        #print("S = {}".format(S))
        mid = int(len(S) / 2)
        S1 = mergeSort(S[:mid])
        S2 = mergeSort(S[mid:])
        #print("S1: {} S2: {}".format(S1, S2))
        S = merge(S1 + S2)
        #print("S = {}".format(S))

    return S