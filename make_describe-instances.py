# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 23:09:19 2016

@author: yhdeng
"""

with open('ec2_describe-instances.bat', 'w') as out_file:
    with open('ec2_regions.txt', 'r') as region_file:
        region_list = region_file.read().splitlines()
        with open('ec2_amis.txt', 'r') as ami_file:
            ami_list = ami_file.read().splitlines()      
            for i in range(len(region_list)):
                out_line = 'aws ec2 describe-instances --region ' + region_list[i] + ' --filters ' + '"Name=image-id, Values=' + ami_list[i] + '"'
                print(out_line)
                out_file.write(out_line + '\n')                