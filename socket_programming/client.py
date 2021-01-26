import socket
import threading

nickname = input("choose nick name")
client = socket.socket()
host = socket.gethostname()
port = 55555
client.connect((host,port))

def receive():
        while True:
                try:
 
                        message = client.recv(1024).decode('ascii')
                        if message == 'NICK':
                                client.send(nickname.encode('ascii'))


                        else:
                                print(message)
                        
                        
                       
                except:
                        print("an error occured")
                        client.close()
                        break
                        
def write():
        while True:
                message = f'{nickname}: {input("")}'
                client.send(message.encode('ascii'))

receive_thread = threading.Thread(target = receive)
receive_thread.start()
write_thread = threading.Thread(target = write)
write_thread.start()



