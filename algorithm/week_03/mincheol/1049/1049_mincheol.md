# 1049 기타줄_민철

<aside>
📌 **문제 링크** 
[https://www.acmicpc.net/problem/1049](https://www.acmicpc.net/problem/1049)

</aside>

## **입력**

첫째 줄 : 끊어진 줄의 개수(N≤100), 기타줄 브랜드 개수(M≤50)

이후 : 패키지 가격, 낱개의 가격

---

## 문제풀이

생각나는 적용할 만한 방법이 없어 Greedy의 방식을 이용

세가지 상황의 값을 각각 구한 후 가장 작은 값을 최솟값으로 출력

1. 패기지(6개)만을 이용하여 사는 경우
2. 패기지(6개)를 이용하여 구매한 후 나머지는 낱개로 사는 경우
3. 낱개로만 구매하는 경우

<aside>
💡 입력의 크기가 100, 50이므로 우선 시간에 구애 받지 않고 문제 해결

</aside>

> 👀***!***
코딩 테스트를 푸는 경우에 너무 배웠던 알고리즘에만 집착하지 말고 생각나지 않는다면 입력 값의 크기를 본 후 가능하면 그리디의 방법이라도 이용하자
> 

> 👀***!***
푼 이후 알게 된 것 :
파이썬에는 max, min이 있다 잘 이용하기!
> 

---

## 결과

메모리 31120KB, 시간 60ms

```python
n, m = map(int, input().split())

min_pack = 1000
min_one = 1000
for i in range(m):
    pack, one = map(int, input().split())
    if pack < min_pack:
        min_pack = pack
    if one < min_one:
        min_one = one
        
min_price = min_one * n
price = (n//6 + 1) * min_pack
if price < min_price:
    min_price = price

price = (n//6) * min_pack + (n%6) * min_one
if price < min_price:
    min_price = price
    
print(min_price)
```