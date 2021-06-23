import socket

def create_socket():
    try:
        global host
        global port
        global s
        host = "192.168.29.185"  # ip of the server
        port = 3603
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Socket Creation Error:" + str(msg))
def socket_connect():
    global host
    global port
    global s
    s.connect((host,port))
def send_receive():
    word = input("Enter a word:")
    s.send(bytes(word, "utf-8"))
    complete_msg = ""
    while True:
        msg = s.recv(8)
        if len(msg) <= 0:
            break
        complete_msg += msg.decode("utf-8")
    print(complete_msg)
def main():
    create_socket()
    socket_connect()
    send_receive()
if __name__ == '__main__':
    main()