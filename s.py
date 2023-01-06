import socket
import os
import time
import sys
import subprocess
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import xml.etree.ElementTree as ET

host = '192.168.101.10' #Server ip
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))


                                           #Empty list to collect unreachable hosts

    
            
def send_request(prog_name, dstclient):
    for ip in dstclient:
        ping_test = subprocess.call('ping %s -n 2' % ip)        #Ping host n times
        if ping_test == 0: 
            message = "run:" + str(prog_name)
                        
            s.sendto(message.encode('utf-8'), dstclient)
            data, addr = s.recvfrom(99999)
            data = data.decode('utf-8')
            print("Message from: " + str(addr))
            print("From connected user: " + data) 
            
            Main.status_lbl.config(text = data)
            
            print("Sending " +data[4::])
            Main.status_lbl.config(text = "Sending")
            file = open(prog_name, 'rb')
            filedata = file.read(99999)
            s.sendto(bytes(filedata), dstclient)
            
            print("Sended")
            Main.status_lbl.config(text = "Sended")
            
            data, addr = s.recvfrom(99999)
            data = data.decode('utf-8')
            print("Message from: " + str(addr))
            print("From connected user: " + data) 
            Main.status_lbl.config(text = data)
            
 

        
 
class send_exe(threading.Thread):
    def __init__(self,prog_name, dstclient):
        threading.Thread.__init__(self)
        self.prog_name = prog_name
        self.dstclient = dstclient
        
    def run(self):
        send_request(self.prog_name, self.dstclient)
        
 

        
    

##################### GUI ########################
def add_client(ip):
    Main.client.append((ip, 4005))
    
def print_c():
    for i in range(len(Main.client)):
        print(Main.client[i])
        print(i)
        Main.client_lbl[i]
        

def run_exe():
    for i in range(get_number_cli()):
        send_exe(Main.filename, Main.client[i]).start()
        
    
 
   

def get_number_cli():
    return len(Main.client)     
    
def readXML():
    tree = ET.parse('config.xml')
    
    root = tree.getroot()
    
    file=root.find("file")
    Main.filename = (file.text)
    Main.filename_lbl.config(text = (file.text))
    
    #command = root.find("command")
    #Main.command = (command.text)
    
    args = root.find("args")
    Main.args = (args.text)
    
    for client in root.iter('client'):
        Main.client.append((client.text, 4005))
        Main.client_lbl.append(tk.Label(master=Main.window, text=client.text))
    


class Main:
    window = tk.Tk()
    filename = ""
    #command = ""
    args = ""
    client = []
    client_lbl = []
    filename_lbl = tk.Label(master=window, text=filename)
    status_lbl = tk.Label(master=window, text="Status programu")
    
    runButton = tk.Button(window,
                        text = "uruchom zdalnie", 
                        command = run_exe)
    

    
def MainWindow():
    
    Main.window.title("PSR")
    Main.window.geometry("600x400")
    
    readXML()
    Main.filename_lbl.pack()
    Main.runButton.pack()
    Main.status_lbl.pack()
    
    print_c()
    
    Main.window.mainloop()
    s.close()

MainWindow()
