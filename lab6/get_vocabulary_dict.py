#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
from pathlib import Path

from typing import Dict


def get_vocabulary_dict() -> Dict[int, str]:
    """Read the fixed vocabulary list from the datafile and return.

    :return: a dictionary of words mapped to their indexes
    """

    # Parse data from the 'data/vocab.txt' file.
    # - The file is saved in tab-separated values (TSV) format.
    # - Each line contains a word's ID and the word itself.
    # The output dictionary should map word's ID on the word itself, e.g.:
    #   {1: 'aa', 2: 'ab', ...}'
    data_folder = Path("c:/Users/tomis/Desktop/um/svm_spam_skeleton/svm_spam__skeleton/")
    file_to_open = data_folder / "data/vocab.txt"
    tsv_file =  open(file_to_open)
    read_tsv = csv.reader(tsv_file, delimiter='\n')

    vocabulary_dict = {}
    for line in read_tsv:
        line_str = ''.join(line)
        splitted_line = line_str.split('\t')
        vocabulary_dict[int(splitted_line[0])] = splitted_line[1]
    return vocabulary_dict
