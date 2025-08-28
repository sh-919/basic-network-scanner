import scapy.all as scapy
import optparse
from termcolor import colored

def get_arguments():
    parse = optparse.OptionParser()
    parse.add_option("-t", "--target", dest = "ip", help = "An example of an IP Address range => 192.168.2.133/24.")
    someoptions, arguments = parse.parse_args()

    if not someoptions.ip:
        parse.error("[-] Please enter an IP Address, use --help for additional info")
    else:
        return someoptions

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request   
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)
    client_list = []
    for element in answered_list:
        client_dict = {"ip" : element[1].psrc, "mac" : element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(result_list):
    print("IP Address\t\tMAC Address\n---------------------------------------")
    for result in result_list:
        print(result["ip"], "\t    ",result["mac"])

def about():
	print(colored("# Creator     :", "blue") + "Sara Husain")
	print(colored("# Linkedin    :", "red") + " https://www.linkedin.com/in/sara-husain")
	print(colored("# Github      :", "green") + " https://github.com/sh-919")
	print(colored("...........................................................................................", "blue"))

about()
someoptions = get_arguments()
scan_output = scan(someoptions.ip)
print_result(scan_output)
