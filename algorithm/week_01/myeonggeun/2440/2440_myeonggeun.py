input_number = int(input())
temp = input_number+1

for i in range(1,input_number+1) :
    for j in range(1, temp) :
        print("*", end="")
    print("")
    temp-=1