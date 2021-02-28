from socket import *

from pip._vendor.distlib.compat import raw_input

#def smtp_client(port=1025, mailserver='127.0.0.1'):
mailserver = ("127.0.0.1".encode(), 1025)
msg = "\r\n In computer networks!"
endmsg = "\r\n.\r\n"
#mailserver = 'smtp.nyu.edu'
#Mailport = 25  # Fill in end
#mailserver = ( "smtp.cs.nyu.edu", 25)

# Create socket called clientSocket and establish a TCP connection with mailserver
ClientSocket = socket(AF_INET, SOCK_STREAM)
   #Fill in end
#ClientSocket.connect((mailserver,Mailport))
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024)

print(recv)
if recv[:3] != '220':
    print('1:220 reply not received from server.')

# Send HELLO command and print server response.
helloCommand = 'HELO Alice\r\n'
clientSocket.sendall(helloCommand.encode())
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('2:250 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <sm9598@nyu.edu> \r\n"
clientSocket.sendall(mailFrom.encode())
recv2 = clientSocket.recv(1024)
print(recv2)
if recv1[:3] != '250':
    print('3:250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptTo = "RCPT TO: <sm9598@nyu.edu> \r\n"
clientSocket.sendall(rcptTo.encode())
recv3 = clientSocket.recv(1024)
print(recv3)
if recv1[:3] != '250':
    print('4:250 reply not received from server.')

# Send DATA command and print server response.
data = "DATA\r\n"
clientSocket.sendall(data.encode())
recv4 = clientSocket.recv(1024)
print(recv4)
if recv1[:3] != '250':
    print('5:250 reply not received from server.')

# Send message data.
subject = "Subject: SMTP mail client testing \r\n\r\n"
clientSocket.sendall(subject.encode())
#message = raw_input("Enter your message: \r\n")
clientSocket.sendall(msg.encode())
clientSocket.sendall(endmsg.encode())
recv_msg = clientSocket.recv(1024)
print("6:Response after sending message body:"+recv_msg.decode())
if recv1[:3] != '250':
    print('7:250 reply not received from server.')

# Send QUIT command and get server response.
clientSocket.sendall("QUIT\r\n".encode())
message=clientSocket.recv(1024)
print(message)
clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')