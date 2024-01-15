# 베스트셀러

## 문제 설명

*   김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.

*   오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

## 성능 요약

메모리: 31120 KB, 시간: 44 ms

## 나의 풀이 방법

```python
number = int(input())
books = {}

for x in range(number):
    name = input()
    if name not in books:
        books[name]=1
    else:
        books[name]+=1

max_sell = max(books.values())
max_books=[]

for key, value in books.items():
    if value==max_sell:
        max_books.append(key)

max_books.sort()
print(max_books[0])
```

*   도서의 수를 number, 팔린 도서와 개수를 저장하는 books를 입력받는다.
*   books에 도서가 있다면 수를 늘리고 없다면 1로 값을 저장한다.
*   가장 많이 팔린 도서의 개수를 max_sell에 저장하며 같은 수들의 도서를 배열에 담고 내림차순으로 정렬하여 0번째 index를 출력한다.

## 배운 점

*   c++에서 주로 사용했던 pair를 사용하기 위해 찾았으나 비슷한 딕셔너리 자료형을 알고 사용할 수 있게 되었다.
*   not in 을 사용하여 편하게 딕셔너리에 있는지 확인하는 법을 알게되었다.

## 반성할 점

*   if문을 사용할 때 괄호를 계속 생성하게 되어 불필요하게 지우는 작업을 하는 점을 고려하여 문제 풀이 속도를 늘리자

## Action Item

*   for문에서 key, value를 사용할 때는 books.items()를 in에 둬야한다.