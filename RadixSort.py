# Análise e Projeto de Algoritmos 2017.1
# Pedro Henrique Villar de Figueirêdo

# Radix sort

def radixSort(a):

    # Shifting numbers to use minimize "zeros to left" and treat negative numbers' case.
    shift = min(a) - 1
    if shift != 0:
        a = [x - shift for x in a]

    # Establishing constants related to A
    lengthA = len(a)
    maxA = max(a)
    maxDigits = len(str(maxA))

    # Transforming to string and filling with zeros when necessary
    a = [str(x).zfill(maxDigits) for x in a]

    # Indexing from 1
    a.insert(0, None)
    b = a.copy()

    for d in range(maxDigits - 1, -1, -1):

        c = [0] * 10

        # Sorting operations
        for j in range(1, lengthA + 1):
            c[int(a[j][d])] += 1
        for i in range(1, len(c)):
            c[i] += c[i - 1]
        for j in range(lengthA, 0, -1):
            b[c[int(a[j][d])]] = a[j]
            c[int(a[j][d])] -= 1

        a = b.copy()

    # Indexing from 0
    b.pop(0)

    b = list(map(int,b))

    # Recovering original sequence
    if shift != 0:
        b = [x + shift for x in b]

    return b