def getoddindex(values):
    even_number= []
    for index,value in enumerate(values):
        if index % 2 != 0:

            even_number.append(value)
    return even_number
def main():
    numbers = [10,20,30,34,45,46,46,45,56]
    print(getoddindex(numbers))


if __name__ == '__main__':
    main()