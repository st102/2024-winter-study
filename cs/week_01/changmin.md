# 정렬 알고리즘
## 1. 선택정렬
정렬되지 않은 요소들 중에 최소값을 찾아 앞으로 가져온다<br>
### 특징
- Not-Stable 알고리즘
- InPlace 알고리즘
- 시간 복잡도 : O(n)

```python
def selectionSort(arr):
    n = len(arr)
    
    for i in range(n):
        minIdx = i:
        
        for j in range(i+1,n):
            if arr[j] < arr[minIdx]: 
                minInex = j 

        arr[i], array[minIdx] = array[minIdx], arr[i]
```

## 2. 삽입정렬
정렬되지 않은 요소에 대해 정렬되어 있는 요소들 사이에서의 위치를 찾아 삽입해준다.
### 특징
- Stable 알고리즘
- InPlace 알고리즘
- 시간 복잡도 
    - Average, Worst : O(n^2), Best : O(n)

```python
def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
```

## 3. 버블 정렬
인접한 두수를 비교하여 큰 수가 뒤로 가게하는 정렬방법이다 </br>
앞에서부터 시작하면 맨 끝부터 뒤에서부터 시작하면 맨 앞부터 정렬된다.
### 특징
- Stable 알고리즘
- InPlace 알고리즘
- 시간 복잡도 : O(n^2)

```python
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

## 4. 병합 정렬
배열을 계속해서 절반으로 나눈 다음 각 부분집합들을 합치며 정렬하는 방법</br>
Divide-Conqur 방식
### 특징
- Stable 알고리즘
- Not-InPlace 알고리즘
- 시간 복잡도 : O(nlogn)
#### Ver1 - 새로운 배열 생성
```python
def mergeSort(arr):
    if len(arr) < 2:
        return arr
    
    mid = arr // 2
    lArr, rArr =  mergeSrot(arr[:mid]),  mergeSrot(arr[mid:])

    l = r = 0

    result = []
    while l < len(lArr) and r < len(rArr):
        if lArr[l] < rArr[r]:
            result.append(lArr[l])
            l += 1
        else:
            result.append(rArr[r])
            r += 1

    result += lArr[l:]
    result += rArr[r:]
    return result

```
#### Ver2 - 변수 사용
```python
def mergeSort(arr):
    def partition(low,high):
        if high - low < 2:
            return
        
        m = h - l // 2
        partition(low,mid)
        partition(mid,high)
        merge(low,mid,high)

    def merge(low, mid, high):
        result = []
        l, r = low, mid

        while l < mid and h < high:
            if arr[l] < arr[r]
                result.append(arr[l])
                l += 1
            else 
                result.append(arr[r])
                r += 1    
        
        if l < mid:
            result += arr[l:mid]
        if r < high:
            result += arr[h:high]

        for i in range(low, high):
            arr[i] = result[i - low]
```

## 5. 퀵 정렬
임의의 피벗 선택 후 배열을 피벗보다 큰 수는 오른쪽 작은 수는 왼쪽으로 집합을 2개로 나누어 해당 과정을 반복한다.</br>
Divid-Conqur 방식
### 특징
- Not-Stable 알고리즘
- InPlace,Not-InPlace 알고리즘
- 시간 복잡도
    - Averga,Best : O(nlogn), Worst : O(n^2)

#### Ver1 - InPlace
```python
def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)

```
#### Ver1 - Not-InPlace
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
            
```

## 6. 힙 정렬
주어진 배열을 최대 힙(내림차순) 혹은 최소 힙(오름차순) 형태로 구성하여 정렬하는 방식이다.
- Not-Stable 알고리즘
- InPlace,Not-InPlace 알고리즘
- 시간 복잡도 : O(nlogn)

```python
코드 짜보자...
```

## 7. 계수 정렬
## 8. 기수 정렬