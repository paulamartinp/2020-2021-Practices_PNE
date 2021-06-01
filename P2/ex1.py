from Client0 import Client
PRACTICE = 2
EXERCISE = 1
print(f"----|Practice {PRACTICE}, Exercise {EXERCISE}|----")

#IP ALWAYS A STRING , AND THE PORT AN INTEGER
IP = "127.0.0.1"
PORT = 8081

c = Client(IP, PORT)
c.ping()
print("IP: " + str(c.ip) + "  Port: " + str(c.port))

