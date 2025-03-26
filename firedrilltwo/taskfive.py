counter = 1
sum = 0
for counter in range(10):
    scores = int(input(f"enter scores{counter+1}:"))
    if scores % 2 == 0:
        sum += scores


print("sum of even number is: ",sum)