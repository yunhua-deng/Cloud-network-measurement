# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 23:09:19 2016

@author: yhdeng
"""

with open('ec2_terminate-instances.bat', 'w') as out_file:
    with open('ec2_regions.txt', 'r') as region_file:
        region_list = region_file.read().splitlines()
        with open('ec2_instances.txt', 'r') as instance_file:
            instance_list = instance_file.read().splitlines()           
            for i in range(len(region_list)):
                out_line = 'aws ec2 terminate-instances --region ' + region_list[i] + ' --instance-ids ' + instance_list[i]
                print(out_line)
                out_file.write(out_line + '\n')