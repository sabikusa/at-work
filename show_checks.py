from netmiko import ConnectHandler
from getpass import getpass
import time
from netmiko import redispatch
import pprint
from netmiko import SSHDetect, Netmiko
import logging
from datetime import datetime
import csv
import random
import sys

logging.basicConfig(filename='testing.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")



IP = ("10.17.4.25")
IP2 = ("10.17.4.77")
IP3 = ("10.161.18.186")
IP4 = ("10.161.18.187")
IP5 = ("10.17.4.79")
IP6 = ("10.17.4.80")

user_name = input("Enter your username to SSH: ")
pwd = getpass()

jump1 = {
'device_type': 'cisco_ios',
'host': IP,
'username': user_name,
'password': pwd,
}

jump2 = {
'device_type': 'cisco_ios',
'host': IP2,
'username': user_name,
'password': pwd,
}

jump3 = {
'device_type': 'cisco_ios',
'host': IP3,
'username': user_name,
'password': pwd,
}

jump4 = {
'device_type': 'cisco_ios',
'host': IP4,
'username': user_name,
'password': pwd,
}

jump5 = {
'device_type': 'cisco_ios',
'host': IP5,
'username': user_name,
'password': pwd,
}

jump6 = {
'device_type': 'cisco_ios',
'host': IP6,
'username': user_name,
'password': pwd,
}


jumps = [jump4,jump3]

print('go to the jump_router first...')



#########################

post = open('BR-SAKI-BB-1.txt', 'w')
targets = open('20210603_acl2.txt')
devices = ['ssh 10.152.241.85\n']


start_time = datetime.now()
print("time started = ")
post.write("time started = ")
print(start_time)
post.write(str(start_time) + '\n')


for i in devices:
	jump = random.choice(jumps)
	net_connect = ConnectHandler(**jump)
	print ("{}".format(net_connect.find_prompt()))
	net_connect.write_channel(i)
	time.sleep(2)
	output = net_connect.read_channel()
	time.sleep(1)

	if 'ssword' in output: 
		net_connect.write_channel(net_connect.password + '\n')
	else:
		print('Skipping this target due to a login failure...\n')
		post.write('Skipping this target due to a login failure...\n')
		net_connect.disconnect()
		continue

	time.sleep(1)
	#output += net_connect.read_channel()
	print(net_connect.find_prompt())
	post.write(net_connect.find_prompt() + '\n')


	net_connect.secret = pwd
	redispatch(net_connect, device_type='cisco_ios')   
	print("Pulling status...")
	try:
		net_connect.write_channel("en\n")
		net_connect.write_channel(net_connect.password + '\n')
		time.sleep(1)
		pre_lldp = net_connect.send_command("show run | i inter| auto")
		pre_vty = net_connect.send_command("show run | s RADIUS")
		#pre_vty2 = net_connect.send_command("show vl | s 800")
		now = datetime.now()
		print(now)
		post.write(str(now) + '\n')
	
		print("-" * 25 + "Authentication" + "-" * 25)
		post.write("-" * 25 + "Authentication" + "-" * 25 + "\n")
		pprint.pprint(pre_lldp)
		pprint.pprint(pre_lldp, stream =  post)
		#pprint.pprint(pre_vty2)
		#pprint.pprint(pre_vty2, stream =  post)
		print("-" * 25 + "RADIUS" + "-" * 25)
		post.write("-" * 25 + "RADIUS" + "-" * 25 + "\n")
		pprint.pprint(pre_vty)
		pprint.pprint(pre_vty, stream = post)
		#print("-" * 25 + "bpdu_guard" + "-" * 25)
		#post.write("-" * 25 + "bpdu_guard" + "-" * 25 + "\n")
		#pprint.pprint(pre_vty2)
		#pprint.pprint(pre_vty2, stream = post)

		print('Returning to the jump_router...')
		post.write('Returning to the jump_router...\n\n')
		net_connect.write_channel("^C\n")
		net_connect.write_channel("exit\n")
		net_connect.disconnect()
	except OSError:
		print("error occurred and skipping this device...")
		post.write("error occurred and skipping this device...\n")
		net_connect.disconnect()
		continue
else:
	net_connect.disconnect()

targets.close()

end_time = datetime.now()
elapse_time = start_time - end_time

print("time ended =")
post.write("time ended = ")
print(end_time)
post.write(str(end_time) + '\n')
print("time elapsed =")
post.write("time elapsed = ")
print(end_time - start_time)
post.write(str(end_time - start_time) + '\n')

post.close()