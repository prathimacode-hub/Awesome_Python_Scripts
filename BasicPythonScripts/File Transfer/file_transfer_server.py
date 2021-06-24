import socket

def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 2110   # port no through which communication will take place
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating a socket
    except socket.error as msg:
        print("Socket Creation Error:" + str(msg))     # error message in case a socket can't be created

def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding with port:" + str(port))
        s.bind((host, port))   # to bind with the port
        s.listen(5)  # to listen to the client for information
    except socket.error as msg:    # error in case the socket could not be binded
        print("Socket Binding error:" + str(msg))
        print("Retrying.........")
        bind_socket()

def socket_accept():
    while True:
        clt_soc, add = s.accept()  # to accept the client socket and address
        # print the I/P and port no through which communication has been established
        print("Connection has been established:IP......." + add[0] + " and Port:" + str(add[-1]))
        receive_file(clt_soc)   # function to receive the file
        clt_soc.close()  # to close the socket after communication


def receive_file(clt_soc):
    filename = clt_soc.recv(1024).decode("utf-8")   # to receive file name and decode it
    file = open(filename, "w")   # to open a file with the received filename in write mode
    print(filename)   # to print the file name
    data = clt_soc.recv(1024).decode("utf-8")    # to receive the data of the file
    file.write(data)   # to write the contents of the file in the new file
    clt_soc.send("File received.".encode("utf-8"))  # to send that file has been received
    file.close()  # to close the file

if __name__ == '__main__':
    create_socket()
    bind_socket()
    socket_accept()