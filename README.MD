# Description

Ultra fast Python script to tag strings within a HTML document. Given a list of 10,000,000 strings, find the start and index of all instances of these strings within a 1,000+ LOC HTML in half a second.

### How to run

Create a virtual enviroment.

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

Benchmarks for tag_html on my PC are:

10,000,000 models: 0.561 seconds
1,000,000 models: 0.054 seconds
100,000 models: 0.005 seconds

### Find all

Run main_find_all.py

```sh
python main_find_all.py
```

In main_find_all.py I gave the option of find_all tags within the sample-html.html. If more than one models are within the HTML, it will find the indexes for all of these models.

Find all output: [['HU6630B', {'start_index': 45747, 'end_index': 45754}, {'start_index': 219620, 'end_index': 219627}, {'start_index': 221198, 'end_index': 221205}], ['HGRGRJA', {'start_index': 192442, 'end_index': 192449}, {'start_index': 203373, 'end_index': 203380}, {'start_index': 219792, 'end_index': 219799}]]
