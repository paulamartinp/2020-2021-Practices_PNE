
def print_colored(message, color):
    import termcolor
    print(termcolor.colored(message, color))


def format_command(command):
    return command.replace("\n", "").replace("\r", "")


def ping():
    print_colored("PING command!", "green")

def get(cs, list_sequences, argument):
    print_colored("GET", "yellow")
    response = list_sequences[int(argument)]
    print(response)
    cs.send(response.encode())


