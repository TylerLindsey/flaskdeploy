from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
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

















