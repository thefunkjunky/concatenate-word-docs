# concatenate-word-docs
Concatenates word docs into a single file

## Installation
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Usage
```
$ source venv/bin/activate

$ python3 concatenate-word.py --help
usage: concatenate-word.py [-h] [-f FILES [FILES ...]] output_file

Concatenate word docs.

positional arguments:
  output_file           Concatenated output file.

optional arguments:
  -h, --help            show this help message and exit
  -f FILES [FILES ...], --files FILES [FILES ...]
                        Files to concatenate.

$ deactivate
```

Example:
```
python concatenate-word.py output.docx -f test1.docx test2.docx
```
