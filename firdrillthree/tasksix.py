def geteveneindex(values):
    sum = 0
    even_number= []
    for index in range(len(values)):
        if index % 2 == 0:
            even_number.append(values[index])
            sum += values[index]
    return sum


def main():
    numbers = [10,20,30,40,50,60,70,80,90]
    print(geteveneindex(numbers))


if __name__ == '__main__':
    main()