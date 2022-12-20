x = [[5, 2, 3], [10, 8, 9]]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
]
sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}
z = [{"x": 10, "y": 20}]

# Update values in a dictionary
x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]["y"] = 30


def iterate_dictionary(list):
    for dict in list:
        entry = ""
        count = 0
        for key, value in dict.items():
            count += 1
            if count < len(dict.keys()):
                entry += f"{key} - {value}, "
            else:
                entry += f"{key} - {value}"
        print(entry)


def iterate_dictionary_2(key_name, list):
    for dict in list:
        print(dict[key_name])


def print_info(some_dict):
    for key, list in some_dict.items():
        print(f"{len(list)} {key}")
        for item in list:
            print(item)


print(x)
print(students)
print(sports_directory)
print(z)
iterate_dictionary(students)
iterate_dictionary_2("first_name", students)
iterate_dictionary_2("last_name", students)
print_info(sports_directory)
