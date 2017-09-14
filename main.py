# Análise e Projeto de Algoritmos 2017.1
# Pedro Henrique Villar de Figueirêdo

import PrintSorts
from CountingSort import countingSort
from HeapSort import heapSort
from InsertionSort import insertionSort
from MergeSort import mergeSort
from QuickSort import quickSort
from RadixSort import radixSort
from SelectionSort import selectionSort

# Main file to call sorts and compare instances


PrintSorts.displaySortStatistics(countingSort,"instances/num.100000.1.in", "Counting Sort")
PrintSorts.displaySortStatistics(quickSort,"instances/num.100000.1.in", "Quick Sort")

PrintSorts.compareSorts([["Heap Sort", heapSort], ["Radix Sort", radixSort]], "instances/num.1000.1.in")
