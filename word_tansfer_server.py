from words import words
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
    clt_soc, add = s.accept()
    print("Connection has been established:IP......." + add[0] + " and Port:" + str(add[-1]))
    received_word = clt_soc.recv(1024)
    received_word = received_word.decode("utf-8")
    print("Word Received:" + received_word)
    check_word(received_word, clt_soc)
    clt_soc.close()


def check_word(received_word, clt_soc):
    flag = 0
    for word in words:
        if word == received_word:
            flag = 1
            break
    if flag == 0:
        clt_soc.send(bytes("Word not found in the list.", "utf-8"))
    else:
        clt_soc.send(bytes("Word found in the list.", "utf-8"))



def main():
    create_socket()
    bind_socket()
    socket_accept()

if __name__ == '__main__':
    main()