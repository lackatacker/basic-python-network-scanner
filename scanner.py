from socket import *
import time
import os
import platform
import socket
import threading
from datetime import datetime
from queue import Queue
startTime = time.time()  # On aura besoin de cette variable pour déterminer le
# Temps d'éxecution
# comments might contain typing mistakes ;)
#if __name__ == '__main__':# Si le programme est appelé en invoke il sera éxecuté, mais pas en import
    # L'adresse IP privée à scanner
    def socket_scan():
        target = input('Enter the host to be scanned: ')
        # T_IP stock le nom de l'ip retourné par la fonction
        t_IP = gethostbyname(target)
        print('Starting scan on host: ', t_IP)

        for i in range(50, 500):  # Liste de ports à scanner
            # s = variable socket- AF_INET = l'adresse IP de mon hôte
            s = socket(AF_INET, SOCK_STREAM)
            # SOCK_STREAM = communication TCP
            # On essaye de créer une connexion avec l'adresse ip
            conn = s.connect_ex((t_IP, i))
            # + port donnés en paramètres;Renvoie 0 en cas de réussite

            if (conn == 0):
                print('Port %d: Service %s OPEN' % (i, getservbyport(i)))
        print('Time taken:', time.time() - startTime)
        s.close()  # inutile de la laisser ouverte XD
    def ping_scan():
        net = input("Enter the Network Address: ")
        net1 = net.split('.')
        a = '.'

        net2 = net1[0] + a + net1[1] + a + net1[2] + a
        st1 = int(input("Enter the Starting Number: "))
        en1 = int(input("Enter the Last Number: "))
        en1 = en1 + 1
        oper = platform.system()

        if (oper == "Windows"):
            ping1 = "ping -n 1 "
        elif (oper == "Linux"):
            ping1 = "ping -c 1 "
        else:
            ping1 = "ping -c 1 "
        t1 = datetime.now()
        print("Scanning in Progress:")

        for ip in range(st1, en1):
            addr = net2 + str(ip)
            comm = ping1 + addr
            response = os.popen(comm)

            for line in response.readlines():
                if (line.count("TTL")):
                    break
                if (line.count("TTL")):
                    print(addr, "--> Live")

        t2 = datetime.now()
        total = t2 - t1
        print("Scanning completed in: ", total)
    def tcp_scan():
        net = input("Enter the IP address: ")
        net1 = net.split('.')
        a = '.'

        net2 = net1[0] + a + net1[1] + a + net1[2] + a
        st1 = int(input("Enter the Starting Number: "))
        en1 = int(input("Enter the Last Number: "))
        print("Processing scan ...")
        en1 = en1 + 1
        t1 = datetime.now()

        def scan(addr):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((addr, 135))
            if result == 0:
                return 1
            else:
                return 0

        def run1():
            for ip in range(st1, en1):
                addr = net2 + str(ip)
                if (scan(addr)):
                    print(addr, "is live")

        run1()
        t2 = datetime.now()
        total = t2 - t1
        print("Scanning completed in: ", total)
    def multi_thread_scan():
        socket.setdefaulttimeout(0.25)
        print_lock = threading.Lock()

        target = input('Enter the host to be scanned: ')
        t_IP = socket.gethostbyname(target)
        print('Starting scan on host: ', t_IP)

        def portscan(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                con = s.connect((t_IP, port))
                with print_lock:
                    print(port, 'is open')
                con.close()
            except:
                pass
        def threader():
            while True:
                worker = q.get()
                portscan(worker)
                q.task_done()

        q = Queue()
        startTime = time.time()


        for x in range(100):
            t = threading.Thread(target=threader)
            t.daemon = True
            t.start()

        for worker in range(1, 500):
            q.put(worker)
        q.join()
        print('Time taken:', time.time() - startTime)
    print("Quel type de scan souhaitez vous realiser ? \n1 - scan de ports basee sur les sockets ?"
          " \n2 - scan de ports base sur les pings ?\n3 - un TCP scan ?\n4 - scan de ports en Multi-threading ")
    choice = int(input())
    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("Enter a valid number please : ")
        choice = int(input())
    else:
        if choice == 1:
            socket_scan()
        elif choice == 2:
            ping_scan()
        elif choice == 3:
            tcp_scan()
        elif choice == 4:
            multi_thread_scan()


