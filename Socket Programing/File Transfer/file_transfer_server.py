import socket

def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 2110
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Socket Creation Error:" + str(msg))

def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding with port:" + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding error:" + str(msg))
        print("Retrying.........")
        bind_socket()

def socket_accept():
    received_word = ""
    while True:
        clt_soc, add = s.accept()
        print("Connection has been established:IP......." + add[0] + " and Port:" + str(add[-1]))
        receive_file(clt_soc)


def receive_file(clt_soc):
    filename = clt_soc.recv(1024).decode("utf-8")
    file = open(filename, "w")
    print(filename)
    data = clt_soc.recv(1024).decode("utf-8")
    file.write(data)
    clt_soc.send("File received.".encode("utf-8"))
    file.close()

if __name__ == '__main__':
    create_socket()
    bind_socket()
    socket_accept()
    clt_soc.close()