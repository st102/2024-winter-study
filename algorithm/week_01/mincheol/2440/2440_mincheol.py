a = int(input())

while a > 0:
    for i in range(1, a):
        print("*", end="")
    print("*")
    a -= 1