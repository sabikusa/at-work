#!/usr/bin/env python3

from netmiko import ConnectHandler
from netmiko import redispatch
from getpass import getpass
import logging
import random
from pprint import pprint
import matplotlib.pyplot as plt
from time import sleep
import datetime
import schedule

logging.basicConfig(filename='testing.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

#TS for access source
TSP1 = "10.17.4.25"
TSP2 = "10.17.4.77"
TSB1 = "10.161.18.186"
TSB2 = "10.161.18.187"

#getting the pw
user_name = input("Enter your username to SSH: ")
pwd = getpass()

#paramas of TS
jump1 = {
'device_type': 'cisco_ios',
'host': TSP1,
'username': user_name,
'password': pwd,
}

jump2 = {
'device_type': 'cisco_ios',
'host': TSP2,
'username': user_name,
'password': pwd,
}

jump3 = {
'device_type': 'cisco_ios',
'host': TSB1,
'username': user_name,
'password': pwd,
}

jump4 = {
'device_type': 'cisco_ios',
'host': TSB2,
'username': user_name,
'password': pwd,
}

TSP = [jump1, jump2]
TSB = [jump3, jump4]

#ASA
ASP1 = "10.17.50.13"
ASP2 = "10.17.50.14"
ASB1 = "10.161.50.13"
ASB2 = "10.161.50.14"

ASP = [ASP1, ASP2]
ASB = [ASB1, ASB2]


class Sessions():
    """pull the active sessions hourly basis to report"""
    def __init__(self, ts, asa):
        self.ts = ts
        self.asa = asa

    def jump(self):
        jp = random.choice(self.ts)
        net_connect = ConnectHandler(**jp)
        print("{}".format(net_connect.find_prompt()))

    def vpn(self):
        pass
        net_connect.write_channel(i)
        sleep(1)
        output = net_connect.read_channel()

        if 'ssword' in output:
            net_connect.write_channel(net_connect.password + '\n')
        else:
            print('Skipping this target due to a login failure...\n')
            net_connect.disconnect()

        sleep(1)
        return net_connect.find_prompt()
        pwd = "Emguyth5ag"
        net_connect.secret = pwd
        redispatch(net_connect, device_type='cisco_asa')
        print('Pulling status...')
            
        


    def pull(self):
        pass
        for i in self.asa:
            jump = random.choice(self.ts)
            net_connect = ConnectHandler(**jump)
            return "{}".format(net_connect.find_prompt())
            net_connect.write_channel(i)
            sleep(1)
            output = net_connect.read_channel()

            if 'ssword' in output:
                net_connect.write_channel(net_connect.password + '\n')
            else:
                print('Skipping this target due to a login failure...\n')
                net_connect.disconnect()
                continue

            sleep(1)
            return net_connect.find_prompt()
            
            pwd = "Emguyth5ag"
            net_connect.secret = pwd
            redispatch(net_connect, device_type='cisco_asa')   
            print("Pulling status...")
            net_connect.write_channel("en\n")
            net_connect.write_channel(net_connect.secret + '\n')
            clients = net_connect.send_command("show vpn- | i CLie")
            print(clients)
            net_connect.disconnect()

        
PDC = Sessions(TSP, ASP)
BDC = Sessions(TSB, ASB)

if __name__ == '__main__':
    PDC.jump()



def jumpp():
    pass
    """to enter the TS first for PDC"""
    jump = random.choice(TSP)
    net_connect = ConnectHandler(**jump)
    print("{}".format(net_connect.find_prompt()))
    #net_connect.disconnect()

def jumpb():
    pass
    """to enter the TS first for BDC"""
    jump = random.choice(TSB)
    net_connect = ConnectHandler(**jump)
    print("{}".format(net_connect.find_prompt()))
    #net_connect.disconnect()

