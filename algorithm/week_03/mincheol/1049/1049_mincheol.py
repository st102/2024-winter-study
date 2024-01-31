n, m = map(int, input().split())

min_pack = 1000
min_one = 1000
for i in range(m):
    pack, one = map(int, input().split())
    if pack < min_pack:
        min_pack = pack
    if one < min_one:
        min_one = one
        
min_price = min_one * n
price = (n//6 + 1) * min_pack
if price < min_price:
    min_price = price

price = (n//6) * min_pack + (n%6) * min_one
if price < min_price:
    min_price = price
    
print(min_price)