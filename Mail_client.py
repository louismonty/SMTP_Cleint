from socket import *
import base64

img = open("/zhome/87/3/155927/Desktop/tesxat/me.jpg", "rb")
encoded_string = base64.b64encode(img.read())




msg = encoded_string
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("127.0.0.1" ,25)
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(mailserver)
#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n' # EHLO for extended SMTP
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
 print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
#mailFromComand= 'MAIL FROM:<s195469@student.dtu.dk>\r\n'
mailFromComand= 'MAIL FROM:<s205424@student.dtu.dk>\r\n'
clientSocket.send(mailFromComand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
 print('250 reply not received from server.')
# Send RCPT TO command and print server response.
rcptToComand= 'RCPT TO:<s205424@student.dtu.dk>\r\n'
clientSocket.send(rcptToComand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
 print('250 reply not received from server.')
# Send DATA command and print server response.
dataComand= 'DATA\r\n'
clientSocket.send(dataComand.encode())


recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '250':
 print('250 reply not received from server.')
# Send message data.
# Fill in start

clientSocket.send("MIME-Version: 1.0\r\n".encode())
clientSocket.send("subject: Finallyy!!\r\n".encode())
#clientSocket.send("FROM: s195469@student.dtu.dk\r \n".encode())
clientSocket.send("FROM: s205424@student.dtu.dk\r\n".encode())
clientSocket.send("TO: s205424@student.dtu.dk\r\n".encode())
clientSocket.send('Content-Type: multipart/related; boundary="frontier"\r\n'.encode())
clientSocket.send("--frontier\r\n".encode())
clientSocket.send('Content-type: text/html; charset=utf-8"\r\n'.encode())
clientSocket.send('\r \n <html><body><div>Finally got the picture to work <img src="cid:me" alt = "test"/></div></body></html>\r \n'.encode())
clientSocket.send("--frontier\r\n".encode())
clientSocket.send('Content-Type: image/jpeg; name = "me.jpg" \r\n'.encode())
clientSocket.send('Content-Disposition:  attachment; filename = "me.jpg" \r\n'.encode())
clientSocket.send('Content-Transfer-Encoding: base64 \r\n'.encode())
clientSocket.send('Content-ID: <me> \r\n'.encode())
clientSocket.send("\r \n ".encode()+encoded_string)
clientSocket.send("--frontier\r\n".encode())
clientSocket.send("--frontier--\r\n".encode())




clientSocket.send(endmsg.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '250':
 print('250 reply not received from server.')
# Fill in end

# Fill in end
# Message ends with a single period.
# Fill in start


# Send QUIT command and get server response.
# Fill in start
dataComand= 'QUIT\r\n'
clientSocket.send(dataComand.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
if recv7[:3] != '250':
 print('250 reply not received from server.')
# Fill in end