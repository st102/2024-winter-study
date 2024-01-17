n = int(input())
a = []
count = 0
pause = True

for i in range(n):
    a.append(int(input()))

while pause is True:

    max_array = 0
    temp = 0

    if n == 1:
        print(count)
        break

    for j in range(n-1):
        if temp < a[j+1]:
            temp = a[j+1]
            max_array = j+1

    if a[0] > temp:
        print(count)
        pause = False
        break

    a[max_array] = a[max_array] - 1
    count = count + 1
    a[0] = a[0] + 1
