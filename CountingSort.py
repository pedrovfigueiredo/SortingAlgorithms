# Análise e Projeto de Algoritmos 2017.1
# Pedro Henrique Villar de Figueirêdo

# Counting sort

def countingSort(a):

    # Shifting numbers to use minimize "zeros to left" and treat negative numbers' case.
    shift = min(a) - 1
    a = [x-shift for x in a]

    # Establishing constants related to A
    lengthA = len(a)
    maxA = max(a)

    c = [0] * maxA

    # Indexing from 1
    a.insert(0,None)
    b = a.copy()
    c.insert(0,None)

    # Sorting operations
    for j in range(1, lengthA + 1):
        c[a[j]] += 1
    for i in range(2, maxA + 1):
        c[i] += c[i - 1]
    for j in range(lengthA, 0, -1):
        b[c[a[j]]] = a[j]
        c[a[j]] -= 1

    # Indexing from 0
    b.pop(0)

    # Recovering original sequence
    b = [x+shift for x in b]

    return b