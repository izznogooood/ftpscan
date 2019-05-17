  
# ftpscan

Scans approximately one /24 subnet (254 addresses) in 2,5sec.

Scan provided subnet for ftp-servers (or IoT-Devices with ftp-login) with provided 
username / password.  

*made for the purpose of catching IOT devices with default password on internal networks*

## Getting Started

```
git clone https://github.com/izznogooood/ftpscan.git
cd ftpscan

python ftpscan.py <cidr> <username> <password>

# or
python setup.py install
ftpscan <cidr> <username> <password>

```

What python command you use varies on different operating systems / Python installations.

### Help Content:

```
positional arguments:
  cidr                  Subnet to scan <192.168.0.0/24>
  user                  <username> to attempt login.
  password              <password> to attempt login.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Filename to store results.
  -v, --verbose         Verbose output
```

### Prerequisites

What do I need to run this thing?

```
Python 3,5
```

### What is CIDR?

https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing