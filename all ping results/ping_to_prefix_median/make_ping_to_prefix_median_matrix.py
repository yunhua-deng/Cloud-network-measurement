# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 19:33:59 2016

@author: yhdeng
"""
import csv, os, re
from sortedcontainers import SortedSet
import my_module

input_folder = '.\\by_dc\\'

# get the list of common prefixes (without any filtering)
common_elements = []
for file in os.listdir(input_folder):
    if file.endswith('.txt'):
        with open(input_folder + file, 'r') as in_file:               
            list_of_lists = list(csv.reader(in_file))
            list_of_lists = list(map(list, zip(*list_of_lists)))
            if not common_elements:
                common_elements = list_of_lists[1]
            else:
                common_elements = SortedSet(common_elements) & SortedSet(list_of_lists[1])

# create the matrix where the row is indexed by dc (wide matrix)
out_file_name_dc_as_row = 'ping_to_prefix_median_matrix_[dc_as_row].csv'
with open(out_file_name_dc_as_row, 'w') as out_file:
    column_name_line = '' + ','
    for e in common_elements:
        column_name_line += e + ','    
    out_file.write(column_name_line.rstrip(',') + '\n')
    for file in os.listdir(input_folder):
        if file.endswith('.txt'):
            with open(input_folder + file, 'r') as in_file:               
                list_of_lists = list(csv.reader(in_file))
                content = 'ec2-' + list_of_lists[0][0] + ','
                for i, one_list in enumerate(list_of_lists):
                    if one_list[1] in common_elements:                    
                        if i < len(list_of_lists) - 1: 
                            content += one_list[-1] + ','
                        else: 
                            content += one_list[-1] + '\n'
                out_file.write(content)

# create the matrix where the row is indexed by prefix (tall matrix)
out_file_name = 'ping_to_prefix_median_matrix.csv'
my_module.transpose(out_file_name_dc_as_row, out_file_name)

# get the final matrix by removing lines with zeros
in_file_name = out_file_name
out_file_name = in_file_name + '_temp.csv'
with open(in_file_name, 'r') as infile:
    with open(out_file_name, 'w') as outfile:
        for line in infile:
            if None == re.match('.*,0,.*', line):
                outfile.write(line)

os.remove(in_file_name)
os.rename(out_file_name, in_file_name)

# get the list of common prefixes (after filtering)
with open('ping_to_prefix_median_matrix.csv', 'r') as in_file:  
    reader = csv.reader(in_file)
    next(reader, None) # skip the headers
    list_of_lists = list(reader)
    buffer = ''    
    for one_list in list_of_lists:
        buffer += one_list[0] + '\n'
    with open('common_prefix_list.csv', 'w') as out_file:
        out_file.write(buffer.rstrip('\n'))