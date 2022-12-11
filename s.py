import socket
import os
import time
import subprocess
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
host = '192.168.101.10' #Server ip
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

class data:
    filename = ""

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
        snd(data[4::], dstclient)
            
 
def snd(prog_name, dstclient):    

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
        send_request(self.prog_name, self.dstclient)
        print("Wys?ano")
 

    

#snd("unt.py")
#send_request("unt.py", client[1])
#while True:   
#send_exe("unt.py", client[1]).start()
##################### GUI ########################
def add_client(ip):
    client.append((ip, 4005))
    
def print_c():
    for i in range(len(client)):
        print(client[i])

def run_exe():
    for i in range(get_number_cli()):
        send_exe("unt.py", client[i]).start()

def get_filename():
    for i in range(len(data.filename)):
        if(data.filename[i]=='/'):
            point = i+1
            
    data.filename = data.filename[point::]
   

def get_number_cli():
    return len(client)     
    
    
def MainWindow():
    window = tk.Tk()
    window.title("PSR")
    window.geometry("600x400")
    frame1 = tk.Frame(master=window,relief=tk.RAISED, width=200, height=100)
    frame1.pack( side=tk.RIGHT)
    frame2 = tk.Frame(master=window,relief=tk.RAISED,  height=30)
    frame2.pack( side=tk.BOTTOM)
    
    def add_btn():
        inp = inputtxt.get(1.0, "end-1c")
        add_client(inp)
        print_cli()
        #lbl.config(text = "Provided Input: "+inp)
        
    def choose_file():
        data.filename = fd.askopenfilename()
        
    def print_cli():
        for i in range(len(client)):
            label = tk.Label(master=frame1, text=client[i][0])
            label.pack()
            
            
   
    
    
    label = tk.Label(master=frame1, text="test")
    label.pack()
    
    print_cli()
    choose_file()
    get_filename()
    filename_lbl = tk.Label(master=frame2, text=data.filename)
    filename_lbl.pack()
    
    
    inputtxt = tk.Text(window,
                   height = 1,
                   width = 20)
    inputtxt.pack()
    
    printButton = tk.Button(window,
                        text = "Dodaj ip klienta", 
                        command = add_btn)
    printButton.pack()
    
    runButton = tk.Button(window,
                        text = "uruchom zdalnie", 
                        command = run_exe)
    runButton.pack()
    
    #
    
    print("file"+data.filename)
    
    window.mainloop()

MainWindow()
