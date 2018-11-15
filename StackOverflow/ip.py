newSet = ["1.0.0.0/24","1.0.0.0/16","1.0.0.0/8","2.0.0.0/24","2.0.0.0/16"]

ip_dict = {}
for ip_subnet in newSet:
    ip,subnet = ip_subnet.split('/')
    subnet = int(subnet)
    if ip not in ip_dict or ip_dict[ip] > subnet:
        ip_dict[ip] = subnet
updated_list = [str(ip)+"/"+str(subnet) for ip,subnet in ip_dict.iteritems()]

ipTotal = 0
for subnet in ip_dict.values():
    y = 32 - int(subnet)
    x = pow(2, y)
    ipTotal = ipTotal + x 


print updated_list,ipTotal
