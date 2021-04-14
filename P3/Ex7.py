from Client0 import Client

PORT = 8081
IP = "127.0.0.1"

c = Client(IP, PORT)
print("* Testing PING...")
print(c.talk("PING"))

print("* Testing GET...")
for n in range(0,4):
    print(c.talk("GET " + str(n)))