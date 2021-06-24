import socket

def create_socket():
    try:
        global host
        global port
        global s
        host = "192.168.29.185"  # ip of the server
        port = 2110  # port no through which communication will take place
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating a socket
    except socket.error as msg:  # error message in case a socket can't be created
        print("Socket Creation Error:" + str(msg))
def socket_connect():
    global host
    global port
    global s
    s.connect((host,port)) # connecting to the socket
def send_receive():
    file = open("data.txt","r")   # opening the file in read mode
    data = file.read() # reading the data of the file
    s.send("data.txt".encode("utf-8"))  # encoding and sending the name of the file
    s.send(data.encode("utf-8"))   # encoding and sending the data of the file
    msg = s.recv(1024).decode("utf-8")  # receiving if the file has received by the server
    print("Response:" + msg )
    file.close()  # closing the file
    s.close()   # closing the socket

def main():
    create_socket()
    socket_connect()
    send_receive()

main()
