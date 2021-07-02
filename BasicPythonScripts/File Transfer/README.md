# Package/Script Name: File Transfer

## Short description of package/script

- For transfer of files between computers or between a windows or VM in a same computer
- It imports the library socket

## Setup instructions

- Need to switch off the local firewall in both the pcs
- To run the server in a VM or in a different computer and the client in the different computer and change the IP in the client folder based on the IP of the VM/Computer.

## Detailed explanation of script, if needed

A. Steps to create the socket program on word transfer from client to server with Ubuntu on VM as the server:
- While creating the server file on Ubuntu(file_transfer_server):
	- a. First created a socket
	- b. Took an arbitary port number greater than 1023(in this case it is 2110) for the transfer of infromation
	- c. Binded the ports of the client and server
	- d. Listened to the client for information
	- e. Received the file name from the client
	- f. Opened a file with the same filename in write mode
	- g. Received the contents of the file and wrote it on the new file
	- h. Sent that the file has been received
	- i. Ended the connection
- While creating the client file on Windows(word_transfer_client):
	- a. First created a socket
	- b. Took the same port number as in the server(in this case 3603)
	- c. Looked for the ip address in the Ubuntu on VM
	- d. Entered the ip address for connecting with the server
	- e. Sent the filename to the server
	- f. Sent the file contents to the server
	- g. Received the file sending result from the server
	- h. Displayed it to the client
	- i. Ended the connection

## Output

![Image](Images/file_transfer_client_ss.jpg)
![Image](Images/file_transfer_server_ss_1.jpg)
![Image](Images/file_transfer_server_ss_2.jpg)
## Author(s)

Kumarjeet Ray

## Disclaimers, if any

N/A
