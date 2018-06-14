  
# ftpscan

Scan provided subnet for ftp-servers with provided username / password.  
*default password scanning*

## Getting Started

```
git clone https://github.com/izznogooood/ftpscan.git
cd ftpscan
python ftpscan.py <cidr> <username> <password>
```

What python command you use varies on different operating systems.

### Help Content:

```
positional arguments:
  cidr                  Subnet to scan <192.168.0.0/24>
  user                  <username> to attempt login.
  password              <password> to attempt login.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Filename to store results.
```

### Prerequisites

What do I need to run this thing?

```
Python 3,5
```

### What is CIDR?

https://mxtoolbox.com/subnetcalculator.aspx