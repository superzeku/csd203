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
        print(arr)
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

arr = [7,3,9,10,2,6,5]
print(arr)
print()
#bubble_sort(arr)
#insertion_sort(arr)
#selection_sort(arr)
quick_sort(arr,0,len(arr)-1)
print(arr)