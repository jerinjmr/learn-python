"""
Learning Python3.

Complete Python Developer in 2022: Zero to Mastery
Udemy Online Course

Advanced Python: OOPs
"""

# Excercise 01: Cats
# Given the below class:


# class Cat:
#     """Class of Cat."""

#     species = 'mammal'

#     def __init__(self, name, age):
#         """Initialize attributes."""
#         self.name = name
#         self.age = age

#     def get_name(self):
#         """Return name of the cat."""
#         return self.name

#     def get_age(self):
#         """Return age of cat."""
#         return self.age


# def find_oldest_cat(cat_list):
#     """
#     Find the oldest cat from the list.

#     :parms cat_list: List of objects of Cat
#     :return oldest_cat: Oldest cat's Object
#     """
#     highest_age = 0
#     oldest_cat = None
#     for cat in cat_list:
#         age = cat.get_age()
#         if age > highest_age:
#             oldest_cat = cat  # Object of oldest cat
#             highest_age = age
#     return oldest_cat


# def main():
#     """Program starts here."""
#     # Instantiate the Cat object with 3 cats
#     cat_list = []
#     cat1 = Cat('Tom', 12)
#     cat2 = Cat('Jerry', 10)
#     cat3 = Cat('Pussy', 6)
#     cat_list.extend([cat1, cat2, cat3])
#     old_cat = find_oldest_cat(cat_list)

#     # Modifying object Attribute using an instance
#     # print(cat1.species)
#     # cat1.species = "Cartoon"
#     # print(cat1.species)

#     # Print out: "The oldest cat is x years old."
#     # x will be the oldest cat age.
#     print(
#         f"The oldest cat ({old_cat.get_name()}) " +
#         f"is {old_cat.get_age()} years old."
#     )


# Excercise 03: Pets
class Pets():
    """Class of Pets."""

    animals = []

    def __init__(self, animals):
        """Initialize attributes."""
        self.animals = animals

    def walk(self):
        """Walk all the pets in list."""
        for animal in self.animals:
            print(animal.walk())


class Cat():
    """Class of cats."""

    is_lazy = True

    def __init__(self, name, age):
        """Initialize attributes."""
        self.name = name
        self.age = age

    def walk(self):
        """Walk cat."""
        return f'{self.name} is just walking around'


class Simon(Cat):
    """Class for simon."""

    def sing(self, sounds):
        """Cat sings sound."""
        return f'{sounds}'


class Sally(Cat):
    """Class for sally."""

    def sing(self, sounds):
        """Cat sings sound."""
        return f'{sounds}'

# 1 Add another Cat


class Persian(Cat):
    """Class for persian cat."""

    def sing(self, sounds):
        """Cat sings sound."""
        return f'{sounds}'


def main():
    """Program starts here."""
    # 2 Create a list of all of the pets
    # (create 3 cat instances from the above)
    simon = Simon('tom', 12)
    sally = Sally('jerry', 10)
    persian = Persian('pussy', 8)
    my_cats = []
    my_cats.extend([simon, sally, persian])

    # 3 Instantiate the Pet class with all your cats use variable my_pets
    my_pets = Pets(my_cats)

    # 4 Output all of the cats walking using the my_pets instance
    my_pets.walk()


if __name__ == "__main__":
    main()
