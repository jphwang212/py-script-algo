#      192.168.0.10 - 192.169.2.100
#
#      192 168 0 10
#      192 169 2 100
#
#      [192] => 192.
#      192.168.0.10, 192.168.0.11, ... , 192.168.0.255
#      192.168.1.0, 192.168.1.1, ... , 192.168.1.255
#      192.168.2.0, 192.168.2.1, ... , 192.168.2.255
#      ...
#      192.169.0.0, 192.169.0.1, ... , 192.169.0.255
#      192.169.1.0, 192.169.1.1, ... , 192.169.1.255
#      192.169.2.0, 192.169.2.1, ... , 192.169.2.255
#
#      0. Make new list
#      1. join matching octets
#      2. Get current octet (first differing octet), get last octet
#      3. while current octet <= same positioned octet and current octet isn't last octet:
#           Get octets between current and last, join with current octet
#           Join current octet with last octet
#           Add to new list
#           increment last octet
#           if last octet == 256:
#             last octet = 0
#             current octet += 1
#             if current octet == same pos octet:
#               current octet = next octet
#
#      4. Increment current octet until upper limit, add to list
#      5. Return new list
