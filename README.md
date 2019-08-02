  
# ftpscan

*Discalimer: This is a proof of concept for another project and not actively maintained. It's stable but not tested*

Scans approximately one /24 subnet (254 addresses) in 2,5sec.
(Has not been optimized, using multiprocessing.dummy in a large envoronment could increase efficiency ten fold...)

Scan provided subnet for ftp-servers (or IoT-Devices with ftp-login) with provided 
username / password.  

*made for the purpose of catching IOT devices with default password on internal networks*

## Install
#### Linux distro with snap support

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-white.svg)](https://snapcraft.io/ftpscan)

```
snap install ftpscan
ftpscan <cidr> <username> <password>
```


#### No snap support / Or on Windows/MAC
```
git clone https://github.com/izznogooood/ftpscan.git
cd ftpscan
python setup.py install
```

What python command you use varies on different operating systems / Python installations.

## Basic Usage
```
ftpscan <cidr> <username> <password>
```

## Help Content:

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

## Prerequisites
*(Snap has no prerequisites)*

What do I need to run this thing?

```
Python 3,5
```

## What is CIDR?

https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing