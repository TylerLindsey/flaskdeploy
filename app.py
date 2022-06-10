from flask import Flask, jsonify, request
from flask_cors import CORS
import sys

app = Flask(__name__)

# want to make an e3ndpoint for tweets
# we are breaking the rules below
tweets = [
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "10",
]

@app.get('/api/tweets')
def tweets_get():
  args = request.args
  #tweetId
  tweet_id = int(args.get('tweetId'))
  if tweet_id == None:
    return jsonify(tweets), 200
  else:
    return jsonify (tweets[tweet_id]), 200



if len(sys.argv) > 1:
  mode = sys.argv[1]
else:
  print('missing argument: testing|production')
  exit()
  
if mode == 'testing':
  from flask_cors import CORS
  CORS(app)
  app.run(debug=True)
elif mode == 'production':
  import bjoern
  print("TYLER you are running in PRODUCTION mode")
  bjoern.run(app, '0.0.0.0', 5000)
else:
  print('invalid mode, must be testing|production')
  exit()












