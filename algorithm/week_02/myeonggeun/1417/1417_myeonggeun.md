# 국회의원 선거

## 문제 설명

*   다솜이는 사람의 마음을 읽을 수 있는 기계를 가지고 있다. 다솜이는 이 기계를 이용해서 2008년 4월 9일 국회의원 선거를 조작하려고 한다.

*   다솜이의 기계는 각 사람들이 누구를 찍을 지 미리 읽을 수 있다. 어떤 사람이 누구를 찍을 지 정했으면, 반드시 선거때 그 사람을 찍는다.

*   현재 형택구에 나온 국회의원 후보는 N명이다. 다솜이는 이 기계를 이용해서 그 마을의 주민 M명의 마음을 모두 읽었다.

*   다솜이는 기호 1번이다. 다솜이는 사람들의 마음을 읽어서 자신을 찍지 않으려는 사람을 돈으로 매수해서 국회의원에 당선이 되게 하려고 한다. 다른 모든 사람의 득표수 보다 많은 득표수를 가질 때, 그 사람이 국회의원에 당선된다.

*   예를 들어서, 마음을 읽은 결과 기호 1번이 5표, 기호 2번이 7표, 기호 3번이 7표 라고 한다면, 다솜이는 2번 후보를 찍으려고 하던 사람 1명과, 3번 후보를 찍으려고 하던 사람 1명을 돈으로 매수하면, 국회의원에 당선이 된다.

*   돈으로 매수한 사람은 반드시 다솜이를 찍는다고 가정한다.

*   다솜이가 매수해야하는 사람의 최솟값을 출력하는 프로그램을 작성하시오.

## 성능 요약

메모리: 31120 KB, 시간: 48 ms

## 나의 풀이 방법

```python
number = int(input())
dasom = int(input())
candidate = []
count=0

for x in range(0,number-1):
    vote=int(input())
    candidate.append(vote)
candidate.sort(reverse=True)
if number==1:
    print(0)
else:
    while candidate[0] >= dasom:
        count+=1
        dasom+=1
        candidate[0]-=1
        candidate.sort(reverse=True)
    print(count)
```

*   후보의 수를 number, 1번을 찍으려고 하는 사람의 수를 dasom, 이외 후보를 candidate 리스트에 입력 받는다.
*   candidate 배열을 오름차순으로 정렬하여 가장 특표가 높은 후보자가 0번째 index에 위치하도록 한다.
*   특표가 가장 높은 후보자 같다면 0을 출력하고 이외는 while문으로 몇명을 돈으로 매수해야하는지 결정한다.
*   while문에서 특이점이라고 하면 가장 높은 후보자가 나오기 위해 계속 sort를 사용하여 오름차순으로 정렬한다.

## 배운 점

*   while문 사용법을 배웠다.

## 반성할 점

*   없음

## Action Item

*   sort 역으로 정렬하는 방법에 rever=True를 알게되었다.