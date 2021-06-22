B. Steps to create the socket program on file transfer from client to server with Ubuntu on VM as the server:
1. First created a text file named data.txt with some information
2. Kept the file in the same directory as the client
3. While creating the server file on Ubuntu(file_transfer_server):
	a. First created a socket
	b. Took an arbitary port number greater than 1023(in this case 2110) for the transfer of infromation
	c. Binded the ports of the client and server
	d. Listened to the client for information
	e. Received the file name from the client
	f. Created a file with the same file name as it was there in the client location and opened it in write mode
	g. Received the data from the client present in the file and wrote the data in the new file
	h. Wrote back to the client about the receival of the file
	h. Ended the connection
4. While creating the client file on Windows(file_transfer_client):
	a. First created a socket
	b. Took the same port number as in the server(in this case 2110)
	c. Looked for the ip address in the Ubuntu on VM
	d. Entered the ip address for connecting with the server
	e. Took the file from the client
	f. Opened the file in read mode
	g. Sent the file name to the server
	h. Sent the file information to the server
	i. Received the response from the server regarding the file
	j. Displayed it to the user
	k. Connection closed

