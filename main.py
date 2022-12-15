import time
import string
import random
import urllib.request

from trie import TrieTool


def generate_random_list(list_size, str_length=10):
    chars = string.ascii_lowercase + string.digits

    list = ["".join(random.choice(chars) for _ in range(str_length)) for _ in range(list_size)]

    return list


if __name__ == "__main__":
    print("Generating a random list...")

    sample_list = generate_random_list(list_size=10000000)

    # These sample tags exist in the HTML
    sample_list.append("HU6630B")
    sample_list.append("HGRGRJA")

    trie_tool = TrieTool(strings=sample_list)

    # Fetch sample HTML file
    with urllib.request.urlopen("https://dl.dropbox.com/s/4m1tjaz6qcvgqgw/sample-html.html") as file:
        sample_html: str = file.read().decode("utf-8")

        timer_start = time.perf_counter()

        print("\nSearching trie...")

        output = trie_tool.tag_string(sample_html)

        print("\Result:", output)

        timer_end = time.perf_counter()

        print(f"\nSearch time: {timer_end - timer_start} seconds\n")
