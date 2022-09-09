def copy(arr):
    new = []
    for e in arr:
        new.append(e)
    return new

def get_min(arr):
    minimum = 0
    for i in range(len(arr)):
        if arr[i] < arr[minimum]:
            minimum = i
    return minimum

def selection_sort(array):
    unsorted = copy(array)
    sorted = []
    for i in range(len(array)):
        minimum_ind = get_min(unsorted)
        sorted.append(unsorted[minimum_ind])
        unsorted.pop(minimum_ind)
    return sorted

def bubble_sort(array):
    arr = copy(array) 
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def insertion_sort(array):
    arr = copy(array)
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            temp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr

def counting_sort(array):
    arr = copy(array)
    minval = arr[get_min(arr)]
    for i in range(len(arr)):
        arr[i] = arr[i] - minval
    max = 0
    for e in arr:
        if e > max:
            max = e
    counts = [0]*(max + 1)
    for e in arr:
        counts[e] += 1
    sorted = []
    for val in range(len(counts)):
        n = counts[val]
        for i in range(n):
            sorted.append(val + minval)
    return sorted

array = [1,9,2,2,3,4,10,11,8,7,5]

print("Selection Sort: ", selection_sort(array))
print("Bubble Sort:    ", bubble_sort(array))
print("Insertion Sort: ", insertion_sort(array))
print("Counting Sort:  ", counting_sort(array))