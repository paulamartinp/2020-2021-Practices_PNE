from Client0 import Client
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_2P"]

IP = "127.0.0.1"
PORT = 8080

client = Client(IP, PORT)

msg = input("Enter here the command tou want to test: ")
print("* Testing " + msg + "...")

if msg == "PING":
    print(client.talk(msg))

elif msg == "GET":
    for i in range(0, 5):
        print(client.talk(msg + " " + str(i)))

elif msg == "INFO" or msg == "COMP" or msg == "REV":
    msg = msg + " ACGTAAAGCGTTGCT"
    print(client.talk(msg))

elif msg == "GENE":
    for i in gene_list:
        print(client.talk(msg + " " + str(i)))
else:
    print("""ERROR. You need to introduce one of the following commands: 
            PING, GET, INFO, COMP, REV, or GENE""")

