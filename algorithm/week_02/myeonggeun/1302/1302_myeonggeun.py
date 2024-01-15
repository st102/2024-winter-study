number = int(input())
books = {}

for x in range(number):
    name = input()
    if name not in books:
        books[name]=1
    else:
        books[name]+=1

max_sell = max(books.values())
max_books=[]

for key, value in books.items():
    if value==max_sell:
        max_books.append(key)

max_books.sort()
print(max_books[0])