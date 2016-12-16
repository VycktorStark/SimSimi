#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib
import json
import os
from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)
key = ""
lang = ""
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    if req.get("result").get("action") != "ApiSimsimi":
        return {}
    baseurl = "http://api.simsimi.com/request.p?"
    texto_url = makeTextQuery(req)
    if texto_url is None:
        return {}
        if key is None:
            return "ERRO!"
        if lang is None:
            return "ERRO!"
    url = baseurl + urllib.urlencode({'text': texto_url.encode('utf8')}) + "&key=" + key + "&lc=" + lang + "&ft=2.3"
    result = urllib.urlopen(url).read()
    data = json.loads(result)
    res = makeWebhookResult(data)
    return res

def makeTextQuery(req):
    result = req.get("result")
    parameters = result.get("parameters")
    mentioned_text = parameters.get("any")
    if mentioned_text is None:
        return {}
    return "" + mentioned_text + ""

def makeWebhookResult(data):
    speech = data.get('response')
    erro = data.get('result')
    if (speech is None) or (erro is "404") or None:
        return {}
    mensagem = speech.encode('utf8')
    print("Response:", mensagem)
    return {
        "speech": mensagem,
        "displayText": mensagem,
        "source": "ApiSimsimi"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print "Starting app on port: %d" % port
    app.run(debug=False, port=port, host='0.0.0.0')
