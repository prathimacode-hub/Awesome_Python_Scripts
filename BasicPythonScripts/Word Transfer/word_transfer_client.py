import socket

def create_socket():
    try:
        global host
        global port
        global s
        host = "192.168.29.185"  # ip of the server
        port = 3603 # socket selected for transfer of information
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Socket Creation Error:" + str(msg))
def socket_connect():
    global host
    global port
    global s
    s.connect((host,port)) # to connect with the server
def send_receive():  # to input a word and send it to the server for checking
    word = input("Enter a word:")
    s.send(bytes(word, "utf-8")) # to send the word in form of bytes after encoding it
    complete_msg = ""
    while True:  # to receive the message sent back from the server
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
