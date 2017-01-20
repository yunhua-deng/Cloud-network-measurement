import my_module

source_dc_name = 'ap-southeast-2'
for percentile_rank in [50, 60, 70, 80, 90, 99]:
	 my_module.process_pinginfoview_to_dc_log('ping_to_dc.txt', source_dc_name, percentile_rank)
	 my_module.process_pinginfoview_to_prefix_log('ping_to_prefix.txt', source_dc_name, percentile_rank)