numC = int(input())
numE = int(input())
graph = [[0 for j in range(numC)] for i in range(numC)]
for i in range(numE):
    a, b = map(int,input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
    
import queue
bfs = queue.Queue()
bfs.put(0)

visited = [0]
visited = visited * numC
visited[0] = 1

count = 0

while not bfs.empty():
    a = bfs.get()
    for i in range(numC):
        if graph[a][i] == 1 and visited[i] == 0:
            count = count + 1
            visited[i] = 1
            bfs.put(i)
            
print(count)