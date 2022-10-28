input_number : int = 1234

number_list = []
def get_list_of_number(number : int):
    if number == 0:
        return
    number_list.append(number % 10)
    get_list_of_number(int(number / 10))
    

def get_difference(number : list):
    min_number = max_number = number[0]
    for num in number[1:]:
        if num < min_number:
            min_number = num
        else:
            if num > max_number:
                max_number = num

    return max_number - min_number

get_list_of_number(input_number)
print(get_difference(number_list))