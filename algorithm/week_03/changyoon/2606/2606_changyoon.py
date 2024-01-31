a = int(input())
b = int(input())

ary = []
check = []

for i in range(b):
    ary.append(list(map(int, input().split())))

for i in range(b):
    if len(check) == 0 and ary[i][0] == 1 or ary[i][1] == 1:
        check.append(ary[i][0])
        check.append(ary[i][1])
    elif ary[i][0] in check and ary[i][1] in check:
        pass
    elif ary[i][0] in check and len(check) != 0:
        check.append(ary[i][1])
    elif ary[i][1] in check and len(check) != 0:
        check.append(ary[i][0])

print(len(check) - 1)