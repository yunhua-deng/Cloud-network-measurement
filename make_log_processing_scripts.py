# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 15:39:36 2016

@author: yhdeng
"""

import os, shutil

folder_name = 'pinginfoview log processing scripts'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

shutil.copy('my_module.py', folder_name)

with open('ec2_regions.txt', 'r') as in_file:
    for line in in_file:
        line = line.strip('\n')
        with open(folder_name + '\\' + line + '.py', 'w') as py_file:
            py_file.write('import my_module\n\n')
            py_file.write('source_dc_name = ' + '\'' + line + '\'' + '\n')
            py_file.write('for percentile_rank in [50, 60, 70, 80, 90, 99]:\n')
            py_file.write('\t my_module.process_pinginfoview_to_dc_log(\'ping_to_dc.txt\', source_dc_name, percentile_rank)\n')
            py_file.write('\t my_module.process_pinginfoview_to_prefix_log(\'ping_to_prefix.txt\', source_dc_name, percentile_rank)')