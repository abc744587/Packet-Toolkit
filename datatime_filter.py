import os
import shutil
import datetime

source_folder = 'C:\\your_folder'  
output_folder = 'C:\\your_folder'  

file_list = os.listdir(source_folder)

for filename in file_list:
    if filename.endswith(".pcapng"):
     
        file_path = os.path.join(source_folder, filename)

        modified_time = os.path.getmtime(file_path)
        modified_date = datetime.datetime.fromtimestamp(modified_time).strftime('%Y%m%d')
        
        date_folder = os.path.join(output_folder, modified_date)
        os.makedirs(date_folder, exist_ok=True)
        
        target_path = os.path.join(date_folder, filename)
        shutil.move(file_path, target_path)

print("File Classification Complete ✅")

# put all pcapng or pcap file in the same folder
# run python3 in the same folder 
# usage: python3 pcap_filter.py
