from requests_oauthlib import OAuth1Session
from linebot import LineBotApi
from linebot.models import TextSendMessage
from time import sleep
import conf,json,sys,requests,random
def retrieve(url,s):
    max=""
    params = {
    'count' : 200,
    'screen_name' : conf.t_user_id
    }
    for i in range(0,10**19):
        dame=False
        if i != 0:
            params['max_id'] = max
        res = s.get(url, params = params)
        if res.status_code == 200:
            timelines = json.loads(res.text)
            idlist = []
            for lines in timelines:
                idlist.append(lines["id"])
                dame=True
            max=id-1
        else:
            print ("Error: %d" % req.status_code)
        if not dame:
            break
    return idlist,int(idlist/2)

def del_twe(id_twe,s):
    url="https://api.twitter.com/1.1/statuses/destroy/"+str(id)+".json"
    params = {
    "trim_user" : "false"
    }
    res = s.post(url, params = params)

def del_fav(id_fav,s):
    url="https://api.twitter.com/1.1/favorites/destroy.json"
    params = {
    "id" : id_fav,
    "include_entities" : "false"
    }
    res = s.post(url, params = params)

def notify_line(seed,result):
    l = LineBotApi(conf.l_AT)
    messages = TextSendMessage(
    text="seedは"+seed+"でした.\nよって,"+result+"."
    )
    l.push_message(conf.l_id, messages=messages)

def del_fav_hal(list_fav,s):
    for id in list_fav[0][list_fav[1]:]:
        del_fav(id,s)
    return "いいね半消し"

def del_fav_all(list_fav,s):
    for id in list_fav[0]:
        del_fav(id,s)
    return "いいね全消し"

def del_twe_hal(list_twe,s):
    for id in list_twe[0][list_twe[1]:]
    return "つぶやき半消し"

def del_twe_all(list_twe,s):
    for id in list_twe:
        del_twe(id,s)
    return "つぶやき全消し"

def del_nothing():
    return "なにもなし"

while True:
    result="いいね・つぶやき全消し"
    sleep(86400)
    twitter = OAuth1Session(conf.CK, conf.CS, conf.t_AT, conf.AS)
    url = "https://api.twitter.com/1.1/favorites/list.json"
    list_fav=retrieve(url,twitter)
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    list_twe=retrieve(url,twitter)
    seed=random.randrange(100)
    if seed in range(0,30):
        result=del_fav_hal(list_fav,twitter)
    elif seed in range(30,55):
        result=del_fav_all(list_fav,twitter)
    elif seed in range(55,65):
        result=del_twe_hal(list_twe,twitter)
    elif seed in range(65,70):
        result=del_twe_all(list_twe,twitter)
    elif seed in range(70,99):
        result=del_nothing()
    else:
        del_fav_all(list_fav,twitter)
        del_twe_all(list_twe,twitter)

    notify_line(seed,result)