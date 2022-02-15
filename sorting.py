#-----------Quick------------------------
def quick_sort(list):
    if len(list) <= 1:
        return list
    
    less_pivot = []
    greater_pivot = []
    pivot = list[0]
    for value in list[1:]:
        if value <= pivot:
            less_pivot.append(value)
        else:
            greater_pivot.append(value)
    return quick_sort(less_pivot) + [pivot] + quick_sort(greater_pivot)

#--------------Merge---------------------------
def merge_sort(list):
    
    if len(list) <= 1:
        return list
    

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(list):
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    return left, right

def merge(left, right):
    l = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1                        
        else:
            l.append(right[j])
            j += 1
            
            
    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1
    return l

#--------------------Heap----------------------
def heap_sort(list):
    buildMaxHeap(list)
    n = len(list)
    while n >= 0:
        list[0], list[n-1] = list[n-1], list[0]
        n -= 1
        heapify(list,0)

def buildMaxHeap(list):
    n = len(list)
    n_half = mt.floor(n/2)
    while n_half >= 0:
        heapify(list, n_half)
        n_half -= 1
        
def heapify(list, i):
    left = 2*i
    right = 2*i+1
    n = len(list)
    
    if left <= n and list[left] > list[i]:
        max = left
    else:
        max = i
    

    print(list)
    if right-1 <= n and list[right-1] > list[max]:
        max = right
    
    if max != i:
        list[0], list[max] = list[max], list[0]
        heapify(list, max)
