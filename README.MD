
# Python Trie Traversal

Python implementation of trie traversal. Search a string (e.g. HTML file) containing millions of characters for matches within a trie tree containing millions of words in less than 0.5 seconds.

### Description

Generates a random list of strings that are added to the trie. Adds two sample strings that are contained in the sample HTML. Fetches sample HTML from Dropbox. Searches HTML using trie data and outputs the result. The result contains the match with its start/end index within the HTML.

**Sample output:**

```console

Generating a random list...

Searching trie...

Result: [{'result': 'HU6630B', 'start_index': 750603, 'end_index': 750610}]

Search time: 0.11101756499920157 seconds

```

### How to run

Create a virtual environment.

```sh

python -m venv env

```

Install dependencies found in `requirements.txt`.

```sh

pip install -r requirements.txt

```

Run main.py

```sh

python main.py

```

### Benchmark on my PC:

**10,000,000 strings, 100,000 sample HTML: 0.561 seconds**