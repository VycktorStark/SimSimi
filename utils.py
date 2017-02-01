from config import *
from utils import *
from request import *
import random, json
def api(self):
    url_api = config.Simi_API
    params = {}
    params['text'] = self
    params['key'] = config.key
    params['lc'] = config.lang
    params['ft'] = config.typeIA
    res_obj, res_str = request_json(url=url_api, params=params)
    if not res_str:
        return random.choice(config.error_msg)
    return res_obj.response.encode('utf8')
