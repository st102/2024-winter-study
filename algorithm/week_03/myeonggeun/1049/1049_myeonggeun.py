purchase, numbers=list(map(int,input().split()))

packages=[]
eaches=[]

for _ in range(numbers):
    package, each=list(map(int, input().split()))
    packages.append(package)
    eaches.append(each)

min_package=min(packages)
min_each=min(eaches)

if min_package/6 > min_each:
    print(min_each*purchase)
else:
    package_purchase, leave=divmod(purchase,6)
    if min_package < leave*min_each:
        print(min_package*(package_purchase+1))
    else:
        print(min_package*package_purchase + min_each*leave)