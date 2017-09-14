# Análise e Projeto de Algoritmos 2017.1
# Pedro Henrique Villar de Figueirêdo

# Heap sort

esquerdo = lambda x: 2 * x
direito = lambda x: 2 * x + 1
tamanho_heap = lambda x: len(x) - 1


def maxHeapfy(S, i):
    l = esquerdo(i)
    r = direito(i)

    if l <= tamanho_heap(S) and S[l] > S[i]:
        maior = l
    else:
        maior = i

    if r <= tamanho_heap(S) and S[r] > S[maior]:
        maior = r

    if maior != i:
        (S[i], S[maior]) = (S[maior], S[i])
        maxHeapfy(S, maior)

    return S


def buildMaxHeap(S):
    for i in range(int(tamanho_heap(S) / 2), 0, -1):
        maxHeapfy(S, i)
    return S


def heapSort(S:list):
    # Transforming into heap
    S.insert(0,None)
    buildMaxHeap(S)
    for i in range(tamanho_heap(S), 1, -1):
        (S[1], S[i]) = (S[i], S[1])
        S[:i] = maxHeapfy(S[:i], 1)
    # Transforming back to list
    S.pop(0)

    return S