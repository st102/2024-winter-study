# 두 수 비교하기 - 1330 

[문제 링크](https://www.acmicpc.net/problem/1330) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

구현

### 문제 풀이

```python
a, b = map(int,input().split())

if a > b:
    print(">")
elif a == b:
    print("==")
else:
    print("<")
```

a,b에 입력한 정수 저장 <br/>
조건문을 통해 a가 b보다 크다면 print(">"), <br/>
a가 b와 같다면 print("=="), <br/>
a가 b보다 작다면 print("<") 를 출력

### 문제 설명

<p>두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.</p>

### 출력 

 <p>첫째 줄에 다음 세 가지 중 하나를 출력한다.</p>

<ul>
	<li>A가 B보다 큰 경우에는 '<code>></code>'를 출력한다.</li>
	<li>A가 B보다 작은 경우에는 '<code><</code>'를 출력한다.</li>
	<li>A와 B가 같은 경우에는 '<code>==</code>'를 출력한다.</li>
</ul>