# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 19:31:43 2016

@author: yhdeng
"""
import csv, os
from sortedcontainers import SortedSet

data_folder = 'C:\\Dataset_Latency_EC2\\cooked\\'

for metric_name in {'ping_to_dc_avg', 'ping_to_dc_p50', 'ping_to_dc_p90'}:   
    #find comment_elements
    common_elements = []
    for file in os.listdir(data_folder):
        if file.endswith(metric_name + '.csv'):
            with open(data_folder + file, 'r') as in_file:
                list_of_lists = list(csv.reader(in_file))
                list_of_lists = list(map(list, zip(*list_of_lists)))
                if not common_elements:
                    common_elements = list_of_lists[1]
                else:
                    common_elements = SortedSet(common_elements) & SortedSet(list_of_lists[1])

    #make matrix
    with open(metric_name + '_matrix' + '_month.csv', 'w') as out_file:
        column_name_line = '' + ','
        for e in common_elements:
            column_name_line += 'ec2-' + e + ','
        out_file.write(column_name_line.rstrip(',') + '\n')
        for file in os.listdir(data_folder):
            if file.endswith(metric_name + '.csv'):
                with open(data_folder + file, 'r') as in_file:               
                    list_of_lists = list(csv.reader(in_file))
                    content = 'ec2-' + list_of_lists[0][0] + ','
                    for i, one_list in enumerate(list_of_lists):
                        if one_list[1] in common_elements:                    
                            if i < len(list_of_lists) - 1: 
                                content += one_list[-1] + ','
                            else: 
                                content += one_list[-1] + '\n'
                    out_file.write(content)