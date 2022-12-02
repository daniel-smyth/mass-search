from time import perf_counter
from classes.feature import Feature
from util.generate_random_list import generate_random_list


def main():
    # Generate a random list of strings
    list_size = 10000

    print(f"\nGenerating random list of size {list_size}...")

    # Longest part of function is generating the list
    sample_list = generate_random_list(size=list_size)

    # Add HU6630B model to end of list
    sample_list.append("HU6630B")

    feature_tagging = Feature(sample_list)

    timer_start = perf_counter()

    # Tag HTML
    result = feature_tagging.tag_html("<html> <body> ABC HU6630B XYZ </body><html>")

    print(f"\nOutput: {result}")

    timer_end = perf_counter()

    print(f"\ntag_html performance time: {timer_end - timer_start} seconds\n")


if __name__ == "__main__":
    main()
