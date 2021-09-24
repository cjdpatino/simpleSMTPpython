from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    message = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO ALICE\r\n'
    clientSocket.send(heloCommand.encode())
    recv_helo = clientSocket.recv(1024).decode()
    print(recv_helo)
    if recv_helo[:3] != '250':
        print('Helo 250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailCommand = "MAIL FROM: christiandpatino2@gmail.com\r\n"
    clientSocket.send(mailCommand.encode())
    recv_mail = clientSocket.recv(1024).decode()
    print(recv_mail)

    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    mailRcpt = "RCPT TO: christiandpatino@gmail.com\r\n"
    clientSocket.send(mailRcpt.encode())
    recv_rcpt = clientSocket.recv(1024).decode()
    print(recv_rcpt)
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    mailData = "DATA\r\n"
    clientSocket.send(mailData.encode())
    recv_data = clientSocket.recv(1024).decode()
    print(recv_data)
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(message.encode())
    recv_msg = clientSocket.recv(1024).decode()
    print(recv_msg)
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv_period = clientSocket.recv(1024).decode()
    print(recv_period)
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quit = "QUIT\r\n"
    clientSocket.sendall(quit.encode())
    recv_quit = clientSocket.recv(1024).decode()
    print(recv_quit)
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
