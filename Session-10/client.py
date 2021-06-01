from Client0 import Client

c = Client("127.0.0.1", 8080)
for i in range(0, 5):
    c.talk(str(i))


