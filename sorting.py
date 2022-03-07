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
def heapSort(list):
    n = len(list) 
    MaxHeap(list,n)
    for i in range(n-1, 0, -1):
        list[i], list[0] = list[0], list[i]   
        heapify(list, i,0)

def MaxHeap(list,n):
    for i in range(mt.floor(n/2), -1, -1):
        heapify(list, n,i)        

def heapify(list, n,i):
    largest = i
    left = 2 * i +1
    right = 2 * i + 2
  
    if left < n and list[i] < list[left]:
        largest = left
    else:
        largest = i
  
    if right < n and list[largest] < list[right]:
        largest = right
  
    if largest != i:
        list[i],list[largest] = list[largest],list[i]
        heapify(list,n,largest)

  

arr = [ 5, 4,8,6,20,50,12]
heapSort(arr)
print (arr)
#------------------------------DFS-------------------------------------------------

#------------------------------BFS-------------------------------------------------
#prepare data
list_of_map={0:[1,2,3], 1:[0,2,4], 2:[0,1,5], 3:[0], 4:[1], 5:[2]}
queue = Queue()
bfs_output = []
visited = {}
parents = {}
level = {}

for point in list_of_map.keys():
    visited[point]= False
    parents[point] = None
    level[point] = -1

#start
s = 2
visited[s] = True
level[s] = 0
queue.put(s)

#algorithm
while not queue.empty():
    u = queue.get()
    bfs_output.append(u)
    for v in list_of_map[u]:
        if not visited[v]:
            visited[v] = True
            parents[v] = u
            level[v] = level[u]+1
            queue.put(v)
              
print(bfs_output)




