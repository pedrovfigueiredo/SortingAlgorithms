# Análise e Projeto de Algoritmos 2017.1
# Pedro Henrique Villar de Figueirêdo

# Method to print any sort, displaying its time and make comparisons

from time import time

def displaySortStatistics(sort, file: str, name: str):
    # reading ints from file
    with open(file) as f:
        A = [int(line.rstrip('\n')) for line in f]

    start = time()
    sort(A)
    end = time()

    elapsed_time = round(end - start, 5)
    print("---------", name, "---------")
    print("Elapsed time:", elapsed_time , "seconds\n")

    return elapsed_time

def compareSorts(sorts: list, file: str):
    # reading ints from file
    with open(file) as f:
        A = [int(line.rstrip('\n')) for line in f]

    # sort[0] = function and sort[1] = name
    times = [[sort[0], displaySortStatistics(sort[1],file,sort[0])] for sort in sorts]



