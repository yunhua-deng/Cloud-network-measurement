# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 17:57:29 2016

@author: yhdeng
"""

import csv, os

common_prefix_folder = "..\\ping_to_prefix_median\\"
raw_data_folder = ".\\raw\\"

common_prefix_list = []
with open(common_prefix_folder + 'common_prefix_list.csv', 'r') as in_file:
    common_prefix_list = in_file.read().splitlines() # 1D list
    for raw_file_name in os.listdir(raw_data_folder):
        if raw_file_name.endswith('.csv'):
            with open(raw_data_folder + raw_file_name, 'r') as raw_file:            
                list_of_lists = list(csv.reader(raw_file))
                buffer = ''
                for one_list in list_of_lists:
                    if one_list[1] in common_prefix_list:
                        buffer += one_list[1] + ',' + one_list[-1] + '\n'
                with open(raw_file_name, 'w') as filtered_file:
                    filtered_file.write(buffer.rstrip('\n'))
           
in_file_name_50th_list = ['ap-southeast-1.ping_to_prefix_50th.csv', 'us-east-1.ping_to_prefix_50th.csv']
in_file_name_90th_list = ['ap-southeast-1.ping_to_prefix_90th.csv', 'us-east-1.ping_to_prefix_90th.csv']
#out_file_name_list = ['ap-southeast-1.ping_to_prefix_combined_sorted.csv', 'us-east-1.ping_to_prefix_combined_sorted.csv']
#out_file_name_list = ['ap-southeast-1.ping_to_prefix_ratio_sorted.csv', 'us-east-1.ping_to_prefix_ratio_sorted.csv']
#out_file_name_list = ['ap-southeast-1.ping_to_prefix_combined_sorted_filtered.csv', 'us-east-1.ping_to_prefix_combined_sorted_filtered.csv']
out_file_name_list = ['ap-southeast-1.ping_to_prefix_ratio_sorted_filtered.csv', 'us-east-1.ping_to_prefix_ratio_sorted_filtered.csv']
for file_id, sth_not_used in enumerate(out_file_name_list):  
    with open(in_file_name_50th_list[file_id], 'r') as file_50th:
        with open(in_file_name_90th_list[file_id], 'r') as file_90th:
            list_of_lists_50th = list(csv.reader(file_50th))
            list_of_lists_90th = list(csv.reader(file_90th))        
            list_of_lists_combined = []        
            for i, j in enumerate(common_prefix_list):
                #list_of_lists_combined.append([list_of_lists_50th[i][0], int(list_of_lists_50th[i][1]), int(list_of_lists_90th[i][1])])
                #list_of_lists_combined.append([list_of_lists_50th[i][0], (float(list_of_lists_90th[i][1]) / float(list_of_lists_50th[i][1]))])
                if float(list_of_lists_50th[i][1]) > 20: # filter out samples with small value (20 ms)
                    #list_of_lists_combined.append([list_of_lists_50th[i][0], int(list_of_lists_50th[i][1]), int(list_of_lists_90th[i][1])])
                    list_of_lists_combined.append([list_of_lists_50th[i][0], (float(list_of_lists_90th[i][1]) / float(list_of_lists_50th[i][1]))])
            list_of_lists_combined.sort(key=lambda ls: ls[1])
            #buffer = 'prefix,90th-50th\n'
            buffer = '' # without headers
            for one_list in list_of_lists_combined:
                for it in one_list:
                    buffer += str(it) + ','
                buffer = buffer.rstrip(',') # buffer.rstrip(',') doesn't change the buffer but creates a new copy
                buffer += '\n'
            buffer = buffer.rstrip('\n')
            with open(out_file_name_list[file_id], 'w') as out_file:
                out_file.write(buffer.rstrip('\n'))