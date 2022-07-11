import time
import requests
import statistics


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

time_res = []

for filename in filesnames:
  files = {"file": (filename, open(filename, "rb"))}
  t0 = time.time()
  res = requests.post("http://localhost:5000/files", files=files)
  t1 = time.time()
  time_res.append(t1 - t0)
  print(res.content)
  print(f"Tempo: {t1 - t0}")
  time.sleep(send_rate)
print(f"Tempo médio de resposta: {statistics.mean(time_res)}")
