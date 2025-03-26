sum = 0
for count in range(4,11,4):
    multiple = 1

    for counter in range(5):
        multiple = multiple * count
        sum = sum + multiple
print(sum,end=" ")