a = int(input())
b = list(map(int, input().split()))
c = int(input())
d = list(map(int, input().split()))

ary = sorted(b)

for i in range(c):
    low = 0
    high = len(ary) - 1
    count = False

    while low <= high:
        mid = (low + high) // 2

        if ary[mid] == d[i]:
            print("1")
            count = True
            break
        elif ary[mid] > d[i]:
            high = mid - 1
        else:
            low = mid + 1

    if not count:
        print("0")