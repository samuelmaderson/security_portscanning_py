from pprint import pprint
import socket
import argparse


def host(ip: str, port: any):
    if port.find('-') != -1:
        port = port.split('-')
        for port in range(int(port[0]),int(port[1])):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip,port))
            if result == 0:
                print(f'Port: {port} open')
            sock.close()

    elif port.find(',') != -1:
        port = port.split(',')
        for pport in port:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip,int(pport)))
            if result == 0:
                print(f'Port: {pport} open')
            sock.close()
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip,int(port)))
        if result == 0:
                print(f'Port: {port} open')
        sock.close


def subnet(iprange: str, port: any):
    for i in range(1,255):
        if port.find(',') != -1:
            iprange = iprange.split('0/24')[0]
            ip = iprange+str(i)
            print(f'Scanning host:{ip}')
            p = port.split(',')
            for pport in p:

                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip,int(pport)))
                if result == 0:
                    print(f'Port: {pport} open')
                sock.close()

        else:
            iprange = iprange.split('0/24')[0]
            ip = iprange+str(i)
            print(f'Scanning host:{ip}')
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip,int(port)))
            if result == 0:
                print(f'Port: {pport} open')
            sock.close()
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', help='target to scan ports')
    parser.add_argument('--port', help='destionation port to be checked')
    parser.add_argument('--range')
    args = parser.parse_args()
    if args.ip == None and args.range == None:
        print('No host was specified, use --help for options!')
        exit(0)
    if args.range != None:
        subnet(args.range, args.port)
    else:
        host(args.ip, args.port)
