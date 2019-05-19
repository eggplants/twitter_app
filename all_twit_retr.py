from requests_oauthlib import OAuth1Session
import json
import conf
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
twit=200
max=""
for ii in range(0,10**19):
    dame=False
    if ii == 0:
        params = {
        'count' : twit,
        'screen_name' : conf.t_user_id
        }
    else:
        params = {
        'count' : twit,
        'screen_name' : conf.t_user_id,
        'max_id' : max
        }
    twitter = OAuth1Session(conf.CK, conf.CS, conf.AT, conf.AS)
    req = twitter.get(url, params = params)
    if req.status_code == 200:
        timelines = json.loads(req.text)
        i=1
        for line in timelines:
            print(i+ii*twit)
            print(line['text'])
            print(line['created_at'])
            id=int(line['id'])
            i+=1
            dame=True
        max=id-1
    else:
        print ("Error: %d" % req.status_code)
    if not dame:
        break