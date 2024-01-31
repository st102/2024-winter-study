import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n은 끊어진 줄의 개수, m은 브랜드 갯수
pack = [] 
one = [] 

for _ in range(m):
    a, b = map(int, input().split())
    pack.append(a)  
    one.append(b)   

count_pack = n // 6
rest = n % 6

cost_pack = min_pack * count_pack
cost_one = min_one * rest

if rest > 0:
    cost_pack += min_pack

answer = min(cost_pack, cost_one)
print(answer)
