import socket

def create_socket():
    try:
        global host
        global port
        global s
        host = "192.168.29.185"  # ip of the server
        port = 2110
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Socket Creation Error:" + str(msg))
def socket_connect():
    global host
    global port
    global s
    s.connect((host,port))
def send_receive():
    file = open("data.txt","r")
    data = file.read()
    s.send("data.txt".encode("utf-8"))
    s.send(data.encode("utf-8"))
    msg = s.recv(1024).decode("utf-8")
    print("Response:" + msg )
    file.close()
    s.close()

def main():
    create_socket()
    socket_connect()
    send_receive()

main()
