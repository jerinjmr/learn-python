"""
Learning Python3.

Complete Python Developer in 2022: Zero to Mastery
Udemy Online Course

Python3 Basics
Cheat Sheet: https://github.com/aneagoie/ztm-python-cheat-sheet
"""


dict_ex = {
    "a": 1,
    "b": 2
}
print(dict_ex)
print(dict_ex.keys())
dict_ex.update({"c": 3, "d": 4})
print(dict_ex)
pop_value = dict_ex.popitem()
print(pop_value)
for (key, value) in dict_ex.items():
    print(key, value)
print(type(dict_ex.keys()))
list_ex = [1, 2, 3, 4]
tuple_ex = (5, 1, 2, 3, 4, 4, 4)
print(tuple_ex[0])
new_tuple = tuple_ex[::-1]
print(new_tuple)


# Excercise 01: First GUI program
# Print Os as empty spaces and 1s as * from picture
# Expected Output: To display a xmas tree
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
EMPTY_PIXEL = " "
FILL_PIXEL = "*"
for row in picture:
    for pixel in row:
        if pixel:
            print(FILL_PIXEL, end="")
        else:
            print(EMPTY_PIXEL, end="")
    print()  # Each row should start from new line


# Excercise 02: Code to find duplicates from given list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate_list = []  # List to store duplicate elements
for element in some_list:
    count = some_list.count(element)
    if count > 1 and element not in duplicate_list:
        duplicate_list.append(element)
# unique_set = set(duplicate_list)  # To eliminate duplicate entries
# duplicate_list = list(unique_set)
print(f'Duplicate\'s list: {duplicate_list}')


# Excercise 03: First Function
# Driver Age Check
def check_driver_age(age=0):
    """Driver age check."""
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congrats on your first year of driving. Enjoy the ride!")


input_age = input("Enter your age: ")
check_driver_age(input_age)


# Excercise 04: Highest Even Number
# Find highest even number from given arguments
def highest_even_number(num_list, *args, **kwargs):
    """Find highest even number."""
    even_list = []
    print(args)
    print(kwargs)
    total_list = num_list + list(args) + list(kwargs.values())
    print(total_list)
    for num in total_list:
        if num % 2 == 0:
            even_list.append(num)
    print(even_list)
    return max(even_list)


print(highest_even_number([7, 6, 3, 4, 10], 1, 2, 8, num1=20, num2=30))
