from queue import PriorityQueue

v = 14
graph = [[] for i in range(v)]

def best_first_search(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, actual_Src))
    visited[actual_Src] = True

    while pq.empty() == False:
        u = pq.get()[1]
        print(u, end=" ")
        if u == target:
            break
        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()


def addEdge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

addEdge(0, 1, 3)
addEdge(0, 2, 6)
addEdge(0, 3, 5)
addEdge(1, 4, 9)
addEdge(1, 5, 8)
addEdge(2, 6, 12)
addEdge(2, 7, 14)
addEdge(3, 8, 7)
addEdge(8, 9, 5)
addEdge(8, 10, 6)
addEdge(9, 11, 1)
addEdge(9, 12, 10)
addEdge(9, 13, 2)
source = 0
target = 9
best_first_search(source, target, v)