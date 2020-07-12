from flask import Flask, jsonify, request
from flask_cors import CORS

import wlserve

app = Flask(__name__)
CORS(app)


from wlserve import games

@app.route('/ping')
def ping():
    return jsonify({"message":"Pong!"})

@app.route('/games')
def games():
    return jsonify(wlserve.games)

@app.route('/play')
def play():
    letters = request.args.get('l')
    lang = request.args.get('lang')
    start = request.args.get('start')
    end = request.args.get('end')
    return jsonify(wlserve.run(letters,lang,start,end))


if __name__=="__main__":
    app.run(debug=True, port=4000)