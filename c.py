import socket
import os
import subprocess
import threading
from tkinter import *
from tkinter import ttk

host='127.0.0.1'
port = 4000

server = (host, port)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_exe(s, exe_name):
    file = open(exe_name, 'rb')
    file_data = file.read(1024)
    s.connect((host,port))
    s.send(file_data)

class send_thread(threading.Thread):
    def __init__(self,mess):
        self.mess = mess
    
    def run(self):
        send_exe(s, mess)

def mess(message):
    
    s.sendto(message.encode('utf-8'), server)
    #print(os.system('cmd /k "tescik.exe"'))
    
mess("dzialajj")

send_exe(s, "tescik.exe")
