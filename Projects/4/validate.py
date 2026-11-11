#CS372
#Project 4
#Parker Palubeski

#Note : Change these to the folder containing the packet data as necessary
addrs_path = "tcp_data/"
data_path = "tcp_data/"

#converts ip to bytes
def ip_bytes(ip):
    return bytes(map(int, ip.split(".")))

#Calculate the Checksum
def checksum(data):
    if len(data) % 2:
        data += b"\x00"
    s = sum((data[i] << 8) + data[i + 1] for i in range(0, len(data), 2))
    while s >> 16:
        s = (s & 0xFFFF) + (s >> 16)
    return ~s & 0xFFFF

#Validate the packet
def validate(addr_file, data_file):
    addr_f = open(addr_file)
    src, dst = addr_f.read().split()
    addr_f.close()
    data_f = open(data_file, "rb")
    d = data_f.read()
    data_f.close()
    orig = (d[16] << 8) + d[17]
    zeroed = d[:16] + b"\x00\x00" + d[18:]
    pseudo = ip_bytes(src) + ip_bytes(dst) + b"\x00\x06" + len(d).to_bytes(2, "big")
    return checksum(pseudo + zeroed) == orig

#Start function calls
for i in range(10):
    try:
        if validate(f"{addrs_path}tcp_addrs_{i}.txt", f"{data_path}tcp_data_{i}.dat"): 
            print("PASS")
        else:
            print("FAIL")
    except FileNotFoundError:
        print(f"FAIL (File Not Found)") 