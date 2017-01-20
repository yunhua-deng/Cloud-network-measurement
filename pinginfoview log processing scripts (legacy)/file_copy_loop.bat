for /f %%g in (ec2_regions.txt) do (copy %%g.py D:\Dataset\Latency_long\%%g)
for /f %%g in (ec2_regions.txt) do (copy my_module.py D:\Dataset\Latency_long\%%g)