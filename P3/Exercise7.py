from Client0 import Client
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_2P"]
list_sequences = ["ACGTAAAGCGTTGCT", "CCCAAAGAACCCGC", "GATTTTCCCAATACTGGG", "TATGCCAACGGTT", "ACAAAGGGCTTACAGT"]

IP = "127.0.0.1"
PORT = 8081
client = Client(IP, PORT)

testing = True
while testing:
    print("\n" + "Type EXIT if you want to stop testing.")
    msg = input("What command do you want to test?: ")
    print("* Testing " + msg + "...")
    if msg == "PING":
        print(client.talk(msg))

    elif msg == "GET":
        for i in range(0, 5):
            print(client.talk(msg + " " + str(i)))

    elif msg == "INFO" or msg == "COMP" or msg == "REV":
        msg = msg + " " + list_sequences[0]  # -- Sequence corresponding to GET 0
        print(client.talk(msg))

    elif msg == "GENE":
        for i in gene_list:
            print(client.talk(msg + " " + str(i)))

    elif msg == "EXIT":
        print("The testing has stopped.")
        testing = False

    else:
        print("""ERROR. You need to introduce one of the following commands: 
                PING, GET, INFO, COMP, REV, or GENE""")
