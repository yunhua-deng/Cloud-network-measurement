# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 23:09:19 2016

@author: yhdeng
"""

with open('ec2_regions.txt', 'r') as region_file:   
    with open('ec2_copy-image.bat', 'w') as out_file:        
        dest_regions = region_file.read().splitlines()
        source_region = 'ap-southeast-1'        
        source_image_id = 'ami-15892176'
        image_name = '"latency_measurement_deng"'
        for region in dest_regions:
            if region != source_region:
                out_line = 'aws ec2 copy-image --source-image-id ' + source_image_id + ' --source-region ' + source_region + ' --region ' + region + ' --name ' + image_name                
                print(out_line)
                out_file.write(out_line + '\n')