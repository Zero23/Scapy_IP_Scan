from scapy.all import *

import sys
import random
	

my_ip_list = []


print("Start the process")
for i in range(1,256):
	num = i
	dst_ip = "192.168.1."+ str(num)
	my_ip_list.append(dst_ip)

#print("test: {0}".format(my_ip_list[0]))

total_ip = len(my_ip_list)

my_ip_list_len =len(my_ip_list) +1

print(my_ip_list_len)

for a in range(66,my_ip_list_len):
	
	resp = sr1(IP(dst=my_ip_list[a])/ICMP(),timeout=2,verbose=0,)
	
	
	if resp is None:
		left_ip = total_ip-(a+1)

		print("There still left {0} IP address.".format(left_ip))
		
	else:
		print("The IP: {0} has response".format(my_ip_list[a]))

	#if a > 255:
		#print("the scanning is done")
		#break
