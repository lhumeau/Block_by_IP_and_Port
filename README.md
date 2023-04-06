# Block_by_IP_and_Port

## Prerequisites 

<code>
import os
import re
import sys
import ctypes
import win32com.client
from ipwhois import IPWhois
from scapy.all import sniff
from scapy.layers.inet import IP
import win32api 
import subprocess
import socket
import netifaces
import threading

</code>

## Installation
<code>
pip install requirements.txt
python ipblockandport.py

</code>

## Usage

Block entries ip from ports 3389 and 443 excepting local interfaces is base on a Windows base Enviroment.
in this code i'm filtering ip by whois libraries using scappy for monitoring packets from source and ports.



## License

This project is licensed under the MIT License. See the [LICENSE] file for more details.

## Contact Information

You can reach me by email at <a href="mailto:l.humeau@hynit.com">l.humeau@hynit.com</a>.

## Donations

If you like this project and want to support my work, you can make a donation on my donations page: 
Patreon:
patreon.com/HYNIT
Paypal:
luishumeau90@gmail.com


