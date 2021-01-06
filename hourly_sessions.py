#!/usr/bin/env python3

from netmiko import ConnectHandler
from netmiko import redispatch
from getpass import getpass
import random
from pprint import pprint
import matplotlib.pyplot as plt
from time import sleep

#TS for access source
TSP1 = ("10.17.4.25")
TSP2 = ("10.17.4.77")
TSB1 = ("10.161.18.186")
TSB2 = ("10.161.18.187")

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

def jumpp():
    """to enter the TS first for PDC"""
    jump = random.choice(TSP)
    net_connect = ConnectHandler(**jump)
    print("{}".format(net_connect.find_prompt()))
    net_connect.disconnect()

def jumpb():
    """to enter the TS first for BDC"""
    jump = random.choice(TSB)
    net_connect = ConnectHandler(**jump)
    print("{}".format(net_connect.find_prompt()))
    net_connect.disconnect()

jumpp()
jumpb()