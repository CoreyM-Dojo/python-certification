def countdown(n):
    list = []
    for i in range(n, 0, -1):
        list.append(i)
    return list


def print_and_return(args):
    print(args[0])
    return args[1]


def first_plus_length(list):
    return list[0] + len(list)


def values_greater_than_second(list):
    new_list = []
    if len(list) < 2:
        return False

    for num in list:
        if num > list[1]:
            new_list.append(num)

    return new_list


def this_length_that_value(size, value):
    result = []

    for i in range(size):
        result.append(value)

    return result


print(countdown(100))
print(print_and_return([10, 2]))
print(first_plus_length([1, 2, 3, 4, 5]))
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))
print(this_length_that_value(4, 7))
