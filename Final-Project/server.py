import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils as su


# Define the Server's port
PORT = 8080


# -- This is for preventing the errors: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):


    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters: ", arguments)


        if path_name == "/":
            contents = su.read_template_html_file("./html/index.html").render()
        elif path_name == "/listSpecies":
            contents = su.listSpecies(arguments)
            print(contents)
        elif path_name == "/karyotype":
            contents = su.karyotype(arguments)
            print(contents)
        elif path_name == "/chromosomeLength":
            contents = su.chromosome_length(arguments)

        else:
            contents = su.read_template_html_file("html/errors/error.html").render()


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html') # Si no ponemos html saldrá texto!!
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return



# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()