counter = 1
count = 0
sum = 0
average = 0
for counter in range(10):
    scores = int(input(f"enter scores{counter+1}:"))
    if scores % 2 == 0:
        count +=1
        sum += scores
        average = sum / count

print("sum of even number is: ",sum)
print("average of even scores is: ",average)