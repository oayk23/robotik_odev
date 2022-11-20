def selectionsort(A):
    for i in range(len(A)):
     
    
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
                    
        A[i], A[min_idx] = A[min_idx], A[i]
def bubblesort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
def insertionSort(arr):
 
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2

        L = arr[:mid]
 
        R = arr[mid:]
 
        mergeSort(L)
 
        mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def partition(array, low, high):
  
    pivot = array[high]

    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
  
            (array[i], array[j]) = (array[j], array[i])
  
    (array[i + 1], array[high]) = (array[high], array[i + 1])
  
    return i + 1
  
  
  
def quick_sort(array, low, high):
    if low < high:
  
        pi = partition(array, low, high)
  
        quick_sort(array, low, pi - 1)
  
        quick_sort(array, pi + 1, high)
  
a = [1,453,645,7,86,56,924,45,89,23,4]
bubblesort(A=a)
print(a)