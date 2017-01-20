# -*- coding: utf-8 -*-
"""
this file contains my functions
@author: yhdeng
"""
import socket 
import csv
import statistics as stat
import numpy
from collections import defaultdict
from sortedcontainers import SortedDict

def process_pinginfoview_to_dc_log(log_filename, source_dc_name):
    with open(log_filename, 'r') as in_file:                
        all_pings = defaultdict(list)     
        for row in csv.reader(in_file): # row will be a list, therefore, no need to use list(csv.reader(in_file)) which consumes huge memory                       
            if row[-1] == 'Succeeded':  
                key = row[1].split('.')[1]
                if key == 'compute-1': 
                    key = 'us-east-1'
                all_pings[key].append(int(row[-3]))
        all_pings = SortedDict(all_pings)
        
        # the cleaned up file
        with open(source_dc_name + '.' + log_filename.rsplit('.')[0] + '.csv', 'w') as out_file:            
            for key, value in all_pings.items(): 
                out_file.write(source_dc_name + ',' + key)
                for it in value:
                    out_file.write(',' + str(it))
                out_file.write('\n')
                
        # the average file
        with open(source_dc_name + '.' + log_filename.rsplit('.')[0] + '_' + 'avg' + '.csv', 'w') as out_file:
            for key, value in all_pings.items():
                out_file.write(source_dc_name + ',' + key + ',' + str(int(stat.mean(value))) + '\n')
        
        # the p50 and p90 files
        for percentile_rank in { 50, 90 }:
            with open(source_dc_name + '.' + log_filename.rsplit('.')[0] + '_' + 'p' + str(int(percentile_rank)) + '.csv', 'w') as out_file:
                for key, value in all_pings.items():
                    out_file.write(source_dc_name + ',' + key + ',' + str(int(numpy.percentile(value, percentile_rank))) + '\n')          

def process_pinginfoview_to_prefix_log(log_filename, source_dc_name):
    with open(log_filename, 'r') as in_file:
        all_pings = defaultdict(list)        
        for row in csv.reader(in_file): # row will be a list, therefore, no need to use list(csv.reader(in_file)) which consumes huge memory
            if row[-1] == 'Succeeded':              
                all_pings[row[2]].append(int(row[-3])) # row[2] is the ip address, row[-3] is the ping
        all_pings = SortedDict(all_pings)          
        
        # the cleaned up file
        with open(source_dc_name + '.' + log_filename.rsplit('.')[0] + '.csv', 'w') as out_file:            
            for key, value in all_pings.items(): 
                out_file.write(source_dc_name + ',' + key)
                for it in value:
                    out_file.write(',' + str(it))
                out_file.write('\n')
                
        # the average file
        with open(source_dc_name + '.' + log_filename.rsplit('.')[0] + '_' + 'avg' + '.csv', 'w') as out_file:
            for key, value in all_pings.items():
                out_file.write(source_dc_name + ',' + key + ',' + str(int(stat.mean(value))) + '\n')
        
        # the p50 and p90 files
        for percentile_rank in { 50, 90 }:
            with open(source_dc_name + '.' + log_filename.rsplit('.')[0] + '_' + 'p' + str(int(percentile_rank)) + '.csv', 'w') as out_file:
                for key, value in all_pings.items():
                    out_file.write(source_dc_name + ',' + key + ',' + str(int(numpy.percentile(value, percentile_rank))) + '\n')
                    
def transpose(i, o=None, d=','):
    f = open(i, 'r')
    file_contents = f.readlines()
    f.close()
    out_data = map((lambda x: d.join([y for y in x])),
                   zip(* [x.strip().split(d) for x in file_contents if x]))
    if o:
        f = open(o, 'w')
        # here we map a lambda, that joins the first element of a column, the 
        # header, to the rest of the members joined by a comma and a space. 
        # the lambda is mapped against a zipped comprehension on the 
        # original lines of the csv file. This groups members vertically
        # down the columns into rows. 
        f.write('\n'.join (out_data))
        f.close()
    return out_data

def resolve_hostname(hostname):
    try:
        ip = socket.gethostbyname(hostname) 
        return ip
    except socket.error:
        return '0.0.0.0'