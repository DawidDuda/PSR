
import threading
import socket
import os
import shutil

host='192.168.101.11' #client ip
port = 4005
server = ('192.168.101.10', 4000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
   
        
def download_prog(message):
    if(message !='q'):
        try:
            
            
            s.sendto(message.encode('utf-8'), server)
            file = open("test.txt", 'wb')
            data, addr = s.recvfrom(99999)
        
            file.write(bytes(data))
            file.close()
            print("odebrano")
            

        except:
            print("Brak połączenia")
            


download_prog("w")


