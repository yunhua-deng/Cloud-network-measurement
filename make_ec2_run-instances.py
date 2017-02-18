# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 23:09:19 2016

@author: yhdeng
"""

with open('ec2_run-instances.bat', 'w') as out_file:
    with open('ec2_regions.txt', 'r') as region_file:
        region_list = region_file.read().splitlines()
        with open('ec2_amis.txt', 'r') as ami_file:
            ami_list = ami_file.read().splitlines()      
            with open('ec2_keys.txt', 'r') as key_file:
                key_list = key_file.read().splitlines()
                for i in range(len(region_list)):
                    out_line = 'aws ec2 run-instances --region ' + region_list[i] + ' --image-id ' + ami_list[i] + ' --count 1 --instance-type c4.large --key-name ' + key_list[i] + ' --security-groups allow_all'
                    print(out_line)
                    out_file.write(out_line + '\n')