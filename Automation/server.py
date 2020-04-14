from ncclient import manager
import xmltodict
import socket
import json

def connect(node):
    try:
        m = manager.connect(host = node, port = '8181', username = 'admin', password = 'Admin_1234!', hostkey_verify = False)
        return m
    except:
        print("Unable to connect " + node)


def Main():
        host = "127.0.0.1"
        port = 5000

        mySocket = socket.socket()
        mySocket.bind((host, port))

        mySocket.listen(5)
        conn, addr = mySocket.accept()
        print ("Connection from: " + str(addr))
        while True:
                message = conn.recv(1024).decode()
                if message:
                        message = "Hello"
                else:
                        break
                conn.send(message.encode())
        conn.close()

if __name__ == '__main__':
        Main()
