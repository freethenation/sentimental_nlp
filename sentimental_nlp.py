#!/usr/bin/env python
import re
import sys
import json
from waitress import serve
import fastText as fasttext
from flask import Flask, request, jsonify

model = fasttext.load_model('model.bin')
app = Flask(__name__)

def tokenize(line):
    line = re.sub(r'[,./<>?;:\"!@#$%^&*()=\[\]{}()]', ' ', line)
    line = re.sub(r'[ \t]{2,}', ' ', line).lower()
    line = re.sub(r'(.)\1\1+', r'\1\1\1', line)
    return line

def predict(line):
    line = tokenize(line)
    predict = model.predict(line)
    return {
        "labels":list(predict[0]),
        "scores":list(predict[1]),
    }

@app.route("/")
def handler():
    review = request.args.get('review')
    if not review:
        return jsonify({'error': 'Make a request with a "review" query parameter and '}), 400
    pre = predict(review)
    pre['review'] = review
    return jsonify(pre)

if __name__ == "__main__":
    if "server" in sys.argv:
        serve(app, host='127.0.0.1', port=3000)
    else:
        for line in sys.stdin.readlines():
            line = line.replace("\n","")
            pre = predict(line)
            pre['review'] = line
            print(json.dumps(pre))
