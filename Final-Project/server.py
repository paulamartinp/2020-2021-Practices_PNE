import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils as su

HUMAN_GENES = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362'
}
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

        context = {}
        if path_name == "/":
            context["list_genes"] = list(HUMAN_GENES.keys())
            contents = su.read_template_html_file("./html/index.html").render(context=context)
        elif path_name == "/listSpecies":
            contents = su.listSpecies(arguments)
            print(contents)
        elif path_name == "/karyotype":
            contents = su.karyotype(arguments, path_name)
            print(contents)
        elif path_name == "/chromosomeLength":
            contents = su.karyotype(arguments, path_name)
            print(contents)
        elif path_name == "/geneSeq":
            contents = su.gene_seq(arguments, path_name, HUMAN_GENES)
        elif path_name == "/geneInfo":
            contents = su.gene_seq(arguments, path_name, HUMAN_GENES)
        elif path_name == "/geneCalc":
            contents = su.gene_seq(arguments, path_name, HUMAN_GENES)

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


# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()