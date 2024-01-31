# 수 찾기

### 성능 요약

메모리: 46712 KB, 시간: 412 ms

### 분류

이분 탐색, 자료 구조, 정렬

### 문제 설명

<p>N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -2<sup>31</sup> 보다 크거나 같고 2<sup>31</sup>보다 작다.</p>

### 출력 

 <p>M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.</p>

## 나의 풀이 방법

```python
def binary_search(arr,target):
    low, high=0,len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return 1
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return 0

number=int(input())
numbers=list(map(int, input().split()))
compare=int(input())
compares=list(map(int, input().split()))
numbers.sort()
for _ in compares:
    print(binary_search(numbers,_))
```

*   이진 탐색 기법을 사용하여 함수를 구성하여 풀이하였다.

## 배운 점

*   없음

## 반성할 점

*   이진 탐색 이전에 선형 탐색 알고리즘을 사용하여 문제를 풀었지만 시간 초과가 되었다. 입력값에서 힌트를 인지하고 문제를 풀이하였어야 했는데 이를 놓쳤다.

## Action Item

*   없음