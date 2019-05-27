from requests_oauthlib import OAuth1Session
import json,csv,datetime
import conf
###this program is....
#####to get all user's tweet_ids
#####then, export to csv(seqnum,tweet_content,postdate)
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
twit=200
max=""
csvname=conf.t_user_id+"_all_tweet_"+str(datetime.datetime.today().strftime("%Y%m%d%H%M%S"))+".csv"
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
    twitter = OAuth1Session(conf.CK, conf.CS, conf.t_AT, conf.AS)
    # req_1 = twitter.post(url, params = params)
    req_2 = twitter.get(url, params = params)
    if req_2.status_code == 200:
        timelines = json.loads(req_2.text)
        i=1
        with open(csvname, 'a') as f:
                writer = csv.writer(f)
                for line in timelines:
                    writer.writerow([
                    # i+ii*twit,          #seqnum
                    line['text']     #tweet_content
                    # line['created_at']
                    ])
                    id=int(line['id'])
                    i+=1
                    dame=True
        max=id-1
    else:
        print ("Error: %d" % req_2.status_code)
    if not dame:
        break