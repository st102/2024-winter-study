n = int(input())
narr = list(map(int, input().split()))

m = int(input())

marr = list(map(int, input().split()))

dict = {}
for i in narr:
    dict[i] = 1
   
for j in marr:
    if j in dict:
        print('1')
    elif not j in dict:
        print('0')