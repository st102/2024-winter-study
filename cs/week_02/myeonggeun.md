# 2주차 알고리즘 - 탐색

## 탐색 알고리즘

- 저장된 데이터들 중에 원하는 값을 찾는 문제

### 선형 탐색 알고리즘 (Linear Search Algorithm)

- 맨 앞이나, 맨 뒤부터 순서대로 하나씩 찾아보는 알고리즘
- 가장 단순하고 간단한 탐색 알고리즘

**특징**

- 순차적 탐색, 단순하고 직관적임

**탐색 과정**

1. 맨 끝부터 하나하나 원하는 값을 찾아본다.
2. 원하는 값을 찾으면, 탐색을 종료

**시간 복잡도** : O(n)

- best : 1
- worst : O(n)

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # 찾은 경우 해당 요소의 인덱스를 반환
    return -1  # 찾지 못한 경우 -1 반환
```

### 이진 탐색 알고리즘 (Binary Search Algorithm)

- 정렬된 데이터 집합에서 원하는 값을 빠르게 찾기 위한 탐색 알고리즘

**특징**

- 정렬된 데이터에서 사용
- 분할 정복 전략

**탐색 과정**

1. 중간지점을 선택한 뒤, 중간지점을 기준으로 왼쪽 혹은 오른쪽 부분만 남긴다.
2. 남긴 부분 중에서 다시 중간지점을 선택한 뒤, 왼쪽 혹은 오른쪽만 남긴다.
3. 위 과정을 원하는 값을 찾거나 검색 범위가 더 이상 줄어들지 않을 때 종료

**시간 복잡도** :  O(log n)

- best : 1
- worst : O(log n)

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # 찾은 경우 해당 요소의 인덱스를 반환
        elif mid_value < target:
            low = mid + 1  # 중간값보다 큰 범위에서 다시 탐색
        else:
            high = mid - 1  # 중간값보다 작은 범위에서 다시 탐색

    return -1  # 찾지 못한 경우 -1 반환
```

### 깊이 우선 탐색 알고리즘 (Depth-First Search, DFS)

- 그래프나 트리와 같은 구조에서 한 노드에서 시작하여 가능한 한 깊이 들어가면 탐색하는 방법

**특징**

- 깊이 우선
- 스택 또는 재귀 사용
- 방문 여부 표시

**탐색 과정**

1. 시작 노드를 방문하고 표시
2. 현재 노드와 이웃한 노드를 확인
3. 방문하지 않은 이웃 노드가 있으면 해당 노드로 이동
4. 방문하지 않은 이웃 노드가 없다면 이전 단계로 돌아감
5. 배열이 비어질 때까지 반복

**시간 복잡도**: O(V+E) - V(노드의 수), E(간선의 수)

- best, worst : O(V + E)

```python
def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

# 예시 그래프
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# 시작 노드 설정
start_node = 'A'

# 방문 여부를 나타내는 집합
visited_set = set()

# DFS 실행
dfs(graph, start_node, visited_set)
```

### 너비 우선 탐색 알고리즘 (Breath-First Search, BFS)

- 그래프나 트리에서 한 노드에서 시작하여 인접한 모든 노드를 먼저 탐색하는 방법

**특징**

- 너비 우선
- 큐 사용
- 방문 여부 표시

**탐색 과정**

1. 시작 노드를 큐에 추가하고 방문 표시
2. 큐가 비어질 때까지 반복
3. 큐에서 하나의 노드를 추출
4. 현재 노드와 인접한 노드들을 확인
5. 큐에서 추출한 노드를 출력하거나 처리
6. 큐에 노드가 남아있다면 3번으로 돌아가 반복

**시간 복잡도**: O(V+E) - V(노드의 수), E(간선의 수)

- best, worst : O(V + E)

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(current_node, end=' ')
            visited.add(current_node)
            queue.extend(graph[current_node])

# 예시 그래프
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# 시작 노드 설정
start_node = 'A'

# BFS 실행
bfs(graph, start_node)
```

### 해시 탐색 알고리즘 (Hash Search Algorithm)

- 해시 함수를 사용하여 데이터를 저장하고 검색하는 방법

특징

- 빠른 검색 속도
- 해시 충돌에 대한 처리
- 메모리 효율성

탐색 과정

- 해시 함수 적용
- 해시 테이블에서 검색
- 충돌 처리

시간 복잡도 : O(1)

- best : O(1)
- worst : O(n)