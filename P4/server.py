import socket
import termcolor
import pathlib
from urllib.parse import urlparse, parse_qs

# -- Favicon is the icon at the top left when searching
# -- T?name=Tyrosine&surname=Nucleotide we will have a dictionary with two keys because of the &

# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080
HTML_PATH = "./html/"


def read_html_file(filename):
    contents = pathlib.Path(filename).read_text()
    return contents


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    req_line = lines[0]                         # -- The request line is the first
    request = req_line.split(' ')[1]
    o = urlparse(request)
    path_name = o.path
    arguments = parse_qs(o.query)
    print("Resources requested: ", path_name)
    print("Parameters: ", arguments)            # -- Parameters are returned as a dictionary

    termcolor.cprint(req_line, "green")

    # -- Generate the response message
    # It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)


    body = read_html_file(HTML_PATH + "index.html")    # -- This new contents are written in HTML language
    status_line = "HTTP/1.1 200 OK\n"                  # -- Status line: We respond that everything is ok (200 code)

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"

    if path_name == "/":
        pass
    elif "/info/" in path_name:
        try:
            # -- Where is the letter? string.split('/')[-1] "A or G or C or T"
            body = read_html_file(HTML_PATH + path_name.split('/')[-1] + ".html")
        except FileNotFoundError:
            body = read_html_file(HTML_PATH + "errors.html")
    else:
        body = read_html_file(HTML_PATH + "errors.html")

    """if path_name == "/info/A":
        body = read_html_file(HTML_PATH + "A.html")
    elif path_name == "/info/C":
        body = read_html_file(HTML_PATH + "C.html")
    elif path_name == "/info/G":
        body = read_html_file(HTML_PATH + "G.html")
    elif path_name == "/info/T":
        body = read_html_file(HTML_PATH + "T.html")"""

    # -- Add the Content-Length
    header += f"Content-Length: {len(body)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


# -----MAIN PROGRAM------

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # -- Listening socket
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # -- Optional: This is for avoiding the problem of Port already in use
ls.bind((IP, PORT))                                        # -- Setup up the socket's IP and PORT
ls.listen()                                                # -- Become a listening socket
print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:
        process_client(cs)  # Service the client
        cs.close()          # -- Close the socket
