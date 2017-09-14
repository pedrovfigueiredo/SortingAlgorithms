# Análise e Projeto de Algoritmos 2017.1
# Pedro Henrique Villar de Figueirêdo

# Method to print any sort, displaying its time and make comparisons

from time import time

def calculateTime(sort, A):

    start = time()
    sort(A)
    end = time()
    elapsed_time = round(end - start, 5)
    return elapsed_time

def displaySortStatistics(sort, file: str, name: str):
    # reading ints from file
    with open(file) as f:
        A = [int(line.rstrip('\n')) for line in f]

    elapsed_time = calculateTime(sort,A)

    print("---------", name, "---------")
    print("Elapsed time:", elapsed_time , "seconds\n")

    return elapsed_time

def compareSorts(sorts: list, file: str):
    # reading ints from file
    with open(file) as f:
        A = [int(line.rstrip('\n')) for line in f]

    # sort[0] = function and sort[1] = name
    times = sorted([[sort[0], calculateTime(sort[1],A)] for sort in sorts], key= lambda x: x[1],reverse=False)

    print("-----------------------------")
    print("Instance:", file)
    for time in times:
        print(time[0],time[1], "seconds")
    print("-----------------------------")





