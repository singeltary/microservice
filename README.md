To request data from the server:
1. Establish a TCP connection to the server running the microservice. The IP address is 127.0.0.1 and the port number is 1237

2. Microservice is set up to receive data in the format below, so please send as utf-8 encoded json
scores = {'leaderboard': [{'score': 100, 'date': '2023-05-07'},
{'score': 90, 'date': '2023-05-08'},
{'score': 80, 'date': '2023-01-07'},
{'score': 70, 'date': '2023-11-07'},
{'score': 60, 'date': '2023-03-15'}],
  
'new_score': {'score': 85, 'date': '2023-06-14'}}

3. The microservice will return a similarly encoded json of a list of dictionaries containing the new leaderboard:
[{'score': 100, 'date': '2023-05-07'},
{'score': 90, 'date': '2023-05-08'},
{'score': 80, 'date': '2023-01-07'},
{'score': 70, 'date': '2023-11-07'},
{'score': 60, 'date': '2023-03-15'}]

Example Python function using socket and json libraries:

clientData = json.dumps({'scoreboard': scores, 'newScore': newScore}).encode('utf-8')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  s.sendall(clientData)
  scoreData = s.recv(1024)
newScores = scoreData.decode('utf-8')
