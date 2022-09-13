def merge(arr1, arr2):
    sorted = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted.append(arr1[i])
            i += 1
        else:
            sorted.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted.append(arr2[j])
        j += 1
    return sorted

def merge_sort(array):
    if len(array) == 1:
        return array
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    print(merge(left, right))
    return merge(left, right)

def quick_sort(array):
    arr = copy(array)
    if len(arr) <= 1:
        return arr
    pivot = arr.pop()
    left = []
    right = []
    for e in arr:
        if e < pivot:
            left.append(e)
        else:
            right.append(e)
    return quick_sort(left) + [pivot] + quick_sort(right)

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
print("Merge Sort:     ", merge_sort(array))
print("Quick Sort:     ", quick_sort(array))