from ncclient import manager
import xml.dom.minidom
import socket

node = "sbx-nxos-mgmt.cisco.com"

def connect(node):
    try:
        device_connection = manager.connect(host = node, port = '8181', username = 'admin', password = 'Admin_1234!', hostkey_verify = False, device_params={'name':'nexus'})
        return device_connection
    except:
        print("Unable to connect " + node)

def getHostname(node):
    device_connection = connect(node)
    hostname = """
               <show xmlns="http://www.cisco.com/nxos:1.0">
                   <hostname>
                   </hostname>
               </show>
               """
    try:
        netconf_output = device_connection.get(('subtree', hostname))
        print(netconf_output)
        xml_doc = xml.dom.minidom.parseString(netconf_output.xml)
        hostname = xml_doc.getElementsByTagName("mod:hostname")
        return "Hostname: "+str(hostname[0].firstChild.nodeValue)
    except:
        print("Unable to get the hostname!")

def getVersion(node):
    try:
        device_connection = connect(node)
        version = """
            <show xmlns="http://www.cisco.com/nxos:1.0">
                <version>
                </version>
            </show>
            """
        netconf_output = device_connection.get(('subtree', version))
        print(netconf_output)
        xml_doc = xml.dom.minidom.parseString(netconf_output.xml)
        version = xml_doc.getElementsByTagName("mod:kickstart_ver_str")
        return "Version: "+str(version[0].firstChild.nodeValue)
    except:
        print("Unable to get this node version")


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
        if message == "show hostname":
                message = getHostname(node)
        elif message == "show version":
                message = getVersion(node)
        elif message == "change hostname":
                newHostname = input("Enter your new hostname: ")
                change(node, newHostname)
        else:
                message = "I do not understand"
        conn.send(message.encode())
    conn.close()

if __name__ == '__main__':
        Main()
