#!/usr/bin/env python

import os
from flask import Flask, request, abort, jsonify


app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        result = {
            "speech": "This is a test response from the web API, it worked!",
            "displayText": "This is the test response from the web API, in DisplayText form!",
            "source": "LoLWebhook"
        }
        print(request.json)
        return jsonify(result), 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run('0.0.0.0', port=port)
