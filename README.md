# Block_by_IP_and_Port

Tool to block IP addresses on ports 3389 and 443 in a Windows environment.

## Prerequisites

* ipwhois
* scapy
* win32com
* netifaces

## Installation

<code>
  pip install requirements.txt
  python ipblockandport.py
 </code>
 
 
## Usage

Block entries ip from ports 3389 and 443 excepting local interfaces is base on a Windows base Enviroment. in this code i'm filtering ip by whois libraries using scappy for monitoring packets from source and ports.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact Information

You can reach me by email at l.humeau@hynit.com.

## Donations

If you like this project and want to support my work, you can make a donation on my donations page:

<a href="https://www.patreon.com/HYNIT" target="_blank"><img src="https://img.shields.io/badge/Support%20me%20on-Patreon-orange.svg?logo=patreon&style=for-the-badge" alt="Support me on Patreon"></a>

<a href="https://www.paypal.com/paypalme/luishumeau90" target="_blank"><img src="https://img.shields.io/badge/Donate%20with-PayPal-blue.svg?logo=paypal&style=for-the-badge" alt="Donate with PayPal"></a>
