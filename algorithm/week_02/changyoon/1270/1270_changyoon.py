n = int(input())

output = []
for i in range(n):
    most = 0
    a = list(map(int, input().split()))

    for j in range(1,len(a)-1):
        temp = 1
        for k in range(j+1,len(a)):
            if a[j] == a[k]:
                temp = temp + 1

        if most < temp:
            most = temp

    if most > a[0] / 2:
        output.append(a[most])
    else:
        output.append("SYJKGW")

for i in range(n):
    print(output[i])