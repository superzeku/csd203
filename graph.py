from arraystack import *
from arrqueue import *
from heap import *
from priorityqueue import PQueue

def dfs(graphM, v):
    n = len(graphM)
    stack = ArrayStack()
    visited = [False for _ in range(n)]
    stack.push(v)
    visited[v] = True
    while not stack.isEmpty():
        p = stack.pop()
        print(p.data,end=" ")
        for i in range(n-1,-1,-1):
            if graphM[p.data][i] != 0 and visited[i] == False:
                stack.push(i)
                visited[i] = True
    for i in range(n):
        if not visited[i]:
            stack.push(i)
            visited[i] = True
            while not stack.isEmpty():
                p = stack.pop()
                print(p.data,end=" ")
                for i in range(n-1,-1,-1):
                    if graphM[p.data][i] != 0 and visited[i] == False:
                        stack.push(i)
                        visited[i] = True
def bfs(graphM, v):
    n = len(graphM)
    queue = ArrQueue()
    visited = [False]*n
    queue.enqueue(v)
    visited[v] = True
    while not queue.isEmpty():
        p = queue.dequeue()
        print(p.data,end = " ")
        for i in range(n):
            if graphM[p.data][i] != 0 and visited[i] == False:
                queue.enqueue(i)
                visited[i] = True

def dijkstra(graphM,s):
    n = len(graphM)
    shortestDist = [float("inf")]*n
    prevNode = [None]*n
    pNode = [None]*n
    shortestDist[s] = 0
    heap = MinHeap()
    heap.insert([0,s])
    while not heap.isEmpty():
        dist, node = heap.extract_min().data
        if dist > shortestDist[node]: continue
        for i in range(n):
            if graphM[node][i] > 0:
                newDist = shortestDist[node] + graphM[node][i]
                if newDist < shortestDist[i]:
                    shortestDist[i] = newDist
                    prevNode[i] = node
                    heap.insert([newDist,i])
    vertices = [i for i in range(n)]
    # print(vertices)
    # print(shortestDist)
    # print(prevNode)
    return vertices, shortestDist, prevNode
def buildShortestPath(graphM,s,e):
    vertices, shortestDist, prevNode = dijkstra(graphM,s)
    path = []
    current = e
    while current!=s:
        path.append(current)
        current = prevNode[current]
    path.append(current)
    print(path[::-1])

def prim(graphM, s):
    n = len(graphM)
    visited = []
    mst = []
    pq = PQueue(reverse=True)
    visited.append(s)
    for i in range(n):
        if graphM[s][i] != 0: pq.enqueue([graphM[s][i],s,i])
    while not pq.isEmpty() and len(visited) < n:
        w, b, e = pq.dequeue().data
        if e not in visited:
            visited.append(e)
            mst.append([b,e])
            for i in range(n):
                if graphM[e][i] != 0 and i not in visited:
                    pq.enqueue([graphM[e][i], e, i])
    return mst

def kruskal(graphM):
    n = len(graphM)
    pq = PQueue(reverse=True)
    for i in range(n):
        for j in range(i,n):
            if graphM[i][j] != 0:
                pq.enqueue([graphM[i][j],i,j])
    parent = [i for i in range(n)]
    def find(v):
        if v == parent[v]: return v
        parent[v] = find(parent[v])
        return parent[v]
    def is_cycle(a,b):
        a = find(a)
        b = find(b)
        if a == b: return True
        parent[b] = a
        return False
    mst = []
    while not pq.isEmpty() and len(mst) < n-1:
        w,v,e = pq.dequeue().data
        if not is_cycle(v,e):
            mst.append([v,e])
    return mst


graphM=[[0,2,0,8,0,0],
        [2,0,0,5,6,0],
        [0,0,0,0,9,3],
        [8,5,0,0,3,2],
        [0,6,9,3,0,1],
        [0,0,3,2,1,0]]

graphM2 = [[0,2,3,3,0,0],
           [2,0,4,0,3,0],
           [3,4,0,0,1,6],
           [3,0,0,0,0,7],
           [0,3,1,0,0,8],
           [0,0,6,7,8,0]]

if __name__ == "__main__":
    mst = kruskal(graphM2)
    print(mst)