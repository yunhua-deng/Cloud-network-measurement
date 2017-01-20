# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 19:57:49 2016

@author: yhdeng
"""

import numpy

intended_total_client_count = 1000

with open('ping_to_pl&prefix_median_matrix.csv', 'w') as out_file:    
    with open('ping_to_pl_median_matrix.csv', 'r') as in_file:
        lines = in_file.readlines()        
        for line in lines:
            out_file.write(line)
        intended_total_client_count -= (len(lines) - 1)
    out_file.write('\n')
    with open('ping_to_prefix_median_matrix.csv', 'r') as in_file:
        next(in_file)
        lines = in_file.readlines()
        lines = numpy.random.choice(lines, intended_total_client_count).tolist()
        for line in lines:
            out_file.write(line)