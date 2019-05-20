###############
#require "conf.py":
#CK         twitter consumer key
#CS         twitter consumer sec
#t_AT       twitter access token
#AS         twitter access sec
#l_AT       line access token
#l_id       line talkroom id
#t_user_id  terget user id("screen_name")
###############
import json,sys,random,time,urllib.request,os,csv

import requests,schedule
from requests_oauthlib import OAuth1Session
from linebot import LineBotApi
from linebot.models import TextSendMessage

import conf
#get favs or tweets data
def retrieve(url,session):
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
#IDEA:
#lookup wheter tweet contains image(tweet_id)(return url_list)
#CSV export(session,name)
#schedule func using higher-order function(func,time)
#download from url(url,savepath=os.getcwd())
#delete tweet every tweet_id
def del_twe(id_twe,session):
    url="https://api.twitter.com/1.1/statuses/destroy/"+str(id_twe)+".json"
    params = {
    "trim_user" : "false"
    }
    res = s.post(url, params = params)
#delete favorite every favorite_id
def del_fav(id_fav,session):
    url="https://api.twitter.com/1.1/favorites/destroy.json"
    params = {
    "id" : id_fav,
    "include_entities" : "false"
    }
    res = s.post(url, params = params)
#notify to line room
def notify_line(seed,result,message):
    l = LineBotApi(conf.l_AT)
    messages = TextSendMessage(
    text="message"
    )
    l.push_message(conf.l_id, messages=messages)
#delete half of favorites
def del_fav_hal(list_fav,session):
    for id in list_fav[0][list_fav[1]:]:
        del_fav(id,session)
    return "いいね半消し"
#delete favorites all
def del_fav_all(list_fav,session):
    for id in list_fav[0]:
        del_fav(id,session)
#delete half of tweets
def del_twe_hal(list_twe,session):
    for id in list_twe[0][list_twe[1]:]
#delete tweets all
def del_twe_all(list_twe,session):
    for id in list_twe:
        del_twe(id,session)
#do nothing
def del_nothing():
    return 0
#################