array = [1, 2, 3, 4, 5]
for i in range(len(array)):
    print(array[i])

print("-------------------")

for i in array:
    print(i)

print("-------------------")

index = 1
while index <= 100:
    print(index)
    index = index + 1

print("-------------------")

for j in range(1,100):
    print(j)

print("-------------------")

for i in range(1, 11, 2):
    if (i % 2) == 0:
        print(i)
        break
else:
    print("not find 复数")

