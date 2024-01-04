# Vowel Count

## 문제 설명

*   두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

## 나의 풀이 방법

```cpp
a,b=input().split()
a=int(a)
b=int(b)

if(a>b):
    print(">")
elif(a<b):
    print("<")
else:
    print("==")

```

*   변수 a, b에 input().split()을 사용하여 빈칸을 기준으로 각각 순서에 맞게 저장하였다.
*   a, b가 현재 string type으로 int type으로 변경해주었다.
*   if문을 사용하여 >, < 인 경우를 지정하였으며 그외인 ==은 else를 사용하여 원하는 결과값이 나오도록 하였다.

## 배운 점

*   두 가지의 변수를 저장하는 방법을 배웠다.
*   int(input().split()) 코드로 한번에 int형식으로 받으려고 했으나 실패했다 각각 해주어야 한다고 한다.

## 반성할 점

*   없음

## Action Item

*   input().split()로 문제를 풀이하니 c++때와는 코드의 간결함에 감격했다.