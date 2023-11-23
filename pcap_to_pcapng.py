import os, subprocess

# Build Path
source_folder = os.getcwd()
target_folder = os.path.join(os.getcwd(), "Convert_pcapng_to_pcap")

print("======= Convert pcap to pcapng 🚗... =======")

# Get the pcap/pcapng files under the path.
pcap_files = [file for file in os.listdir(source_folder) if file.endswith(".pcap")]

for file in pcap_files:
    pcapng_path = os.path.join(target_folder, f"{os.path.splitext(file)[0]}.pcapng")

    # Determine whether the target_folder exists, if not, create it.
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    cmd = ["tshark", "-F", "pcapng", "-r", os.path.join(source_folder, file), "-w", pcapng_path]
    subprocess.run(cmd)
 
print("======= Done ✅=======")

# put all pcapng or pcap file in the same folder
# run python3 in the same folder 
# usage: python3 pcap_to_pcapng.py