array = [1,2,3,4,5,6,7,7,4,5,5]

for i in range(len(array) - 1):
    for j in range(i + 1, len(array)):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]

print(array)
for i in range(len(array) - 1, 0, -1):
    if array[i] == array[i - 1]:
        print(array[i])
        break