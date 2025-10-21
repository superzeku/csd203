def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i
        while j>0 and arr[j-1]>key:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        max_idx = i
        for j in range(i):
            if arr[j] > arr[max_idx]: max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

def partition(arr,l,r):
    pivot = arr[r]  
    i = l-1
    for j in range(l,r):
        if arr[j]<=pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r],arr[i+1]
    return i+1
def quick_sort(arr,l,r):
    if l >= r: return
    pi = partition(arr,l,r)
    quick_sort(arr,l,pi-1)
    quick_sort(arr,pi+1,r)

def merge(arr,l,m,r):
    n1 = m-l+1
    n2 = r-m
    l_arr = arr[l:l+n1]
    r_arr = arr[m+1:m+1+n2]
    i = 0; j = 0; k = l
    while i<n1 and j<n2:
        if l_arr[i]<r_arr[j]:
            arr[k] = l_arr[i]
            i+=1
        else:
            arr[k] = r_arr[j]
            j+=1
        k+=1
    while i<n1:
        arr[k]=l_arr[i]
        k+=1; i+=1
    while j<n2:
        arr[k]=r_arr[j]
        k+=1; j+=1

def merge_sort(arr,l,r):
    if l>=r: return 
    m = (l+r)//2
    merge_sort(arr,l,m)
    merge_sort(arr,m+1,r)
    merge(arr,l,m,r)

def heapify_down(arr,n,i):
    l = i*2+1
    r = i*2+2
    largest = i
    if l<n and arr[l]>arr[largest]: largest = l
    if r<n and arr[r]>arr[largest]: largest = r
    if largest!=i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_down(arr,n,largest)
def heap_sort(arr):
    n = len(arr)
    for i in range(len(arr)//2-1,-1,-1): heapify_down(arr,n,i)
    for i in range(len(arr)-1,-1,-1):
        arr[i],arr[0] = arr[0], arr[i]
        heapify_down(arr,i,0)

def bucket_sort(arr):
    n = len(arr)
    n_buckets = 3
    buckets = [[] for _ in range(n_buckets)]
    #distribute array into buckets
    for i in range(n):
        if arr[i] <= 3: buckets[0].append(arr[i])
        elif arr[i] <= 6: buckets[1].append(arr[i])
        else: buckets[2].append(arr[i])
    for i in range(n_buckets): insertion_sort(buckets[i])
    k = 0
    for i in range(n_buckets):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k+=1

def radix_sort(arr):
    if not arr:
        return
    n = len(arr)
    max_val = max(arr)
    n_loop = len(str(max_val)) 
    base = 1
    
    for i in range(n_loop):
        n_list = [[] for _ in range(10)] 
        
        for j in range(n):
            idx = arr[j] // base % 10
            n_list[idx].append(arr[j])
            
        arr_temp = [] 
        for k in range(10):
            arr_temp += n_list[k]
        arr[:] = arr_temp
        base *= 10

arr = [24, 320, 672, 348, 654, 910, 78, 76]
print(arr)
print()
#bubble_sort(arr)
#insertion_sort(arr)
#selection_sort(arr)
#merge_sort(arr,0,len(arr)-1)
#heap_sort(arr)
#bucket_sort(arr)
radix_sort(arr)
print(arr)