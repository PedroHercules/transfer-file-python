import socket
import tqdm
import os

# server IP address
SERVER_HOST = "10.180.42.246"
SERVER_PORT = 3333
BUFFER_SIZE = 4096
SEPARATOR = ";"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)

print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

client_socket, addr = server_socket.accept()
print(f"[+] {addr} is connected")

received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)

filename = os.path.basename(filename)
filesize = int(filesize)

progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename, "wb") as f:
  while True:
    # read 1024 bytes from the socket (receive)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:    
            # nothing is received
            # file transmitting is done
            break
        # write to the file the bytes we just received
        f.write(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))

client_socket.close()
server_socket.close()

