import time
import threading
import socket
import os
import shutil

host='192.168.101.11' #client ip
port = 4005
server = ('192.168.101.10', 4000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))

def receive_req():
    data, addr = s.recvfrom(9999999999)
    data=data.decode('utf-8')
    if(data[0:4] == "run:"):
        print(data[0:3])
        print(data[4::])
        execute(data[4::])
        print("koniec")
        
    if(data[0:4] == "kil:"):
        print("kill")
        os.system("taskkill /im" + data[4::])
        
def download_prog(message):
    if(message !='q'):
        try:
            
            message = "snd:"+str(message)
            s.sendto(message.encode('utf-8'), server)
            
            data, addr = s.recvfrom(99999)
            file = open(message[4::], 'wb')
            file.write(bytes(data))
            file.close()
            print("odebrano")
            

        except:
            print("Brak połączenia")
            
##windows
def execute(prog_name):
    print("execute")
    if(os.path.exists(prog_name)):
        print("if")
    #       print(subprocess.check_output(prog_name, shell=True, text=True))
    #print(os.system('cmd /k "tescik.exe"'))
    else:
        download_prog(prog_name)
        time.sleep(2)
      #  if(os.path.exists(prog_name)):
     #          print(subprocess.check_output(prog_name, shell=True, text=True))

execute("unt.py")


