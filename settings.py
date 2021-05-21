import lang, os

LN = os.environ['LN']
TR = lang.languages
Sudo_ID = 438131290

SimSimi = dict(url='http://api.simsimi.com/request.p', ft="2.3", lc='LN', text='Hi')
SimSimi['key']  = os.environ['SECRET_KEY_SIMSIMI']
ErroApiSimSimi = lang.erroapi

SECRET_KEY = os.environ['SECRET_KEY']
TELEGRAM_API = f'https://api.telegram.org/bot{SECRET_KEY}/setWebhook'
