# 자료구조

## 1. Array (배열)
- 동일한 타입의 데이터들을 저장가능하며, 고정된 크기를 가지고 있다.
- 인덱싱이 되어 있어 인덱스 번호로 데이터에 접근할 수 있다. 
   - 인덱스를 지정하여 접근하기 때문에 모든 요소에 빠르게 접근 가능
 

### 용도

- 특정 요소를 빠르게 읽어야 할 때
- 다차원 데이터를 다룰 때

## 2. Linked List (연결 리스트)

- 각 노드가 데이터와 포인터를 가지고 한 줄로 연결되어 있는 방식으로 데이터를 저장하는 자료구조
   - 각 요소는 node
   - 각 node에는 key와 다음 노드를 가르키는 tail 포함
   - 첫 번째 요소는 head
   - 마지막 요소는 tail
- 배열의 크기를 미리 선언해야 하는 배열 리스트와 달리 연결 리스트는 데이터의 숫자만큼만 메모리를 사용하면 되니 메모리 낭비가 적다.
- 특정 요소에 접근하러면 처음부터 방문해야하기 때문에 속도가 느리다

### 용도
- 데이터의 삽입과 추가가 빈번하게 일어날때

## 3. Stack (스택)
- 한 방향으로만 입력할 수 있는 자료구조로 중간에 값을 끼어 넣어 저장할 수 없다. 
   - 즉, 같은 크기의 자료를 정해진 한 방향으로만 입력, 저장, 삭제가 가능하다.
- 후입선출(Last In First Out, LIFO) 구조
   -  마지막에 들어온 데이터가 가장 먼저 리턴, 삭제된다.

### 용도
   - 깊이 우선 탐색
   - 재귀 함수 호출 구현

## 4. Queue (큐)
- 양 방향에서 입력과 출력이 진행되는 자료구조로 중간에 값을 끼어 넣어 저장할 수 없다
- 선입선출(First In First Out, FIFO) 구조이다.
    -  가장 먼저 들어온 데이터가 가장 먼저 리턴, 출력된다

### 용도
   - 너비 우선 탐색

## 5. Tree (트리)
- 노드들이 계층적으로 연결된 비선형 자료구조이다.
- 최상위 노드(루트)가 있고 최상위 노드 아래에 다른 하위 노드가 있고 그 하위 노드 안에는 또 다른 하위 노드가 있는 부모(parent)와 자식(child) 형태이다.

### 용도
- BST
- Heap
- Binary Tree

## 6. Heap (힙)
- 완전 이진 트리의 형태로 만들어진 자료구조
   - 삽입과 삭제시 O(nlogn) 소요
- 최대 힙(max heap) : 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진 트리
- 최소 힙(min heap) : 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진 트리

### 용도
- 최댓값 혹은 최솟값을 빠르게 찾아내기 위해 사용 (우선순위 큐, 힙 정렬)

## 7. Hash Table (해시 테이블)
- 해시함수를 사용하여 변환한 값을 색인(index)으로 삼아 키(key)와 데이터(value)를 저장하는 자료구조
  - 보통 버킷(bucket)이라는 작은 서브그룹에 키/데이터 쌍 저장
- 데이터의 크기에 관계없이 삽입 및 검색에 매우 효율적

## 8. Graph(그래프)
- 정점(Vertex)과 간선(edge)으로 이루어진 자료구조
   - 정점(Vertex) : 노드(node)라고도 하며 정점에는 데이터가 저장
   - 간선(edge) : 링크(arcs)라고도 하며 노드간의 관계를 나타낸다.
- 그래프는 정점마다 간선이 없을수도 있고 있을수도 있으며 루트 노드, 부모와 자식이라는 개념이 존재하지 않는 부분에서 트리와 다르다.
   - 방향(directed) 그래프
   - 무방향(undirected) 그래프