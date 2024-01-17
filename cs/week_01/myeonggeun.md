# 1주차 알고리즘 - 정렬

## Selection Sort, 선택 정렬

정의 : 데이터 중 가장 작은 값을 데이터로 선택하여 앞으로 보내는 정렬

시간복잡도 : O ( N * N ) 

- Worst, Average = O(N^2)

## Insertion Sorot, 삽입 정렬

정의 : 데이터를 순서대로 뽑아 적절한 위치를 찾아 삽입하는 정렬

시간복잡도 : O ( N * N )

- Worst = O(N^2)
- Average = O(N)

## Bubble Sort, 버블 정렬

정의 : 옆에 있는 데이터와 비교하여 더 작은 값을 앞으로 보내는 정렬

시간복잡도 : O ( N * N )

- Worst, Average, Best = O(N*2)

## Merge Sort, 합병 정렬

정의 : 데이터 배열을 2개 이상의 부분 배열로 분할하고 부분 배열에서 정렬을 한 뒤 결합하여 다시 정렬을 진행, 데이터 배열 전체가 다시 결합되고 정렬되면서 마침

시간복잡도 :  O ( N log N )

- Worst, Average, Best = O ( N log N )

## Heap Sort, 힙 정렬

정의 : 이진트리 기반의 트리형 자료구조로써 최솟값이나 최대값 찾음

시간복잡도 : O ( N log N )

- Worst, Average, Best = O ( N log N )

## Quick Sort, 퀵 정렬

정의 : 데이터 중 임의의 기준값을 정해서 두 부분 집합으로 나눔, 이때의 기준 값을 피벗(Pivot)이라고 하고 왼쪽은 피벗보다 작은 값, 오른쪽은 피벗보다 큰 값을 배치하고 더 이상 집합을 나눌 수 없을 때까지 재귀

시간복잡도 : O ( N log N )

- Worst = O ( N^2 )
- Average, Best = O ( N log N )

## Radix Sort, 기수 정렬

정의 : 낮은 자릿수부터 비교하여 완성하는 정렬

시간복잡도 : O(dN)이며 d는 자릿수