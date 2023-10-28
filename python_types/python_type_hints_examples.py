from typing import Optional

def get_full_name(first_name: str, last_name: str):
    """
    Returns the full name of a person given their first and last name.

    Parameters:
    -----------
    first_name : str
        The person's first name.
    last_name : str
        The person's last name.

    Returns:
    --------
    str
        The person's full name.
    """
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))


def get_name_with_age(name: str, age: int):
    """
    Returns a string that includes a person's name and age.

    Parameters:
    -----------
    name : str
        The person's name.
    age : int
        The person's age.

    Returns:
    --------
    str
        A string that includes the person's name and age.
    """
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


print(get_name_with_age("Hamed", 33))


def process_items(items: list[str]):
    """
    Prints each item in a list.

    Parameters:
    -----------
    items : list[str]
        A list of strings.
    """
    for item in items:
        print(item)


def process_items_2(items_t: tuple[int, int, str], items_s: set[bytes]):
    """
    Returns a tuple and a set.

    Parameters:
    -----------
    items_t : tuple[int, int, str]
        A tuple of integers and a string.
    items_s : set[bytes]
        A set of bytes.

    Returns:
    --------
    Tuple[tuple[int, int, str], set[bytes]]
        A tuple that includes the input tuple and set.
    """
    return items_t, items_s


def process_items_3(prices: dict[str, float]):
    """
    Prints each item name and price in a dictionary.

    Parameters:
    -----------
    prices : dict[str, float]
        A dictionary of item names and prices.
    """
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


def process_item_4(item: int | str):
    """
    Prints an item.

    Parameters:
    -----------
    item : int | str
        An integer or a string.
    """
    print(item)


def say_hi(name: Optional[str] = None):
    """
    Prints a greeting.

    Parameters:
    -----------
    name : str, optional
        The person's name. Defaults to None.
    """
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


class Person:
    def __init__(self, name: str):
        """
        Initializes a Person object.

        Parameters:
        -----------
        name : str
            The person's name.
        """
        self.name = name


def get_person_name(one_person: Person):
    """
    Returns a person's name.

    Parameters:
    -----------
    one_person : Person
        A Person object.

    Returns:
    --------
    str
        The person's name.
    """
    return one_person.name
