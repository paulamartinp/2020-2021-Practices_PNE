from Client0 import Client
PRACTICE = 2
EXERCISE = 3
print(f"----|Practice {PRACTICE}, Exercise {EXERCISE}|----")

IP = "127.0.0.1"
PORT = 12000

c = Client(IP, PORT)
# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")
