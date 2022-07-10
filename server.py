from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import codecs
import uuid

app = Flask(__name__)

auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')

cluster = Cluster(['127.0.0.1'], port=9042, auth_provider=auth_provider)
session = cluster.connect('store')

@app.route('/files', methods = ['POST'])
def upload_file():
  file = request.files['file']
  file_read = file.read()
  file64_encoded = codecs.encode(file_read, 'hex_codec')

  session.execute('USE store')

  id = uuid.uuid1()
  print(id)

  strCQL = "INSERT INTO server_file (id, file) VALUES (?,?)"
  pStatement = session.prepare(strCQL)
  session.execute(pStatement,[id,file64_encoded])

  return 'File uploaded successfully'


if __name__ == '__main__':
  app.run(debug = True)