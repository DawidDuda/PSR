import socket
import os
import subprocess
import threading
from tkinter import *
from tkinter import ttk

host = '192.168.101.10' #Server ip
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
 
 
 
 
def snd_dwn(prog_name):
 
    data, addr = s.recvfrom(1024)
    data = data.decode('utf-8')
    print("Message from: " + str(addr))
    print("From connected user: " + data)      

 
    print("Sending...")
    file = open(prog_name, 'rb')
    filedata = file.read(99999)
    s.sendto(bytes(filedata), addr)
 
 
 
class download(threading.Thread):
    def __init__(self,prog_name):
        threading.Thread.__init__(self)
        self.prog_name = prog_name
        
    def run(self):
        snd_dwn(self.prog_name)
        print("Wys?ano")
    

while True:
    
    download("test.txt").start()
