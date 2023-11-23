# Packet-Toolkit

Packet-Toolkit contains tools for processing packet files, which can help you analyze packet files more efficiently.

## Installation

Packet-Toolkit operates based on tshark and is written in Python3, so tshark and python3 must be installed.

You can install [Wireshark](https://www.wireshark.org/download.html) directly, and tshark will be downloaded automatically. Next, please add the path of tshark to the environment variable, otherwise ".py" will not be able to read tshark.

## Introduction

```pcap_filter.py```: Used to filter packet content. If you have many packet files and want to exclude certain content or filter out specific content for analysis, you can use it.

```datatime_filter.py```: Used for categorizing packet dates. If you have many packet files, you can use it to automatically categorize packet files by different dates.

```pcap_to_pcapng.py```: Used for format conversion between pcap and pcapng. Sometimes you may need to convert the format of packet files, for example, when using NetworkMiner, you may need to convert a pcapng file to pcap.
