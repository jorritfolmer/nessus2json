# Convert Nessus XML to JSON for use in Tableau or Power BI

## Why?

Reasons:
* The Nessus CSV export is lacking a lot of fields, but can be imported into BI tooling
* The Nessus XML export has everything, but cannot be imported into BI tooling.

So this Python script grabs the relevant stuff from the XML export and packs it into a usable JSON for use in Tableau or Power BI

## Installation

1. Clone this repository
1. `python -m venv venv`
1. `source . venv/bin/activate`
1. `pip install -r requirements.txt`

## Usage

```
$ python nessus2json.py
usage: nessus2json.py [-h] filename

positional arguments:
  filename    Filename of Nessus XML export

optional arguments:
  -h, --help  show this help message and exit
```


