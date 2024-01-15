number = int(input())
check=True
answer=[]
for _ in range(number):
    check=True
    area_count=list(map(int, input().split()))
    areas = area_count[0]
    area_count.pop(0)
    wars={}

    for x in area_count:
        if(x not in wars):
            wars[x]=1
        else:
            wars[x]+=1

    max_soldier=max(wars.values())
    if areas < max_soldier*2:
        for key, value in wars.items():
            if max_soldier==value:
                answer.append(key)
    else:
        answer.append("SYJKGW")
        
for y in answer:
    print(y)