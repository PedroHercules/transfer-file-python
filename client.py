# Fazer modificações nesta branch
import socket
import tqdm
import os

SEPARATOR = ";"
BUFFER_SIZE = 4096
filename = "data.csv"
filesize = os.path.getsize(filename)

host = "10.180.42.246"
port = 3333

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    #s.sendto(b"Hello", (host, port))  
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
    # close the socket
    s.close()
    teste = s.recv(1024)  
    print(teste)