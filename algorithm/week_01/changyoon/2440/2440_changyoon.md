# 별 찍기 - 3 - 2440 

[문제 링크](https://www.acmicpc.net/problem/2440) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

구현

### 문제 풀이

```python
a = int(input())

for i in range(a):
    b = a-i
    print(b * "*")
```

a에 반복을 할 횟수를 입력 받음 <br/>
그 후 b에 a - ( i번째 반복, i는 0부터 시작 ) 로 저장 <br/>
별의 개수를 b의 개수 만큼 출력

### 문제 설명

<p>첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제</p>

### 입력 

 <p>첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.</p>

### 출력 

 <p>첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.</p>