def getoddindex(values):
    sum = 0
    even_number= []

    for index in range(len(values)):
        if index % 2 != 0:
            even_number.append(values[index])
            sum += values[index]
    return sum
def main():
    numbers = [10,20,30,34,45,46,46,45,56]
    print(getoddindex(numbers))


if __name__ == '__main__':
    main()