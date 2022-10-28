natural_number : int = 123

def print_number(number : int):
    if (number == 0):
        return
    print(number % 10, end=' ')
    print_number(int(number / 10))

print_number(natural_number)