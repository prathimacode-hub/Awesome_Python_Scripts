from words import words
import socket


def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 2110 #port selected for transfer of information
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Socket Creation Error:" + str(msg)) # Error message in case socket can't be created


def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding with port:" + str(port)) 
        s.bind((host, port)) # to bind with the socket using the port no
        s.listen(5) # to listen to the client for receiving information
    except socket.error as msg:
        print("Socket Binding error:" + str(msg)) # error in case of problem in binding
        print("Retrying.........")
        bind_socket()


def socket_accept():
    clt_soc, add = s.accept() # receive client socket and address
    print("Connection has been established:IP......." + add[0] + " and Port:" + str(add[-1]))
    received_word = clt_soc.recv(1024) # receive the word sent by client in form of bytes
    received_word = received_word.decode("utf-8") # to decode the word from bytes to text
    print("Word Received:" + received_word) #print the received word
    check_word(received_word, clt_soc) # to check if the word is present in the list
    clt_soc.close() # close the socket after communication


def check_word(received_word, clt_soc):
    flag = 0
    for word in words:
        if word == received_word:
            flag = 1
            break
    if flag == 0:
        clt_soc.send(bytes("Word not found in the list.", "utf-8")) # to send back to client in case word is found
    else:
        clt_soc.send(bytes("Word found in the list.", "utf-8")) # to send back to client in case word is not found



def main():
    create_socket()
    bind_socket()
    socket_accept()

if __name__ == '__main__':
    main()
