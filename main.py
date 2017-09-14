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


#PrintSorts.displaySortStatistics(radixSort,"instances/num.100000.4.in", "Radix Sort")
#PrintSorts.displaySortStatistics(quickSort,"instances/num.100000.1.in", "Quick Sort")

PrintSorts.compareSorts([["Counting Sort", countingSort], ["Radix Sort", radixSort]], "instances/counting.txt")
#PrintSorts.compareSorts([["Counting Sort", countingSort], ["Radix Sort", radixSort]], "instances/num.1000.1.in")
#PrintSorts.compareSorts([["Counting Sort", countingSort], ["Radix Sort", radixSort]], "instances/num.1000.2.in")
#PrintSorts.compareSorts([["Counting Sort", countingSort], ["Radix Sort", radixSort]], "instances/num.1000.3.in")
#PrintSorts.compareSorts([["Counting Sort", countingSort], ["Radix Sort", radixSort]], "instances/num.1000.4.in")
#PrintSorts.compareSorts([["Counting Sort", countingSort], ["Radix Sort", radixSort]], "instances/num.10000.1.in")
#PrintSorts.compareSorts([["Counting Sort", countingSort], ["Radix Sort", radixSort]], "instances/num.10000.2.in")
#PrintSorts.compareSorts([["Counting Sort", countingSort], ["Radix Sort", radixSort]], "instances/num.10000.3.in")
#PrintSorts.compareSorts([["Counting Sort", countingSort], ["Radix Sort", radixSort]], "instances/num.10000.4.in")
#PrintSorts.compareSorts([["Counting Sort", countingSort], ["Radix Sort", radixSort]], "instances/num.100000.1.in")
#PrintSorts.compareSorts([["Counting Sort", countingSort], ["Radix Sort", radixSort]], "instances/num.100000.2.in")
#PrintSorts.compareSorts([["Counting Sort", countingSort], ["Radix Sort", radixSort]], "instances/num.100000.3.in")
#PrintSorts.compareSorts([["Counting Sort", countingSort], ["Radix Sort", radixSort]], "instances/num.100000.4.in")
