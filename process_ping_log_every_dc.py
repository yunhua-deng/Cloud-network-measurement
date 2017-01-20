# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 23:19:26 2017

@author: yhdeng
"""

import my_module

with open('ec2_regions.txt', 'r') as source_dc_name_file:
    print('data processing: start...\n')
    for source_dc_name in source_dc_name_file:
        source_dc_name = source_dc_name.strip('\n')
        print('processing source_dc: ' + source_dc_name + '\n')
        my_module.process_pinginfoview_to_dc_log(log_filename='ping_to_dc.txt', source_dc_name)
        my_module.process_pinginfoview_to_prefix_log(log_filename='ping_to_prefix.txt', source_dc_name)
    print('data processing: complete...\n')