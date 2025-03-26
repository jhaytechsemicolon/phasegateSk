counter = 1
sum = 0
average = 0
for counter in range(10):
    scores = int(input(f"enter scores{counter + 1}:"))
    if 0 < scores <= 100:
        counter += 1
        sum += scores
        average = sum / counter

print("sum of even number is: ", average)

