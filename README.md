# basic network scanner 

This is a basic network scanner for scanning a range of IP addresses and getting their MAC addresses.

Supported for Linux and written in Python.

# before using (guide):

you will need to install some packages. 
check [needed.txt](https://github.com/sh-919/basicnetworkscanner/blob/main/needed.txt) for more info. 

if not already installed, download [required.sh](https://github.com/sh-919/basicnetworkscanner/blob/main/required.sh) and follow the directions below to install.


## 1) open shell + login as root
    sudo -s

## 2) give execute permission to the bash file that will install the requirements
    chmod +x /path/to/required.sh

## 3) Navigate to directory required.sh is in and run the script.
    ./required.sh

once you have completed these steps you can download and run [basicnetworkscanner.py](https://github.com/sh-919/basicnetworkscanner/blob/main/basicnetworkscanner.py).



# sample usages: 

> **this command will  scan a range of IP addresses and grab their MAC addresses**

    python3 basicnetworkscanner.py -t <ip address>

> **example**

    python3 basicnetworkscanner.py -t 192.168.38.1/24

> **for help**

    python3 basicnetworkscanner.py --help

