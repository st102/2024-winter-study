# 2606 바이러스_민철

<aside>
📌 **문제 링크** 
[https://www.acmicpc.net/problem/2606](https://www.acmicpc.net/problem/2606)

</aside>

## **입력**

첫째 줄 : 컴퓨터의 수(100이하인 양의 정수)

둘째 줄 : 네트워크상 직접 연결되어있는 컴퓨터 쌍의 수(99+98+97+…+1)

번호의 쌍

---

## 문제풀이

컴퓨터의 수와 네트워크 상에서 서로 연결어있음 →그래프 문제로 해석

각 컴퓨터 → node

네트워크 → edge

⇒ 바이러스가 걸리게되는 컴퓨터의 수 → 연결성분에 포함되어있는 컴퓨터의 수

<aside>
💡 입력이 100이하이므로 adj matrix로 나타내고 2중 for-loop을 사용해도 100*100이므로 사용가능 예상

</aside>

그래프의 연결성분 → bfs를 통해 방문한 노드를 알아낼 수 있다

queue를 이용하여 bfs구현

이차원 배열의 값이 1인경우 visited의 값이 0인 경우에 queue에 노드 값을 추가해주고 count++을 해준 후 count 출력

> 👀***!***
dfs → stack 이용
bfs → queue 이용
dfs, bfs → 백트래킹 이용히여 구현 가능
※백트레킹의 경우 입력값에 따라 알고리즘의 크기가 너무 커질 수 있음
> 

---

## 결과

메모리 37852KB, 시간 132ms

```python
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
```