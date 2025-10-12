import random
import time
# function

def create_array(n):
    random.seed(0)
    for i in range(n): a.append(random.randint(0,100))
    
def median3(a,l,r):
    m = (l+r)//2
    if a[l]>a[m]: a[l],a[m] = a[m],a[l]
    if a[l]>a[r]: a[l],a[r] = a[r],a[l]
    if a[m]>a[r]: a[m],a[r] = a[r],a[m]
    a[m],a[r] = a[r],a[m]
    return a[r]

def partition(a,l,r):
    pivot = a[r]   #median3(a,l,r)
    i = l-1
    for j in range(l,r):
        if a[j]<=pivot:
            i+=1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r],a[i+1]
    return i+1

def quick_sort(a,l,r):
    while l<r:
        if r-l>10:
            pi = partition(a,l,r)
            if r-pi>pi-l:
                quick_sort(a,l,pi-1)
                l = pi+1
            else:
                quick_sort(a,pi+1,r)
                r = pi-1
        else:
            insertion_sort(a,l,r)
            break

def insertion_sort(a,l,r):
    for i in range(l+1,r+1):
        k = a[i]
        j = i-1
        while j>=l and a[j]>k:
            a[j+1]=a[j]
            j-=1
        a[j+1]=k

# main
a = []
create_array(20)
print(a)
quick_sort(a,0,len(a)-1)
print(a)