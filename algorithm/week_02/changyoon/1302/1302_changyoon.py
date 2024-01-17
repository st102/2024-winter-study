n = int(input())
a = []
b = []
most = 0

for i in range(n):
    a.append((input()))

for i in range(n):
    temp = 0

    for j in range(n):
        if a[i] == a[j]:
            temp = temp + 1

    if most <= temp:
        most = temp
        b.append(i)

if len(b) > 1:
    for j in range(len(b)):
        if a[b[0]] > a[b[j]]:
            a[b[0]] = a[b[j]]
    print(a[b[0]])
else:
    print(a[b[0]])


