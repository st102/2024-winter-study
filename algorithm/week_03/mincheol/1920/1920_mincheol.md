# 1920 수찾기_민철

<aside>
📌 **문제 링크** 
[https://www.acmicpc.net/problem/1049](https://www.acmicpc.net/problem/1920)

</aside>

## **입력**

첫째 줄 : 1≤N≤100,000

둘쨰 줄 : N개의 정수

셋쨰 줄 : 1≤M≤100,000

넷쨰 줄 : M개의 정수

모든 정수의 범위는 -2^31 보다 크거나 같고 2^31보다 작다.

---

## 문제풀이

<aside>
💡 입력의 크기가 너무 크므로 단순 선형 탐색으로는 문제를 풀 수 없음
100,000 * 100,000

</aside>

- 이진 탐색 트리를 제작하려 함
    
    ![Untitled](1920%20%E1%84%89%E1%85%AE%E1%84%8E%E1%85%A1%E1%86%BD%E1%84%80%E1%85%B5_%E1%84%86%E1%85%B5%E1%86%AB%E1%84%8E%E1%85%A5%E1%86%AF%207d678bb71d46412a9d22a6164423052b/Untitled.png)
    

구현 중 코드가 너무 복잡하여 다른 방법 탐색

- 배열 이용

100,000 크기의 배열을 만들어준 후

입력받은 인덱스의 해당되는 배열값을 1로 변경

이후 M의 값을 인덱스로 넣어 값 비교

배열의 크기가 너무 커서 시간 내로 끝낼 수 없음, 선형탐색과 다르지 않은 방법

- 딕셔너리 이용

딕셔너리의 key 탐색 방법이 이진탐색이므로 nlogn의 크기로 탐색할 수 있으므로 이를 이용하여 문제 해결

N개의 정수를 dict의 key값으로 입력받음

M개의 정수 중 key값이 존재하면 1을 아니면 0을 출

> 👀***!***
dict 등 여러 자료구조의 Big O값을 알아두면 문제를 해결하기 훨씬 수월함
> 

---

## 결과

메모리 51312KB, 시간 176ms

```python
n = int(input())
narr = list(map(int, input().split()))

m = int(input())

marr = list(map(int, input().split()))

dict = {}
for i in narr:
    dict[i] = 1
   
for j in marr:
    if j in dict:
        print('1')
    elif not j in dict:
        print('0')
```