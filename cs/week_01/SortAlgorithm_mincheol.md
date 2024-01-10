# 정렬 알고리즘

### 정렬 알고리즘이란?

- 목록 안에 저장된 요소들을 특정한 순서대로 재배치하는 알고리즘
- 입력데이터는 보통 배열과 같은 데이터 구조 (연결리스틑 사용하면 처음 or 끝부터 차례대로 훑어야해서 정렬 시 사용이 복잡해진다)
- 흔히 사용하는 순서 : 숫자 , 사전 순서(A~Z)
- 정렬 방향 : 오름차순, 내림차순

### 사용하는 이유??

- 좀 더 효율적인 알고리즘을 사용하기 위해
- 사람이 읽기 편함을 위한 등등...

### 정렬시 고려사항

- 시간 복잡도
- 메모리 사용량
- 안정성(stability) - > safety가 아니라 stable 이다. -> 데이터의 순서가 바뀌지 않느냐 여부 문제
- 직렬 vs 병렬

**안정성을 잘 모르는 이유**

- "모든 정렬 알고리즘은 같은 키를 가진 데이터의 순서를 안바꾼다"라고 잘못생각함.

모든경우에 대해 최선의 정답을 내는 알고리즘은 없다.

정렬 알고리즘을 선택할때 고려해야할점으로

1. 정렬할 데이터의 양

2. 데이터와 메모리

3. 이미 정렬된 정도

4. 필요한 추가 메모리의 양

5. 상대위치 보존여부(안정성) 등

에따라 선택이 달라질 수 있다.

**정렬알고리즘** 

**1. 선택정렬(Selection Sort)**

방법 : 선택된 값과 나머지 데이터중에 비교하여 알맞은 자리를 찾는 알고리즘. 안정성은 보장되지 않는다.

예시:

![https://blog.kakaocdn.net/dn/blSBFD/btqPem0zr5m/hh4Q5i81KoUXHUwC8TyKik/img.gif](https://blog.kakaocdn.net/dn/blSBFD/btqPem0zr5m/hh4Q5i81KoUXHUwC8TyKik/img.gif)

- 빅오 표기(시간복잡도)

![https://blog.kakaocdn.net/dn/bStM8y/btqFBYiXBb0/mk1Jeq2ZkfdDpY1sCIqDAk/img.png](https://blog.kakaocdn.net/dn/bStM8y/btqFBYiXBb0/mk1Jeq2ZkfdDpY1sCIqDAk/img.png)

**worst,average,best 모두 동일**

---

**2. 삽입정렬(Insertion Sort)**

설명 : -데이터 집합을 순회하면서 정렬이 필요한 요소롤 **뽑아내어** 이를 다시 적당한곳으로 **삽입**하는 알고리즘.

-성능은 버블정렬보다 좋음

예시 :

![https://blog.kakaocdn.net/dn/begzyV/btqO71XwCp9/anVaLURwpwx2Qms15QHRS1/img.gif](https://blog.kakaocdn.net/dn/begzyV/btqO71XwCp9/anVaLURwpwx2Qms15QHRS1/img.gif)

![https://blog.kakaocdn.net/dn/bStM8y/btqFBYiXBb0/mk1Jeq2ZkfdDpY1sCIqDAk/img.png](https://blog.kakaocdn.net/dn/bStM8y/btqFBYiXBb0/mk1Jeq2ZkfdDpY1sCIqDAk/img.png)

**worst,average 동일, best 이미 정렬되어 있다면 O(n)**

---

**3. 버블정렬(Bubble Sort)**

설명 : 거품이 수면으로 올라오는 듯 하여 붙여진 버블정렬. 인접한 두 수를 비교하여 오름차순or 내림차순. 안정성은 보장한다.

예시 :

![https://blog.kakaocdn.net/dn/kTpcI/btqO13hKM3O/hsZY59VnJYPiQVKikxw4N0/img.gif](https://blog.kakaocdn.net/dn/kTpcI/btqO13hKM3O/hsZY59VnJYPiQVKikxw4N0/img.gif)

- 빅오 표기(시간복잡도)

![https://blog.kakaocdn.net/dn/bStM8y/btqFBYiXBb0/mk1Jeq2ZkfdDpY1sCIqDAk/img.png](https://blog.kakaocdn.net/dn/bStM8y/btqFBYiXBb0/mk1Jeq2ZkfdDpY1sCIqDAk/img.png)

**worst,average,best 모두 동일**

---

**4. 병합 정렬(Merge Sort)**

설명 : 둘 이상의 부분집합으로 가르고, 각 부분집합을 정렬한 다음 부분집합들을 다시 정렬된 형태로 합치는 방식. 안정성은 보장한다.

- 분할 정복법 사용**(Divide-And-Conquer)**
1. 분할 : 해결하고자 하는 문제를 작은 크기의 동일한 문제들로 분할한다.
2. 정복 : 각각의 작은 문제를 순환적으로 해결한다.

합병 : 작은 문제의 해를 합하여(merge) 원래 문제에 대한 해를 구한다.

예시 :

![https://blog.kakaocdn.net/dn/bA5bcq/btqO6gHzdBG/lx43EvHWXDaKBrhjz4zVa0/img.gif](https://blog.kakaocdn.net/dn/bA5bcq/btqO6gHzdBG/lx43EvHWXDaKBrhjz4zVa0/img.gif)

- 병합정렬은 다른 대부분의 정렬 알고리즘과 달리 데이터 집합이 메모리에 한번에 올리기에 너무 클때 쓰기 좋은 방법이다. ex. 큰 파일의 내용을 여러개의 작은 파일로 나누어 적당한 알고리즘으로 정렬하고 다시 저장하는 식으로 합치기
- 빅오 표기(시간복잡도)

![https://blog.kakaocdn.net/dn/clRMaD/btqFFUM02kZ/JWMGwsODOYTcrKGj3GXM91/img.png](https://blog.kakaocdn.net/dn/clRMaD/btqFFUM02kZ/JWMGwsODOYTcrKGj3GXM91/img.png)

**worst,average,best 모두 동일**

- ****다른 알고리즘과 비교 했을 때 O(n) 수준의 메모리가 추가로 필요하다는 **단점**

---

5**. 퀵 정렬(Quick Sort)(분할정복)**

**방법** :  데이터 집합내에 임의의 기준(pivot)값을 정하고 해당 피벗으로 집합을 기준으로 두개의 부분 집합으로 나눈다.

한쪽 부분에는 피벗값보다 작은값들만, 다른 한쪽은 큰값들만 넣는다. 안정성 보장 X

더 이상 쪼갤 부분 집합이 없을 때까지 각각의 부분 집합에 대해 피벗/쪼개기 재귀적으로 적용.

**예시  :**

![https://blog.kakaocdn.net/dn/sVgeg/btqO6hT6nVq/APxheX0siKi3SJRHxvx3n0/img.gif](https://blog.kakaocdn.net/dn/sVgeg/btqO6hT6nVq/APxheX0siKi3SJRHxvx3n0/img.gif)

- 병합정렬과 마찬가지로 분할 정복법 사용**(Divide-And-Conquer)**
- **범위, 기준, 비교, 스왑**으로 순서
- 빅오 표기(시간복잡도)

![https://blog.kakaocdn.net/dn/clRMaD/btqFFUM02kZ/JWMGwsODOYTcrKGj3GXM91/img.png](https://blog.kakaocdn.net/dn/clRMaD/btqFFUM02kZ/JWMGwsODOYTcrKGj3GXM91/img.png)

**average,best동일**

![https://blog.kakaocdn.net/dn/dBBfL4/btqFHrb5Qyy/4l53w62pRV4arlKK18uNVK/img.png](https://blog.kakaocdn.net/dn/dBBfL4/btqFHrb5Qyy/4l53w62pRV4arlKK18uNVK/img.png)

**worst**