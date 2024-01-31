a, b = map(int, input().split())

string = []
temp = []
count = 0

for i in range (b):
    string.extend(list(map(int, input().split())))

while True:
    temp = list(string)
    if a < 6:
        for i in range(1, len(string), 2):
            string[i] *= a
        count += min(string)
        print(count)
        break

    else:
        for i in range(1, len(temp), 2):
            temp[i] *= 6
        count += min(temp)
        a -= 6