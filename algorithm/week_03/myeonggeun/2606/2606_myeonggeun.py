computer = int(input())
number = int(input())

graph = [[] for _ in range(computer+1)]
visited = [False] * (computer+1)
count=-1

for _ in range(number):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    global count
    visited[v]=True
    count+=1
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

dfs(1)
print(count)