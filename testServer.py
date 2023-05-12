import socket
import json

HOST = '127.0.0.1'
PORT = 1239

def updateLeaderboard(scores):
  #if new score < lowest score, return original leaderboard
  if scores['newScore']['score'] < scores['scoreboard'][4]['score']:
    return scores['scoreboard']
  #appends new score to leaderboard, sorts, and returns sorted list
  scores['scoreboard'].append(scores['newScore'])
  newList = sorted(scores['scoreboard'], key=lambda sc: sc['score'])
  newList.reverse()
  newList.pop()
  return newList

def startServer():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    data = conn.recv(1024)
    clientData = json.loads(data.decode('utf-8'))
    updatedBoard = updateLeaderboard(clientData)
    print(updatedBoard)
    response = json.dumps(updatedBoard).encode('utf-8')
    conn.sendall(response)
    print('sent server response')
    

startServer()