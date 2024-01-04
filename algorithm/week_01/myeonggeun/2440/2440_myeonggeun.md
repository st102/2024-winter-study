# Vowel Count

## 문제 설명

*   첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제

## 나의 풀이 방법

```cpp
input_number = int(input())
temp = input_number+1

for i in range(1,input_number+1) :
    for j in range(1, temp) :
        print("*", end="")
    print("")
    temp-=1
```

*   정수로 변수를 입력받고 반복문에서 숫자를 줄이기 위한 temp 변수를 만든다.
*   반복문 두개를 사용하여 1번째 반복문에는 N번째 줄까지 출력을 2번째 반복문에서는 N개의 별을 찍도록한다.
*   두 번째 반복문이 끝날때마다 줄바꿈과 temp의 수를 1 줄인다.

## 배운 점

*   for문 사용법을 배웠다.
*   print를 출력할 때 end로 문자의 마지막에 추가되는 문자열을 지정할 수 있다는 것을 배웠다.

## 반성할 점

*   없음

## Action Item

*   print할때 자동으로 줄바꿈이 된다니 신기했지만 \n으로 구분하여 출력할 수 없이 print만 여러번 나오게 되는 상황이 온다면 다소 귀찮을 수도 있을 것 같다는 생각이 들었다.