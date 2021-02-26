from socket import *
import smtplib

from pip._vendor.distlib.compat import raw_input


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My testing computer networking message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver = smtplib.SMTP("smtp.gmail.com", 587)
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)

    # Fill in start
    # Fill in end
    #rcptTo = "RCPT TO: <destination12(at the rate) xyz(dot)com> \r\n"
    clientSocket.send(AF_INET , SOCK_STREAM)
    recv = clientSocket.recv(1024).decode()
    ##print(recv)
    #if recv[:3] != '220':
        ##print('220 reply not received from server.')
    #elif recv[:3] == "220":
        ##print("Success")

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        ##print('250 reply not received from server.')

    # # Info for username and password
    # username = "abc@example.com"  # the username for your server
    # password = "pswd"  # the password for your server, changed here
    # base64_str = ("\x00" + username + "\x00" + password).encode()
    # base64_str = base64.b64encode(base64_str)
    # authMsg = "AUTH PLAIN ".encode() + base64_str + "\r\n".encode()
    # clientSocket.send(authMsg)
    # recv_auth = clientSocket.recv(1024)
    # print(recv_auth.decode())
    # if recv1[:3] != '250':
    #     print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFrom = "MAIL FROM: <anyemailid@gmail.com> \r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(b'After MAIL FROM command: ' + recv2)
    ##print(recv2)
    #if recv1[:3] != '250':
        ##print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptTo = "RCPT TO: <destination@gmail.com> \r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(b"After RCPT TO command: " + recv3)
    ##print(recv3)
    #if recv1[:3] != '250':
        ##print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)
    ##print(b"After DATA command: " + recv4)
    #if recv1[:3] != '250':
        ##print('250 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    subject = "Subject: SMTP mail client testing \r\n\r\n"
    clientSocket.send(subject.encode())
    #message = raw_input("Enter your message: \r\n")
    #clientSocket.send(message.encode())
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024).decode()
    #print("Response after sending message body:" + recv_msg.decode())
    ##print(recv_msg)
    #if recv1[:3] != '250':
        ##print('250 reply not received from server.')
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    ailMessageEnd = '\r\n.\r\n'
    #clientSocket.send(message + mailMessageEnd)
    clientSocket.send(endmsg.encode())
    recv6 = clientSocket.recv(1024).decode()
    ##print(recv6)
    #if recv6[:3] != '250':
        ##print('250 reply not received from server.')

    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    clientSocket.send("QUIT\r\n".encode())
    message = clientSocket.recv(1024)
    ##print(message)
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')