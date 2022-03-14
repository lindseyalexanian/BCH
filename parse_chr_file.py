#!/usr/bin/env python3
# bch_assignment.py

"""BCH assignment by Lindsey. This script parses the initial file. The statistical analysis is done 
in another file (an Rscript file)"""


import sys
import os
import re

def _get_headers(list_of_required_headers):
    """Get header names"""

    headers = list_of_required_headers

    #open selected text file
    with open('RF204_Alt055.tlx', 'r') as infile:
        first_line = infile.readline()
        first_line_list = first_line.split('\t')
        first_line_list_format = [i.rstrip(os.linesep) for i in first_line_list]

        indices = []
        for item in first_line_list_format:
            if item in headers:

                header_index = first_line_list_format.index(item)
                indices.append(header_index)

            else:
                pass
        return indices


def get_columns(list_of_required_headers):
    """Get columns and print the required data to a text file"""

    data_reprint = open("analysis_dataRF.txt", 'w')
    data_reprint.write("\t".join(list_of_required_headers) + '\n')
    data_from_column = []
    headers = _get_headers(list_of_required_headers)
    # checks every line in the text file
    with open('RF204_Alt055.tlx', 'r') as infile:
        # skip header line
        next(infile)
        for line in infile:
            # splits data by tab
            numbers = line.split('\t')
            data_from_column = []
            for i in headers:
                column_numbers = (numbers[i])
                data_from_column.append(column_numbers)

            data_reprint.write("\t".join(data_from_column) + '\n')

    data_reprint.close()

# call the function
get_columns(['Rname', 'Junction'])