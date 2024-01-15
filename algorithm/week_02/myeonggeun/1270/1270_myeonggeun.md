# 땅따먹기

## 문제 설명

*   드디어 전쟁은 전면전이 시작되었고, 서로 땅을 따먹기 시작했다.

*   현재 여러 지역은 한창 전쟁이 벌어지고 있는 상황인데, 어느 지역은 거의 전쟁이 마무리 단계로 가고 있다.

*   하지만 당신은 군대를 보낼 때 적군을 혼란시키기 위해서 우리 나라의 군대라는걸 표시하지 않고, 군대의 번호로 표시했다.

*   어느 땅에서 한 번호의 군대의 병사가 절반을 초과한다면 그 땅은 그 번호의 군대의 지배하에 놓이게 된다.

*   이때, 각 땅들을 지배한 군대의 번호를 출력하여라. 만약, 아직 전쟁이 한창중인 땅이라면 “SYJKGW”을 쌍 따옴표 없이 출력한다.

## 성능 요약

*   메모리: 51660 KB, 시간: 9976 ms

## 나의 풀이 방법

```python
number = int(input())
check=True
answer=[]
for _ in range(number):
    check=True
    area_count=list(map(int, input().split()))
    areas = area_count[0]
    area_count.pop(0)
    wars={}

    for x in area_count:
        if(x not in wars):
            wars[x]=1
        else:
            wars[x]+=1

    max_soldier=max(wars.values())
    if areas < max_soldier*2:
        for key, value in wars.items():
            if max_soldier==value:
                answer.append(key)
    else:
        answer.append("SYJKGW")
        
for y in answer:
    print(y)
```

*   땅의 개수를 number, 땅의 병사 수 및 군대 번호를 area_count에 담는다.
*   areas로 땅의 병사 수를 담고 area_count에서 제거한다.
*   각 번호와 개수를 담는 for문을 만들고 가장 높은 군대 번호를 비교하여 SYJKGW 혹은 승리한 군대 번호를 배열에 담아 마지막에 출력한다.

## 배운 점

*   없음

## 반성할 점

*   없음

## Action Item

*   이전에 풀었던 문제와 비슷하게 생각하여 풀었으나 딕셔너리에 대한 이해도와 사용법이 부족함을 인지하고 더 알아가야겠다.
*   채점하는데 시간이 오래걸렸다. 좀 더 효율적인 코드를 짤 수 있도록 다시 봐야한다.