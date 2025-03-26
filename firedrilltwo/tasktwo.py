counter = 1
sum = 0
average = 0
for counter in range(10):
    scores = int(input(f"enter scores{counter+1}:"))
    sum = sum + scores
    average = sum/10

print("average scores is: ",average)