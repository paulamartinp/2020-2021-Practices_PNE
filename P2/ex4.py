from Client0 import Client

PRACTICE = 2
EXERCISE = 6
print(f"----|Practice {PRACTICE}, Exercise {EXERCISE}|----")

IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)

c.debug_talk("Message 1: This is my first message")
c.debug_talk("Message 2:  Testing...")