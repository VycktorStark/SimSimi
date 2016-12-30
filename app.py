#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random, urllib, json, os
from flask import flash, request, render_template, Flask, make_response

app = Flask(__name__)
key = ""
lang = "pt"
error_msg = [""]
typeIA = "2.3"
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:" + json.dumps(req, indent=4) + "")
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    if req.get("result").get("action") != "ApiSimsimi":
        return {}
    baseurl = "http://api.simsimi.com/request.p?"
    texto_url = req.get("result").get("resolvedQuery")
    if texto_url is None:
        return {
            "speech": "ERROR BOT! " + random.choice(error_msg),
            "displayText": "ERROR BOT! " + random.choice(error_msg),
            "source": "ApiSimsimi"
        }
        if key is None:
            return {
                "speech": "ERROR BOT! Missing the key",
                "displayText": "ERROR BOT! Missing the key",
                "source": "ApiSimsimi"
            }
        if lang is None:
            return {
                "speech": "ERROR BOT! Missing the lang",
                "displayText": "ERROR BOT! Missing the lang",
                "source": "ApiSimsimi"
            }
    url = baseurl + urllib.urlencode({'text': texto_url.encode('utf8')}) + "&key=" + key + "&lc=" + lang + "&ft=" + typeIA + ""
    result = urllib.urlopen(url).read()
    data = json.loads(result)
    speech = data.get('response')
    erro = data.get('result')
    if (speech is None) or (erro is "404") or None:
        return {
            "speech": "ERROR BOT! " + random.choice(error_msg),
            "displayText": "ERROR BOT! " + random.choice(error_msg),
            "source": "ApiSimsimi"
        }
    mensagem = speech.encode('utf8')
    print("Response: " + mensagem + "")
    return {
        "speech": mensagem,
        "displayText": mensagem,
        "source": "ApiSimsimi"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port: %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
