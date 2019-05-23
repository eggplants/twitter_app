from requests_oauthlib import OAuth1Session
from linebot import LineBotApi
from linebot.models import TextSendMessage,ImageSendMessage
from time import sleep
import conf,json,sys,requests
###this program is....
#####to detect update of user(RT,tweet)
#####then, notify line talk room
#####if the tweet contains a img, it sends there
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
    req_2 = twitter.get(t_url, params = params)
    if req_2.status_code == 200:
        timelines = json.loads(req_2.text)
        for lines in timelines:
            if old < lines["id"]:
                #post to LINE
                print(lines["id"])
                l = LineBotApi(conf.l_AT)
                messages = TextSendMessage(text=lines["text"]+"\n"
                                                +lines['created_at']+"\n"
                                                +"twitter.com/"+conf.t_user_id+"/status/"+lines["id_str"])
                l.push_message(conf.l_id, messages=messages)
                #with image
                try:
                    messages=ImageSendMessage(
                        original_content_url=lines["extended_entities"]["media"][0]["media_url_https"],
                        preview_image_url=lines["extended_entities"]["media"][0]["media_url_https"])
                    l.push_message(conf.l_id, messages=messages)
                except KeyError:
                        print("keyerror")
                old = lines["id"]
    else:
        print ("Error: %d" % req.status_code)
    sleep(10)
