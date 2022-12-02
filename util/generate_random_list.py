import random
import string


def generate_random_list(size: int, string_length=10):
    """
    Generate list of given size containing random strings of given length

    Returns:
        `random_list`: List containing random strings
    """
    chars = string.ascii_lowercase + string.digits

    random_list = [
        "".join(random.choice(chars) for _ in range(string_length))
        for _ in range(size)
    ]

    return random_list
