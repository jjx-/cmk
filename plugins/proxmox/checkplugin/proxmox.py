#!/usr/bin/python

#Agent output example
<<<proxmox>>>
100 CheckMK running 1024 13.3 6.6
101 Offloader running 32 0.0 0.2

#Proxmoxs VE Host
def inventory_proxmox(info):
    for i in info:
        vm = i[0] + " " + i[1]
        yield vm, {}

def check_proxmox(item, params, info):
    perfdata = []
    

check_info["proxmox"] = {
    "check_function" : check_proxmox,
    "inventory_function" : inventory_proxmox,
    "service_description" : "VM %s",
    "has_perfdata" : True,
    "group" : "proxmox",
}
