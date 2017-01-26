#!/usr/bin/env python
#-*- coding: utf-8 -*-
# encoding: utf-8
import json
from flask import flash, request, render_template, Flask, make_response
from config import *
from utils import *
from request import *
app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
	req = request.get_json(silent=True, force=True)
	print("Request:" + json.dumps(req, indent=4))
	res = processRequest(req)
	res = json.dumps(res, indent=4)
	r = make_response(res)
	r.headers['Content-Type'] = 'application/json'
	return r
def processRequest(req):
	if req.get("result").get("action") == "ApiSimsimi":
		texto = req.get("result").get("parameters").get("any").lower().encode('utf8')
		return {"speech": api(texto)}

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port: %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
