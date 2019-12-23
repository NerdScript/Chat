ip = "" #127.0.0.1
port = 443

s = socket.socket(AF_INET, SOCK_STREAM)

s.bind((ip, port))
s.listen(1)

while True:
    
