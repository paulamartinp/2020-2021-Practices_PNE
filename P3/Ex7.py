from Client0 import Client
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_2P"]

PORT = 8081
IP = "127.0.0.1"

c = Client(IP, PORT)
print("* Testing PING...")
print(c.talk("PING"))

print("* Testing GET...")
for n in range(0,4):
    print(c.talk("GET " + str(n)))


print("* Testing INFO...")
print(c.talk("INFO" + " AAACCGCGCTTT"))

print("* Testing COMP...")
print(c.talk("COMP" + " AAACCGCGCTTT"))

print("* Testing REV...")
print(c.talk("REV" + " AAACCGCGCTTT"))

print("* Testing GENE...")
for gene in range(0, len(gene_list)):
    print(c.talk("GENE " + gene_list[gene]))
