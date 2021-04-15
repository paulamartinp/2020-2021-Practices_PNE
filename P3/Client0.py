import socket
from termcolor import colored

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("Ok")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print("Server is up")
            s.close()
        except ConnectionRefusedError:
            print("Could not connect to the server. Is it running?. Have you checked the IP and the Port?")

    def __str__(self):
        return "Connection to SERVER at " + self.ip + ", PORT: " + str(self.port)


    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        print(msg)
        # Send data.
        s.send(str.encode(msg))
        # Receive data
        response = s.recv(2048).decode("utf-8")  # -- 2048 is the maximum number of characters we can receive
        # Close the socket
        s.close()
        # Return the response
        return response



    def debug_talk(self, msg):
        color_msg = colored(msg, "blue")
        response = self.talk(color_msg)
        print(colored(response, "yellow"))










