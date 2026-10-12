def split_ip(ip, subnet, num_bytes):

    net = []
    host = []


    for i in range(num_bytes):
        net_byte = ip[i] & subnet[i]
        host_byte = ip[i] & (0xff - subnet[i])

        net.append(net_byte)
        host.append(host_byte)
    return net, host


ip = [192, 168, 17, 2]
mask = [255,255,248,0]
num_bytes = 4

net_bytes, host_bytes = split_ip(ip, mask, num_bytes)

print(f"Network bytes: {net_bytes}")
print(f"Host bytes: {host_bytes}")
