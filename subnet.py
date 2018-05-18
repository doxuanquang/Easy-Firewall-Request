
import math
import re
from conversion import netmask

"""
network = network.split("/")  #split network & mask
network_id = network[0]
network_mask = network[1]
"""

network_mask = "255.255.255.256"
if len(network_mask) <3:
    network_mask = network_mask
elif re.match (r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", network_mask) != None:
    network_mask = netmask(network_mask)
else:
    print("Wrong Mask!")

print(network_mask)