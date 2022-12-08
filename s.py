import socket
import os
import time
import subprocess
import threading
from tkinter import *
from tkinter import ttk

host = '192.168.101.10' #Server ip
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

client = [('192.168.101.11', 4005),('192.168.101.156', 4005)]
 
def send_request(prog_name, dstclient):
    
    message = "run:" + str(prog_name)
                
    s.sendto(message.encode('utf-8'), dstclient)
                    
    data, addr = s.recvfrom(99999)
    data = data.decode('utf-8')
    print("Message from: " + str(addr))
    print("From connected user: " + data) 
    if(data[0:3]== "snd"):
        print("wysylam" +data[4::])
        dwn_snd(data[4::])
            
 
def dwn_snd(prog_name, dstclient):    
         

 
    print("Sending...")
    file = open(prog_name, 'rb')
    filedata = file.read(99999)
    s.sendto(bytes(filedata), dstclient)
 
 
 
class send_exe(threading.Thread):
    def __init__(self,prog_name, dstclient):
        threading.Thread.__init__(self)
        self.prog_name = prog_name
        self.dstclient = dstclient
        
    def run(self):
        dwn_snd(self.prog_name, self.dstclient)
        print("Wys?ano")
 

    

#dwn_snd("unt.py")
send_request("unt.py", client[1])
#while True:   
#    send_exe("test.txt").start()
