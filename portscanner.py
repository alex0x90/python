#Simple port scanner python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(3)

#
host = input("Enter IP to scan: ")
#host = "127.0.0.1" 
#
def portscan(port):
        if sock.connect_ex((host,port)):
                print("[-] Port %s is closed" %port)
        else:
                print("[+] Port %s is opened" % port)

#port range to scan
print("Scanning %s for common ports (1-1024)" %host)
for port in range(1,1025):
    portscan(port)

    
