import flask, os, json, requests, re, random, time
app = flask.Flask(__name__)
app.config.from_object('settings')
cfg = app.config
def timeatual(self):
    return int((time.time()-self)/60)

def convbot(msgtext="OI", ln=cfg['LN']):
    result = requests.get(cfg['APISIMSIMI'],
        params=dict(lc=ln, text=msgtext, ft= "2.3",
        key= cfg['SECRET_KEY_SIMSIMI'])).json()
    if result["result"] == 100:
        return result["response"]
    else:
        return cfg['ERROAPISIMSIMI']
