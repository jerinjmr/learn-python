"""
Learning Python3.

Complete Python Developer in 2022: Zero to Mastery
Udemy Online Course

Advanced Python: Functional Programming
"""

# Excercise 01: Demonstrate map(), filter(), zip() and reduce()
# from functools import reduce


# def pass_filter(score):
#     """Filter the scores that pass over 50%."""
#     return score > 50


# def total(sum_items, item):
#     """Sum of elements in a list."""
#     return sum_items + item


# # 1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']
# print(list(map(str.upper, my_pets)))


# # 2 Zip the 2 lists into a list of tuples,
# # but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5, 4, 3, 2, 1]
# # my_numbers.sort()
# print(list(zip(my_strings, sorted(my_numbers))))

# # 3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]
# print(list(filter(pass_filter, scores)))


# # 4 Combine all of the numbers that are in a list on this file using reduce
# # i.e my_numbers and scores. What is the total?
# print(reduce(total, my_numbers + scores, 0))


# Excercise 02: Demo of Lambda funtions

# # Print sqaure of each item in list
# my_list = [5, 4, 3]
# print(list(map(lambda item: item**2, my_list)))

# # Sort the list as per second element in tuple using lambda
# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# a.sort(key=lambda x: x[1])
# print(a)


# # Excercise 03: Find duplicate from list using comprehensions
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicate_list = list(
#     {item for item in some_list if some_list.count(item) > 1})
# print(duplicate_list)

# Excercise 04: Demo decorator
# Create an @authenticated decorator that only allows the function to run if
# user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(func):
    """Authenticaton function."""
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return func(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    """Send messages from user."""
    print(f"{user['name']}: message has been sent")


message_friends(user1)
