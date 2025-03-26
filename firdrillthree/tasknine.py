def getoddindex(values):
    even_number= []
    for index,value in enumerate(values):
        if index % 2 != 0:

            even_number.append(value)
            minimum = even_number[0]
            if value < minimum:
                minimum = value
    return minimum
def main():
    numbers = [10,20,30,34,45,46,46,45,56]
    print(getoddindex(numbers))


if __name__ == '__main__':
    main()