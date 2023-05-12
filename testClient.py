import socket
import json

HOST = '127.0.0.1'
PORT = 1239

scores = [{'score': 100, 'date': '2023-05-07'},
          {'score': 90, 'date': '2023-05-08'},
          {'score': 80, 'date': '2023-01-07'},
          {'score': 70, 'date': '2023-11-07'},
          {'score': 100, 'date': '2023-03-15'}
         ]

newScore = {'score': 75, 'date': '2023-06-14'}

clientData = json.dumps({'scoreboard': scores, 'newScore': newScore}).encode('utf-8')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  s.sendall(clientData)
  scoreData = s.recv(1024)
newScores = scoreData.decode('utf-8')
print(f'new scores:{newScores}')  