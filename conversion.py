import re
import math

def netmask(mask):
    mask = mask.split(".")
    print(mask)
    mask_length = 0
    binary_mask = ""
    for octet in mask:
        octet = int(octet)
        octet = bin(octet)
        print(octet)
        octet = octet[2:10]
        print(octet)
        binary_mask += octet
    print(binary_mask)
    print(re.search("01",binary_mask))
    if re.search("01",binary_mask) != None:
            print("Bad mask!!!")
    else:
        mask_length += binary_mask.count("1")
    return mask_length

mask = "255.255.254.128"
print(netmask(mask))