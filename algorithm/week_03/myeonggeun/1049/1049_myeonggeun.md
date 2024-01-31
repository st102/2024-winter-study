# 기타줄

### 성능 요약

메모리: 31120 KB, 시간: 44 ms

### 분류

그리디 알고리즘, 수학

### 문제 설명

<p>Day Of Mourning의 기타리스트 강토가 사용하는 기타에서 N개의 줄이 끊어졌다. 따라서 새로운 줄을 사거나 교체해야 한다. 강토는 되도록이면 돈을 적게 쓰려고 한다. 6줄 패키지를 살 수도 있고, 1개 또는 그 이상의 줄을 낱개로 살 수도 있다.</p>

<p>끊어진 기타줄의 개수 N과 기타줄 브랜드 M개가 주어지고, 각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격, 낱개로 살 때의 가격이 주어질 때, 적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N과 M이 주어진다. N은 100보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에는 각 브랜드의 패키지 가격과 낱개의 가격이 공백으로 구분하여 주어진다. 가격은 0보다 크거나 같고, 1,000보다 작거나 같은 정수이다.</p>

### 출력 

 <p>첫째 줄에 기타줄을 적어도 N개 사기 위해 필요한 돈의 최솟값을 출력한다.</p>

## 나의 풀이 방법

```python
purchase, numbers=list(map(int,input().split()))

packages=[]
eaches=[]

for _ in range(numbers):
    package, each=list(map(int, input().split()))
    packages.append(package)
    eaches.append(each)

min_package=min(packages)
min_each=min(eaches)

if min_package/6 > min_each:
    print(min_each*purchase)
else:
    package_purchase, leave=divmod(purchase,6)
    if min_package < leave*min_each:
        print(min_package*(package_purchase+1))
    else:
        print(min_package*package_purchase + min_each*leave)
```

*   문제 설명에서 되도록이면 적게 사용해야된다는 점에서 최소값으로 min함수를 사용하고 최대 50개의 묶음과 개별 가격이 주어지기에 배열에 모두 담아도 시간초과가 나지 않을 것 같아서 그대로 사용하여 문제를 풀이하였다.
*   packages, eaches에서 묶음과 개별의 가격을 모두 받은 후 최소값을 추출하였다.
*   추출한 최소값들에서 묶음과 개별을 조절하여 가장 적은 값으로 기타줄을 살 수 있도록 구현하였다.

## 배운 점

*   python의 나눗셈과 몫에 대해서 / // % divmod 등 알게되었다.

## 반성할 점

*   없음

## Action Item

*   없음