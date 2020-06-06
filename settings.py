import lang, os, random
TR = lang.languages
LN = os.environ['LN']
SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY_SIMSIMI = os.environ['SECRET_KEY_SIMSIMI']
TELEGRAM_API = f'https://api.telegram.org/bot{SECRET_KEY}/setWebhook'
APISIMSIMI = 'http://api.simsimi.com/request.p'
ERROAPISIMSIMI = random.choice([
	'kié',
	'q foi',
	"SEU ARROMBADO FDP",
	'O que vc quer comigo me deixa em paz poha!!!',
	'POLICIA AQUI E SimSimi TEM UM CARA ME SAKEANDO SOCORU'])
MSGTERMINAL = "User {} with the id {}\nsend: {}\nresponse is: {}"
