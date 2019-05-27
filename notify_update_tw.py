from requests_oauthlib import OAuth1Session
from linebot import LineBotApi
from linebot.models import TextSendMessage
from time import sleep
import json,sys,requests,conf
t_url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
#twitter request
old=0
params = {
'count' : 1,
'screen_name' : conf.t_user_id,
'exclude_replies' : "false",
'include_rts' : "false"
}

while True:
    twitter = OAuth1Session(conf.CK, conf.CS, conf.t_AT, conf.AS)
    req = twitter.get(t_url, params = params)
    if req.status_code == 200:
        timelines = json.loads(req.text)
        for lines in timelines:
            if old != lines["id"]:
                #post to LINE
                l = LineBotApi(conf.l_AT)
                messages = TextSendMessage(text=lines["text"]+"\n"
                                                +lines['created_at']+"\ntwitter.com/"
                                                +conf.t_user_id+"/status/"+lines["id_str"])
                l.push_message(conf.l_id, messages=messages)
                old = lines["id"]
    else:
        print ("Error: %d" % req.status_code)
    sleep(60)
