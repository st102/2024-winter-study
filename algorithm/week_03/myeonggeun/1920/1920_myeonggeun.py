def binary_search(arr,target):
    low, high=0,len(arr)-1
    
    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return 1
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
        
    return 0

number=int(input())
numbers=list(map(int, input().split()))
compare=int(input())
compares=list(map(int, input().split()))
numbers.sort()
for _ in compares:
    print(binary_search(numbers,_))