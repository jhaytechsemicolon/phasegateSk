counter = 1
sum = 0
for counter in range(10):
    scores = int(input(f"enter scores{counter + 1}:"))
    if scores < 0 or scores > 100 :
        print("score out of range")

        int(input(f"enter scores{counter + 1}:"))
        scores = 0
    sum += scores





print("sum of even number is: ",sum)

