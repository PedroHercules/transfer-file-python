import time
import requests


n_file = int(input('Informe a numero de arquivos\n'))
file_size = int(input('Informe o tamanho dos arquivos em MB\n'))
send_rate = int(input('Informe a taxa de envio em segundos\n'))

filesnames = []

for i in range(n_file):
  filename = 'file_'+str(i)+'.txt'
  with open(filename, 'wb') as f:
    num_chars = 1024 * 1024 * file_size
    f.write(b'0' * num_chars)
  filesnames.append(filename)

for filename in filesnames:
  files = {"file": (filename, open(filename, "rb"))}
  res = requests.post("http://localhost:5000/files", files=files)
  print(res.content)
  time.sleep(send_rate)
