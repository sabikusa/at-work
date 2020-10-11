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


jumps = [jump1,jump3]

print('go to the jump_router first...')



#########################

pdc_devices = [
 'ssh 10.17.4.61\n', 'ssh 10.17.4.62\n', 'ssh 10.17.4.63\n', 'ssh 10.17.4.64\n', 
'ssh 10.160.255.9\n', 'ssh 10.160.255.10\n', 'ssh 10.160.255.11\n', 'ssh 10.160.255.12\n',
 'ssh 10.160.255.8\n', 'ssh 10.17.13.46\n', 'ssh 10.160.255.7\n', 'ssh 10.160.255.22\n', 
'ssh 10.160.255.6\n', 'ssh 10.160.255.24\n', 'ssh 10.17.4.42\n', 'ssh 10.17.4.49\n',
 'ssh 10.17.4.92\n', 'ssh 10.160.253.102\n', 'ssh 10.160.255.5\n', 'ssh 10.17.4.75\n', 
'ssh 10.17.4.76\n', 'ssh 10.160.250.5\n', 'ssh 10.160.250.6\n', 'ssh 10.17.4.10\n', 
'ssh 10.17.4.11\n', 'ssh 10.17.145.20\n', 'ssh 10.17.4.72\n', 'ssh 10.17.4.55\n', 
'ssh 10.17.4.51\n', 'ssh 10.17.6.166\n', 'ssh 10.17.6.70\n', 'ssh 10.17.13.123\n', 
'ssh 10.17.13.104\n', 'ssh 10.17.13.103\n', 'ssh 10.160.214.102\n', 'ssh 10.160.252.59\n', 
'ssh 10.160.252.60\n', 'ssh 10.17.4.4\n', 'ssh 10.17.4.5\n', 'ssh 10.17.2.5\n', 
'ssh 10.17.14.72\n', 'ssh 10.160.245.4\n', 'ssh 10.17.240.20\n', 'ssh 10.17.4.13\n', 
'ssh 10.17.4.14\n', 'ssh 10.17.4.21\n', 'ssh 10.17.4.22\n', 'ssh 10.17.4.23\n', 
'ssh 10.17.4.24\n', 'ssh 10.17.4.29\n', 'ssh 10.17.4.30\n', 'ssh 10.17.4.87\n', 
'ssh 10.17.4.88\n', 'ssh 10.17.4.15\n', 'ssh 10.17.4.16\n', 'ssh 10.17.4.69\n', 
'ssh 10.17.4.70\n', 'ssh 10.17.4.126\n', 'ssh 10.17.4.125\n', 'ssh 10.17.4.25\n', 
'ssh 10.17.4.77\n', 'ssh 10.17.4.79\n', 'ssh 10.17.4.80\n', 'ssh 10.17.240.11\n', 
'ssh 10.160.255.25\n', 'ssh 10.17.4.8\n', 'ssh 10.17.4.9\n', 'ssh 10.17.8.4\n', 
'ssh 10.160.99.3\n', 'ssh 10.17.4.6\n', 'ssh 10.17.4.7\n', 'ssh 10.17.16.3\n', 
'ssh 10.17.4.26\n', 'ssh 10.17.4.71\n', 'ssh 10.17.4.78\n', 'ssh 10.17.4.86\n', 
'ssh 10.17.13.122\n', 'ssh 10.160.255.19\n', 'ssh 10.17.4.84\n', 'ssh 10.17.4.54\n']

bdc_devices = [
'ssh 10.160.255.59\n', 'ssh 10.160.255.60\n', 'ssh 10.160.255.61\n', 'ssh 10.160.255.62\n',
 'ssh 10.160.255.58\n', 'ssh 10.160.255.57\n', 'ssh 10.160.255.75\n', 'ssh 10.161.18.192\n',
 'ssh 10.161.18.230\n', 'ssh 10.161.13.118\n', 'ssh 10.161.12.62\n', 'ssh 10.160.255.56\n',
 'ssh 10.160.255.78\n', 'ssh 10.161.18.142\n', 'ssh 10.161.18.147\n', 'ssh 10.161.18.212\n',
 'ssh 10.161.18.197\n', 'ssh 10.161.29.30\n', 'ssh 10.161.18.198\n', 'ssh 10.161.18.201\n',
 'ssh 10.161.18.202\n', 'ssh 10.161.18.188\n', 'ssh 10.161.99.3\n', 'ssh 10.161.18.189\n', 
'ssh 10.161.18.190\n', 'ssh 10.160.255.55\n', 'ssh 10.161.24.73\n', 'ssh 10.160.255.63\n',
 'ssh 10.160.255.64\n', 'ssh 10.161.18.176\n', 'ssh 10.161.18.177\n', 'ssh 10.161.18.178\n',
 'ssh 10.161.18.179\n', 'ssh 10.161.18.180\n', 'ssh 10.161.18.181\n', 'ssh 10.161.18.194\n',
 'ssh 10.161.18.182\n', 'ssh 10.161.18.183\n', 'ssh 10.161.18.184\n', 'ssh 10.161.18.185\n',
 'ssh 10.161.18.186\n', 'ssh 10.161.18.187\n', 'ssh 10.161.18.203\n', 'ssh 10.161.18.209\n',
 'ssh 10.161.29.166\n', 'ssh 10.161.13.110\n', 'ssh 10.161.28.28\n', 'ssh 10.161.28.27\n',
 'ssh 10.161.29.203\n', 'ssh 10.160.255.74\n']


io_devices = [
'ssh 10.160.255.112\n', 'ssh 10.160.255.113\n', 'ssh 10.160.255.111\n', 
'ssh 10.160.255.117\n', 'ssh 10.160.255.118\n', 'ssh 10.160.255.116\n']

nx_os = ['ssh 10.17.4.61\n', 'ssh 10.17.4.62\n', 'ssh 10.17.4.63\n', 'ssh 10.17.4.64\n',
 'ssh 10.17.4.10\n', 'ssh 10.17.4.11\n', 'ssh 10.17.4.4\n', 'ssh 10.17.4.5\n', 'ssh 10.17.4.8\n',
 'ssh 10.17.4.9\n', 'ssh 10.17.4.6\n', 'ssh 10.17.4.7\n', 'ssh 10.161.18.231\n', 'ssh 10.161.18.232\n', 
'ssh 10.161.18.233\n', 'ssh 10.161.18.234\n', 'ssh 10.161.18.158\n', 'ssh 10.161.18.159\n', 'ssh 10.161.18.162\n', 
'ssh 10.161.18.163\n', 'ssh 10.161.18.156\n', 'ssh 10.161.18.157\n', 'ssh 10.161.18.164\n', 'ssh 10.161.18.165\n']

ext_devices = ['ssh 10.160.208.3\n', 'ssh 10.160.208.4\n', 'ssh 10.160.208.6\n',
 'ssh 10.160.208.41\n', 'ssh 10.160.208.19\n', 'ssh 10.160.208.25\n', 'ssh 10.160.208.9\n',
 'ssh 10.160.208.15\n', 'ssh 10.160.208.14\n', 'ssh 10.160.208.5\n', 'ssh 10.160.208.23\n',
 'ssh 10.160.208.24\n', 'ssh 10.160.208.21\n', 'ssh 10.160.208.22\n', 'ssh 10.160.208.18\n',
 'ssh 10.160.208.7\n', 'ssh 10.160.208.8\n', 'ssh 10.160.208.28\n', 'ssh 10.160.208.40\n',
 'ssh 10.160.208.30\n', 'ssh 10.17.20.218\n', 'ssh 10.17.20.226\n', 'ssh 10.160.208.31\n', 
'ssh 10.160.208.32\n', 'ssh 10.160.208.33\n', 'ssh 10.160.208.34\n', 'ssh 10.160.214.212\n',
 'ssh 10.160.214.202\n', 'ssh 10.160.214.213\n', 'ssh 10.160.214.226\n', 'ssh 10.160.214.214\n',
 'ssh 10.160.214.230\n', 'ssh 10.160.208.35\n', 'ssh 10.160.208.36\n', 'ssh 10.160.208.37\n', 
'ssh 10.160.208.38\n', 'ssh 10.160.208.39\n']

ho_devices = ['ssh 10.160.141.65\n', 'ssh 10.160.141.120\n', 'ssh 10.160.141.121\n', 'ssh 10.160.141.89\n', 
'ssh 10.160.141.68\n', 'ssh 10.160.141.69\n', 'ssh 10.160.131.4\n', 
'ssh 10.160.131.130\n', 'ssh 10.160.129.4\n', 'ssh 10.160.249.196\n', 'ssh 10.160.249.197\n', 'ssh 10.160.249.199\n',
 'ssh 10.160.249.201\n', 'ssh 10.160.249.203\n', 'ssh 1S0.160.249.204\n', 'ssh 10.160.249.205\n', 'ssh 10.160.249.206\n',
 'ssh 10.160.249.221\n', 'ssh 10.160.249.222\n', 'ssh 10.160.249.193\n', 'ssh 172.16.32.28\n', 'ssh 172.16.32.29\n',
 'ssh 10.152.232.2\n', 'ssh 10.152.232.3\n', 'ssh 10.152.232.4\n', 
'ssh 10.152.232.5\n', 'ssh 10.152.241.104\n', 'ssh 10.152.240.2\n', 'ssh 10.152.240.159\n', 'ssh 10.17.241.6\n', 
'ssh 10.17.241.7\n', 'ssh 10.160.170.95\n', 'ssh 10.160.170.65\n', 
'ssh 10.160.170.70\n', 'ssh 10.160.170.71\n', 'ssh 10.17.67.195\n', 'ssh 10.17.64.163\n', 'ssh 10.17.64.164\n',
 'ssh 10.160.170.72\n', 'ssh 10.160.170.73\n', 'ssh 10.160.170.74\n', 'ssh 10.160.170.75\n', 'ssh 10.160.170.78\n',
 'ssh 10.160.170.79\n', 'ssh 10.160.170.80\n', 'ssh 10.160.170.81\n', 'ssh 10.160.170.82\n', 'ssh 10.160.170.83\n',
 'ssh 10.160.170.96\n', 'ssh 10.160.170.97\n', 'ssh 10.160.170.84\n', 'ssh 10.160.170.85\n', 'ssh 10.160.166.129\n',
 'ssh 10.17.241.2\n', 'ssh 10.17.241.3\n', 'ssh 10.160.166.163\n', 'ssh 10.160.166.164\n', 'ssh 10.160.166.165\n',
 'ssh 10.160.166.166\n', 'ssh 10.160.166.168\n', 'ssh 10.160.166.169\n', 'ssh 10.160.166.140\n', 'ssh 10.160.166.141\n',
 'ssh 10.160.166.136\n', 'ssh 10.160.248.120\n', 'ssh 10.160.248.121\n', 'ssh 10.67.66.10\n', 'ssh 10.160.248.128\n',
 'ssh 10.67.66.6\n', 'ssh 10.67.66.7\n', 'ssh 10.67.66.11\n', 'ssh 10.67.66.12\n', 'ssh 10.67.67.1\n', 'ssh 10.67.67.2\n',
 'ssh 10.67.66.13\n', 'ssh 10.67.66.14\n', 'ssh 10.67.66.15\n', 'ssh 10.67.66.16\n', 'ssh 10.67.66.17\n', 'ssh 10.67.66.18\n',
 'ssh 10.67.66.19\n', 'ssh 10.67.66.20\n', 'ssh 10.67.66.21\n', 'ssh 10.67.66.22\n', 'ssh 10.67.66.23\n', 
 'ssh 10.67.66.26\n', 'ssh 10.67.66.27\n', 'ssh 10.67.66.28\n', 'ssh 10.67.66.29\n', 'ssh 10.67.66.30\n',
 'ssh 10.67.66.31\n', 'ssh 10.67.66.32\n', 'ssh 10.160.249.149\n', 'ssh 10.160.249.149\n', 'ssh 10.160.249.148\n',
 'ssh 10.160.249.130\n', 'ssh 10.160.249.131\n', 'ssh 10.160.248.52\n', 'ssh 10.160.248.53\n', 'ssh 10.160.24.10\n', 
'ssh 10.160.248.58\n', 'ssh 10.160.24.2\n', 'ssh 10.160.24.3\n', 'ssh 10.160.24.11\n', 'ssh 10.160.24.12\n', 'ssh 10.160.24.13\n',
 'ssh 10.160.24.14\n', 'ssh 10.160.24.15\n', 'ssh 10.160.24.17\n', 'ssh 10.160.24.18\n', 'ssh 10.160.24.20\n']

bo_devices = ['ssh 10.152.33.14\n', 'ssh 10.152.240.21 \n', 'ssh 10.152.240.149\n', 'ssh 10.152.33.69\n', 
'ssh 10.152.240.25\n', 'ssh 10.152.240.154\n', 'ssh 10.152.240.9\n', 'ssh 10.152.240.136\n', 'ssh 10.152.241.105\n',
 'ssh 10.152.232.66\n', 'ssh 10.152.232.67\n', 'ssh 10.152.34.134\n', 'ssh 10.152.240.14\n', 'ssh 10.152.240.142\n',
 'ssh 10.152.34.66\n', 'ssh 10.152.34.67\n', 'ssh 10.152.240.19\n', 'ssh 10.152.240.147\n', 'ssh 10.152.241.68\n',
 'ssh 10.152.236.2\n', 'ssh 10.152.236.3\n', 'ssh 10.152.236.4\n', 'ssh 10.152.240.31\n', 'ssh 10.152.240.130\n',
 'ssh 10.152.34.2\n', 'ssh 10.152.240.10\n', 'ssh 10.152.240.137\n', 'ssh 10.152.20.133\n', 'ssh 10.152.20.130\n',
 'ssh 10.152.20.131\n', 'ssh 10.152.20.139\n', 'ssh 10.152.240.7\n', 'ssh 10.152.240.134\n', 'ssh 10.152.241.86\n',
 'ssh 10.152.241.87\n', 'ssh 10.152.231.132\n', 'ssh 10.152.240.13\n', 'ssh 10.152.240.141\n', 'ssh 10.152.24.2\n',
 'ssh 10.152.240.24\n', 'ssh 10.152.240.153\n', 'ssh 10.152.35.68\n', 'ssh 10.152.240.23\n', 'ssh 10.152.240.151\n',
 'ssh 10.152.25.2\n', 'ssh 10.152.240.27\n', 'ssh 10.152.240.156\n', 'ssh 10.152.26.3\n', 'ssh 10.152.240.85\n',
 'ssh 10.152.240.220\n', 'ssh 10.152.241.103\n', 'ssh 10.152.240.71\n', 'ssh 10.152.240.199\n', 'ssh 10.152.26.130\n',
 'ssh 10.152.26.135\n', 'ssh 10.152.240.68\n', 'ssh 10.152.240.196\n', 'ssh 10.152.22.5\n', 'ssh 10.152.240.16\n',
 'ssh 10.152.240.144\n', 'ssh 10.152.20.2\n', 'ssh 10.152.240.5\n', 'ssh 10.152.240.132\n', 'ssh 10.152.21.130\n',
 'ssh 10.152.240.15\n', 'ssh 10.152.240.143\n', 'ssh 10.152.21.2\n', 'ssh 10.152.21.19\n', 'ssh 10.152.21.8\n',
 'ssh 10.152.240.22 \n', 'ssh 10.152.240.150 \n', 'ssh 10.152.241.74\n', 'ssh 10.152.241.75\n', 'ssh 10.152.236.36\n',
 'ssh 10.152.240.11\n', 'ssh 10.152.240.138\n', 'ssh 10.152.35.2\n', 'ssh 10.152.35.3\n', 'ssh 10.152.240.1\n',
 'ssh 10.152.240.129\n', 'ssh 10.152.22.130\n', 'ssh 10.152.240.20\n', 'ssh 10.152.240.148\n', 'ssh 10.152.241.100 \n',
 'ssh 10.152.236.74\n', 'ssh 10.152.236.73\n', 'ssh 10.152.236.72\n', 'ssh 10.152.236.71\n', 'ssh 10.152.236.70\n',
 'ssh 10.152.236.69\n', 'ssh 10.152.236.68\n', 'ssh 10.152.237.13\n', 'ssh 10.152.237.14\n', 'ssh 10.152.241.72\n',
 'ssh 10.152.241.73\n', 'ssh 10.152.236.197\n', 'ssh 10.152.236.198\n', 'ssh 10.152.236.199\n', 'ssh 10.152.236.196\n',
 'ssh 10.152.237.57\n', 'ssh 10.152.237.58\n', 'ssh 10.152.2.2\n', 'ssh 10.152.2.3\n', 'ssh 10.152.240.17\n', 'ssh 10.152.240.145\n',
 'ssh 10.152.241.70\n', 'ssh 10.152.241.71\n', 'ssh 10.152.231.101\n', 'ssh 10.152.231.102\n', 'ssh 10.152.240.3\n',
 'ssh 10.152.240.131\n', 'ssh 10.152.10.2\n', 'ssh 10.152.10.3\n', 'ssh 10.152.240.29 \n', 'ssh 10.152.240.158\n',
 'ssh 10.152.24.130\n', 'ssh 10.152.240.28\n', 'ssh 10.152.240.157\n', 'ssh 10.152.241.96\n', 'ssh 10.152.235.70\n',
 'ssh 10.152.235.71\n', 'ssh 10.152.235.72\n', 'ssh 10.152.235.73\n', 'ssh 10.152.235.126\n', 'ssh 10.152.237.70\n',
 'ssh 10.152.237.71\n', 'ssh 10.152.27.2\n', 'ssh 10.152.240.94\n', 'ssh 10.152.240.229\n', 'ssh 10.152.6.2\n', 'ssh 10.152.6.3\n',
 'ssh 10.152.240.84\n', 'ssh 10.152.240.219\n', 'ssh 10.152.23.130\n', 'ssh 10.152.240.82\n', 'ssh 10.152.240.217\n',
 'ssh 10.152.241.102\n', 'ssh 10.152.236.132\n', 'ssh 10.152.236.133\n', 'ssh 10.152.240.96 \n', 'ssh 10.152.240.231\n',
 'ssh 10.152.241.98\n', 'ssh 10.152.234.65\n', 'ssh 10.152.234.7\n', 'ssh 10.152.234.5 \n', 'ssh 10.152.234.6\n',
 'ssh 10.152.234.4\n', 'ssh 10.152.234.27\n', 'ssh 10.152.240.211\n', 'ssh 10.152.237.34\n', 'ssh 10.152.241.88\n',
 'ssh 10.152.224.226\n', 'ssh 10.160.126.64\n', 'ssh 10.152.240.207\n', 'ssh 10.152.241.79\n', 'ssh 10.152.230.164\n',
 'ssh 10.152.230.165\n', 'ssh 10.152.240.66\n', 'ssh 10.152.240.194\n', 'ssh 10.152.230.166\n', 'ssh 10.152.36.2\n',
 'ssh 10.152.240.89\n', 'ssh 10.152.240.224\n', 'ssh 10.152.16.2\n', 'ssh 10.152.16.3\n', 'ssh 10.152.240.87\n',
 'ssh 10.152.240.222\n', 'ssh 10.152.29.2\n', 'ssh 10.152.240.90 \n', 'ssh 10.152.240.225\n', 'ssh 10.152.35.196\n',
 'ssh 10.152.240.92\n', 'ssh 10.152.240.227 \n', 'ssh 10.152.36.69\n', 'ssh 10.152.240.75\n', 'ssh 10.152.240.202\n',
 'ssh 10.152.29.131\n', 'ssh 10.152.29.130\n', 'ssh 10.152.240.69\n', 'ssh 10.152.240.197\n', 'ssh 10.152.36.130\n',
 'ssh 10.152.240.72\n', 'ssh 10.152.240.200\n', 'ssh 10.152.37.4\n', 'ssh 10.152.37.5 \n', 'ssh 10.152.240.93\n',
 'ssh 10.152.240.228\n', 'ssh 10.152.30.130\n', 'ssh 10.152.30.131\n', 'ssh 10.152.240.81\n', 'ssh 10.152.240.216\n',
 'ssh 10.152.241.76\n', 'ssh 10.152.235.139\n', 'ssh 10.152.235.140\n', 'ssh 10.152.235.136\n', 'ssh 10.152.235.137\n',
 'ssh 10.152.235.183\n', 'ssh 10.152.235.135\n', 'ssh 10.152.237.44\n', 'ssh 10.152.237.45\n', 'ssh 10.152.37.133\n',
 'ssh 10.152.37.132\n', 'ssh 10.152.240.79\n', 'ssh 10.152.240.214\n', 'ssh 10.152.241.95\n', 'ssh 10.152.237.69\n',
 'ssh 10.152.240.210\n', 'ssh 10.152.38.66\n', 'ssh 10.152.240.86\n', 'ssh 10.152.240.221\n', 'ssh 10.152.230.196\n',
 'ssh 10.152.230.197\n', 'ssh 10.152.240.78\n', 'ssh 10.152.240.213\n', 'ssh 10.152.241.92\n', 'ssh 10.152.241.93\n',
 'ssh 10.152.241.89\n', 'ssh 10.152.237.76\n', 'ssh 10.152.240.208\n', 'ssh 10.152.37.197\n', 'ssh 10.152.240.70\n',
 'ssh 10.152.240.198\n', 'ssh 10.152.18.3\n', 'ssh 10.152.18.2\n', 'ssh 10.152.240.83\n', 'ssh 10.152.240.218\n',
 'ssh 10.152.32.2\n', 'ssh 10.152.240.80\n', 'ssh 10.152.240.215\n', 'ssh 10.152.241.66\n', 'ssh 10.152.236.164\n',
 'ssh 10.152.236.165\n', 'ssh 10.152.240.67\n', 'ssh 10.152.240.195\n', 'ssh 10.152.241.85\n', 'ssh 10.152.237.54\n',
 'ssh 10.152.240.206\n', 'ssh 10.152.241.90\n', 'ssh 10.152.241.91\n', 'ssh 10.152.231.68\n', 'ssh 10.152.231.69\n',
 'ssh 10.152.237.72\n', 'ssh 10.152.240.212\n']


devices = [
 'ssh 10.160.249.203\n']
 

post = open('Kobe_error_2.txt', 'w')


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
	time.sleep(1)
	output = net_connect.read_channel()

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
		pre_lldp = net_connect.send_command("show auth sess | i VOI", use_textfsm=True)
		pre_vty = net_connect.send_command("show auth sess | i Un")
		#pre_vty2 = net_connect.send_command("show auth sess meth mab | i DATA", use_textfsm=True)
		now = datetime.now()
		print(now)
		post.write(str(now) + '\n')
	
		print("-" * 25 + "Voice_auth" + "-" * 25)
		post.write("-" * 25 + "Voice_auth" + "-" * 25 + "\n")
		pprint.pprint(pre_lldp)
		pprint.pprint(pre_lldp, stream =  post)
		print("-" * 25 + "auth failure" + "-" * 25)
		post.write("-" * 25 + "auth failure" + "-" * 25 + "\n")
		pprint.pprint(pre_vty)
		pprint.pprint(pre_vty, stream = post)
		#print("-" * 25 + "auth mab data" + "-" * 25)
		#post.write("-" * 25 + "auth mab data" + "-" * 25 + "\n")
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