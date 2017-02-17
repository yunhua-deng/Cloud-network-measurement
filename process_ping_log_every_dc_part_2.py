# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 23:19:26 2017

@author: yhdeng
"""

import my_module
import subprocess
import os

source_dc_name_file_name = 'ec2_regions_part_2.txt'

# process ping_to_dc
with open(source_dc_name_file_name, 'r') as source_dc_name_file:
    print('processing ping_to_dc: start...\n')
    subprocess.call(['7z', 'e', 'all.ping_to_dc.zip'])
    for source_dc_name in source_dc_name_file:
        source_dc_name = source_dc_name.strip('\n')
        print('processing source_dc: ' + source_dc_name + '\n')
        my_module.process_pinginfoview_to_dc_log('ping_to_dc.txt', source_dc_name)
        os.remove(source_dc_name + '.' + 'ping_to_dc.txt')
    print('processing ping_to_dc: done\n')
	
# process ping_to_prefix
with open(source_dc_name_file_name, 'r') as source_dc_name_file:
    print('processing ping_to_prefix: start...\n')
    for source_dc_name in source_dc_name_file:
        source_dc_name = source_dc_name.strip('\n')
        print('processing source_dc: ' + source_dc_name + '\n')	
        zip_file_name = source_dc_name + '.ping_to_prefix.zip'
        subprocess.call(['7z', 'e', zip_file_name])
        my_module.process_pinginfoview_to_prefix_log('ping_to_prefix.txt', source_dc_name)
        os.remove(source_dc_name + '.' + 'ping_to_prefix.txt')
    print('processing ping_to_prefix: done\n')