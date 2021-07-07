from netmiko import ConnectHandler
from getpass import getpass
import time
from netmiko import redispatch
import pprint
from netmiko import SSHDetect, Netmiko
import logging
from datetime import datetime
import random

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


jumps = [jump1,jump2, jump3, jump4]

print('go to the jump_router first...')



#########################


post = open('20210614_2.txt', 'w')
targets = open('20210614_2_acl.txt', 'r')

start_time = datetime.now()
print("time started = ")
post.write("time started = ")
print(start_time)
post.write(str(start_time) + '\n')

acl = "acl.txt"
reseq = ['ip access- reseq NW-Security 10 10']

def configs():
	print("Applying configs...")
	now = datetime.now()
	print(now)
	post.write(str(now) + '\n')
	print("============================Change============================")
	post.write("============================Change============================\n")
	
	net_connect.write_channel('en\n')
	net_connect.write_channel(net_connect.password + '\n')
	
	output = net_connect.send_config_from_file(acl)
	print(output)
	post.write(output + '\n')

	output = net_connect.send_config_set(reseq)
	print(output)
	post.write(output + '\n')
	time.sleep(2)

	print("============================END============================")
	post.write("============================END============================\n")
	now = datetime.now()
	print(now)
	post.write(str(now) + '\n')


for i in targets:
	jump = random.choice(jumps)
	net_connect = ConnectHandler(**jump)
	print ("{}".format(net_connect.find_prompt()))
	net_connect.write_channel(i)
	time.sleep(2)
	output = net_connect.read_channel()
	time.sleep(2)

	if 'ssword' in output:
		net_connect.write_channel(net_connect.password + '\n')
	else:
		print('Skipping this target due to a login failure...\n')
		post.write('Skipping this target due to a login failure...\n')
		net_connect.disconnect()
		continue

	time.sleep(1)
	output += net_connect.read_channel() 
	print(output)
	post.write(output + '\n')
	time.sleep(1)
	net_connect.secret = getpass
	net_connect.write_channel("\n")
	redispatch(net_connect, device_type='cisco_ios')
	print("Pre_change_status...")
	time.sleep(1)
	pre_vty = net_connect.send_command("show ip access- NW-Security")

	now = datetime.now()
	print(now)
	post.write(str(now) + '\n')

	print("---------------------------Pre_ACL status---------------------------")
	post.write("---------------------------Pre_ACL status---------------------------\n")
	pprint.pprint(pre_vty)
	pprint.pprint(pre_vty, stream = post)

	configs()

	time.sleep(2)

	try:
		post_vty = net_connect.send_command("show ip access- NW-Security")
		print("---------------------------Post__ACL status---------------------------")
		post.write("---------------------------Post__ACL status---------------------------\n")
		pprint.pprint(post_vty)
		pprint.pprint(post_vty, stream = post)
		print("--------------------------END of output------------------------")
		post.write("--------------------------END of output------------------------\n")

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

print("""

	        !!!FINISH!!!
       

""")
post.write("""

	        !!!FINISH!!!
       

""")


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