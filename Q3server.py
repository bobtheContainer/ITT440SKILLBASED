import threading
import random
import socket
# Q3 SERVER
# s = server
quotes = ["Saya Give Up Q2", "Boleh connect dan dapat input", "Dapat reply dari sever conver farrenheit ke celcius","dah buat mcm2 jadi makin teruk","x terima int sbb can't bytes???","no idea"]

def handle_c(c_socket):
    quote = random.choice(quotes)
    c_socket.send(quote.encode())
    c_socket.close()

s = socket.socket()
s.bind(("",4444 ))
s.listen(5)

while True:
    c, addr = s.accept()
    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
    c_handler = threading.Thread(target=handle_c, args=(c,))
    c_handler.start()

