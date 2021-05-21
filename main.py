from tools import convbot, RespFlask, RespTG
import requests, random, flask, json, re, os
app = flask.Flask(__name__)
app.config.from_object('settings')
cfg = app.config


@app.errorhandler(404)
def server_error(e):
	return RespFlask(status=200)

@app.before_request
def handler():
	if (flask.request.method == 'GET') and (flask.request.path == "/start"):
		r = requests.get(cfg['TELEGRAM_API'],params={
				"url": f"{flask.request.host}/webhook",
				'max_connections': 1,
				"allowed_updates": ["message"]
			}).json()
		return RespFlask(response=r['description'], status=200)

	elif (flask.request.method == 'POST') and (flask.request.path == "/webhook"):
		msg = flask.request.get_json(silent=True, force=True)
		if not ('message' in msg):
			return RespFlask(status=200)
		else:
			msg, ln = msg['message'], cfg['LN']
			if (msg['chat']['type'] != 'private'):
				RespFlask(response=RespTG(method='leaveChat', chat_id=msg['chat']['id']))
			if ("language_code" in  msg['from']):
				ln = msg['from']['language_code'][:2]
			if ('text' in msg):
				cmd = msg['text'].replace('/','').lower().split()
				if ("entities" in msg):
					if ("bot_command" in msg['entities'][0]['type']):
						print(cmd)
						if ('help' in cmd) or ('start' in cmd): 
							__text__ = cfg['TR'][ln][0]['start']
						elif ('about' in cmd):
							__text__ = cfg['TR'][ln][0]['about']
						elif ('ping' in cmd):
							__text__ = 'pong'
					else:
						__text__ = convbot(msgtext=msg['text'],LN=ln)
				else:
					__text__ = convbot(msgtext=msg['text'],LN=ln)
				return RespFlask(response=RespTG(method='sendMessage', chat_id=msg['chat']['id'], text=__text__, reply_to_message_id  = msg['message_id']))
			else:
				return RespFlask(status=200)
			
if __name__ == '__main__':
	app.run(debug=True, port=int(os.getenv('PORT', 3000)), host='0.0.0.0')
