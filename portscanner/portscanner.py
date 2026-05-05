import socket
import termcolor

def scan(target, ports):
        print('\n' + ' Starting Scan For ' + str(target))
        for port in range(1,ports):
                scan_port(target,port)
def scan_port(ipaddress, port):
        try:
                sock = socket.socket()
                sock.connect((ipaddress, port))
                print('[+] Port Opened ' + str(port))
                sock.close()
        except: 
                pass

targets = input("[*] Enter Target to Scan(split them by ,): ")
ports = int(input("[*} Enter How Many Ports you Want to Scan: "))

if "," in targets:
        print(termcolor.colored(("[*] Scanning Multiple Targets"),'green'))
        for ip_addr in targets.split(","):
                scan(ip_addr.strip(' '),ports)
