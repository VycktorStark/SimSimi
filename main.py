from tools import flask, convbot, timeatual, cfg, app, os, requests, json, random
@app.errorhandler(404)
def server_error(e):
	return flask.Response(status=200)

@app.before_request
def handler():
	if (flask.request.method == 'GET') and (flask.request.path == "/start"):
		r = requests.get(cfg['TELEGRAM_API'],params=dict(url = f"{flask.request.host}/webhook", 
			max_connections = int(1), allowed_updates = "message"))
		return flask.Response(response=r.json()['description'], status=200)
	
	elif (flask.request.method == 'POST') and (flask.request.path == "/webhook"):
		msg = flask.request.get_json(silent=True, force=True)
		if not ('message' in msg):
			return flask.Response(status=200)
		else:
			msg = msg['message']
			if (timeatual(msg['date']) > int(10)): 
				return flask.Response(status=200)
			if (msg['chat']['type'] != 'private'):
				return flask.Response(response=json.dumps(dict(method='leaveChat', 
																chat_id=msg['chat']['id'])), 
																headers={'Content-Type':'application/json'},
																status=200)
			if ("language_code" in  msg['from']): cfg['LN'] = msg['from']['language_code'][:2]
			if ('text' in msg):
				cmd, ln = msg['text'].replace('/','').lower().split(), cfg['LN']
				params = dict(method ='sendMessage', 
							text = cfg['ERROAPISIMSIMI'], 
							chat_id = msg['chat']['id'],
							reply_to_message_id  = msg['message_id'], parse_mode =  "HTML")
				if ("entities" in msg):
					if ("bot_command" in msg['entities'][0]['type']):
						if ('help' in cmd) or ('start' in cmd): 
							params['text'] = cfg['TR'][ln][0]['start']
						elif ('about' in cmd):
							params['text'] = cfg['TR'][ln][0]['about']
						elif ('ping' in cmd):
							params['text'] = 'pong'
						elif ('/IA' == msg['text']):
							params['text'] = cfg['TR'][ln][0]['notcmdia']
					else:
						params['text'] = convbot(msgtext=msg['text'],ln=ln)
				else:
					params['text'] = convbot(msgtext=msg['text'],ln=ln)
				if ("username"in msg['from']):
					print(msg['from']['username'])
				print(cfg['MSGTERMINAL'].format(msg['from']['first_name'],msg['from']['id'],msg['text'],params['text']))
				return flask.Response(response=json.dumps(params), headers={'Content-Type':'application/json'},status=200)
			else:
				return flask.Response(status=200)
			
if __name__ == '__main__':
	app.run(debug=True, port=int(os.getenv('PORT', 3000)), host='0.0.0.0')
