import time
import requests
import statistics
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

server_addr = os.getenv('IP_SERVER')

n_file = int(os.getenv('N_FILES'))
file_size = int(os.getenv('SIZE_FILES'))
send_rate = int(os.getenv('RATE'))

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
  res = requests.post(f"{server_addr}/files", files=files)
  t1 = time.time()
  time_res.append(t1 - t0)
  print(res.content)
  print(f"Tempo: {t1 - t0}")
  time.sleep(send_rate)

df = pd.DataFrame(time_res, columns=['tempo'])
df.to_csv(f'rate_{send_rate}_size_{file_size}.csv')
print(f"Tempo médio de resposta: {statistics.mean(time_res)}")
