import os
import subprocess
import socket
import psutil

host='127.0.0.1'
port = 4000
    
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))

def download():
    data, addr = s.recvfrom(1024)
    data = data.decode('utf-8')
    server = (host, port)
    

def snd_dwn():
    data, addr = s.recvfrom(1024)
    data = data.decode('utf-8')
    print("message from: "+str(addr))
    print("from conencted: "+data)
    if(data == "tescik.exe"):
        if(os.path.exists("tescik.exe")):
           print(subprocess.check_output('tescik.exe', shell=True, text=True))
        
        else:
            message = "0"
            server = (host,port)
            s.sendto(message.encode('utf-8'), server)
 

def check_is_running(exe_name):
    
    while(True):
        stan = (exe_name in (i.name() for i in psutil.process_iter()))
        if(stan == True):
            print(exe_name + " działa")
snd_dwn()
    
