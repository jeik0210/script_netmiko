#!/usr/bin/env python
# -*- coding: utf-8 -*-
from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.203',
    'username': 'cisco',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l2_s1)
output = net_connect.send_command('show ip interface brief')
print(output)
