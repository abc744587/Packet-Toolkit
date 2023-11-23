import os, subprocess

folder_path = os.getcwd()
file_list = [pcapng for pcapng in os.listdir(folder_path) if pcapng.endswith(".pcapng")] # You can specify it as pcap or pcapng
print(len(file_list), "files are being filtered 🚗...")

for file in file_list:
    input_file_path = os.path.join(folder_path, file)
    output_file_path = os.path.join(folder_path, "New_" + file) # You can specify output file name

    filter_expression = "(((not udp) and not ip.geoip.asnum in {8068,8070,8075,15169})) and (not (ip.src==10.0.0.0/8 and ip.dst==10.0.0.0/8))" # Filter command
    
    cmd = ["tshark", "-r", input_file_path, "-w", output_file_path, "-Y", filter_expression]
    subprocess.run(cmd)
    print(file, "filter completed ✅")

# put all pcapng or pcap file in the same folder
# run python3 in the same folder 
# usage: python3 pcap_filter.py
