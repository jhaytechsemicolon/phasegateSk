counter = 1
sum = 0
for counter in range(10):
    scores = int(input(f"enter scores{counter+1}:"))
    sum = sum + scores
print("sum of scores is: ",sum)