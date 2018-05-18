import math
import reg
from conversion import netmask

network = network.split("/")  #split network & mask
network_id = network[0]
network_mask = network[1]

if re.match(r"[0-9][0-9]", network_mask):
  network_mask = network_mask
else if re.match (r"[0-9][0-9][0-9]'\.'[0-9][0-9][0-9]'\.'[0-9][0-9][0-9]'\.'[0-9][0-9][0-9]"):
  network_mask = netmask(network_mask)
else print("Wrong Mask!")


