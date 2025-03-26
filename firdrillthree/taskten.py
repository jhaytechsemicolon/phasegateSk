def geteveneindex(values):
    even_number = []
    for index, value in enumerate(values):
        if index % 2 == 0:
            even_number.append(value)
            maximum = even_number[0]
            if value > maximum:
                maximum = value
    return maximum


def main():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    print(geteveneindex(numbers))


if __name__ == '__main__':
    main()