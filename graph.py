from arraystack import *
from arrqueue import *
from heap import *

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
    
graphM=[[0,2,0,8,0,0],
        [2,0,0,5,6,0],
        [0,0,0,0,9,3],
        [8,5,0,0,3,2],
        [0,6,9,3,0,1],
        [0,0,3,2,1,0]]
buildShortestPath(graphM,0,5)