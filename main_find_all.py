import codecs
from time import perf_counter
from classes.feature import Feature
from util.generate_random_list import generate_random_list


def main():
    # Generate a random list of strings
    list_size = 10000

    print(f"\nGenerating random list of size {list_size}...")

    sample_list = generate_random_list(size=list_size)

    # Add HU6630B and HGRGRJA model to end of list
    sample_list.append("HU6630B")
    sample_list.append("HGRGRJA")

    # Sample HTML
    html = codecs.open("sample-html.html", "r")
    html_str: str = html.read()

    feature_tagging = Feature(sample_list)

    timer_start = perf_counter()

    output = feature_tagging.tag_html(html_str, find_all=True)

    print(f"\nFind all output: {output}")

    timer_end = perf_counter()

    print(f"\ntag_html performance time: {timer_end - timer_start} seconds\n")


main()
