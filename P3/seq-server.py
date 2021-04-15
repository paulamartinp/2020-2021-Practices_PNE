import socket
import server_utils

list_sequences = ["ACGTAAAGCGTTGCT", "CCCAAAGAACCCGC", "GATTTTCCCAATACTGGG", "TATGCCAACGGTT", "ACAAAGGGCTTACAGT"]
GENE_FOLDER = "./projects/"
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_2P"]

IP = "127.0.0.1"
PORT = 8081

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # -- Step 1: create the socket
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # -- For avoiding the problem of Port already in use
ls.bind((IP, PORT))                                       # -- Step 2: Bind the socket to server's IP and PORT
ls.listen()                                               # -- Step 3: Configure the socket for listening

print("The server is configured!")
count_connections = 0
client_address_list = []
while True:
    print("\n" + "Waiting for Clients to connect... ")
    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.append(client_ip_port)
        count_connections += 1
        print("CONNECTION " + str(count_connections) + ". Client IP, PORT: " + str(client_ip_port))
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        print("A client has connected to the server!")  # -- Execute this part if there are no errors

    msg_raw = cs.recv(2048)  # -- The received message is in raw bytes
    msg = msg_raw.decode()   # -- We decode it for converting it into a human-readeable string

    formatted_message = server_utils.format_command(msg)
    print(formatted_message)
    formatted_message = formatted_message.split(" ")

    if len(formatted_message) == 1:
        command = formatted_message[0]
    else:
        command = formatted_message[0]
        argument = formatted_message[1]

    if command == "PING":
        server_utils.ping(cs)

    elif command == "GET":
        server_utils.get(cs, list_sequences, argument)

    elif command == "INFO":
        server_utils.info(cs, argument)

    elif command == "COMP":
        server_utils.comp(cs, argument)

    elif command == "REV":
        server_utils.rev(cs, argument)

    elif command == "GENE":
        server_utils.gene(cs, argument, gene_list, GENE_FOLDER)

    else:
        response = "ERROR. Not Available Command"
        cs.send(str(response).encode())
        print(response)
    cs.close()  # -- Close the data socket
