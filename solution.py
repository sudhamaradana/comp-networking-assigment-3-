from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n I love computer networks!"
    endmsg = "\r\n.\r\n"


# server = "localhost"
server = '127.0.0.1'
port = 1025
emailFrom = "sm9598@nyu.edu"
emailTo = "sm9598@nyu.edu"

# Connect to the local host (an EECS server, where this code should be executed)
mailserver = (server, port)

# Create socket called clientSocket and establish a TCP connection with nailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
# Fill in end
recv = clientSocket.recv(1024).decode()
# print(recv)
# if recv[:3] != '220':
#    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
# print(recv1)
# if recv1[:3] != '250':
#    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
fromCommand = 'MAIL FROM:Sudha' + emailFrom + '\r\n'
clientSocket.send(fromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
# print(recv2)
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptCommand = 'RCPT TO: ' + emailTo + '\r\n'
clientSocket.send(rcptCommand.encode())
recv3 = clientSocket.recv(1024).decode()
# print(recv3)
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
# print(recv4)
# Fill in end

# Send message data.
# Fill in start
msg = "\r\n I love computer networks!"

clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
endmsg = "\r\n.\r\n"
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
# print(recv5)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
# print(recv6)
# Fill in end
if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
