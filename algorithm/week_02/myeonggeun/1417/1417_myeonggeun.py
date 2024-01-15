number = int(input())
dasom = int(input())
candidate = []
count=0

for x in range(0,number-1):
    vote=int(input())
    candidate.append(vote)
candidate.sort(reverse=True)
if number==1:
    print(0)
else:
    while candidate[0] >= dasom:
        count+=1
        dasom+=1
        candidate[0]-=1
        candidate.sort(reverse=True)
    print(count)