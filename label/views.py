from django.shortcuts import render
from label.scraping import altema,maltine,bunkai,sense,trekkie,warp,planet,flau,progressive,digger,owsla,revealed
# Create your views here.
import json
import requests
from label.models import lineid,diggerdb
from django.shortcuts import render
from django.http import HttpResponse


ACCESS_TOKEN = "VfiERPUAyZgGItiV0P7xYRuJLPL1krT9jB81YbK1V4hFoxDbMSSwRvTJzG4K7+eFFH0mobhsF5tcXtLtlSGWKq0uho67eg3Dh6Z6eImDBo8WKnwD63Do+Nfwa/PN9UQnG9c01HJgTk07RX0mquWUBQdB04t89/1O/w1cDnyilFU="

HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

ENDPOINT = 'https://api.line.me/v2/bot/message/multicast'
PUSH_ENDPOINT ='https://api.line.me/v2/bot/message/push'


def linetransmit(label,title,artist,url): #label,title,artist,url
    p = "done"
    text = "New Release!\n" +label+"\n"+title+" - "+artist+" "+url
    userid = []
    for ids in lineid.objects.all():
        userid.append(ids.user)
    payload = {
        "to":userid,
        "messages":[
            {
                "type":"text",
                "text": text
            }
        ]
    }
    requests.post(ENDPOINT,headers=HEADER,data=json.dumps(payload))



def takahashi(no):

    payload = {
        "to":'U9cffcfa9f62705b889bfc4470efea951',
        "messages":[
            {
                "type":"text",
                "text": '今日は更新なかった'
            }
        ]
    }
    requests.post(PUSH_ENDPOINT,headers=HEADER,data=json.dumps(payload))




def labelcheck(request):
  p = "done"

  dig = digger.digger(0)
  alt = altema.altema(0)
  if alt['key']==1:
      linetransmit(alt['label'],alt['title'],alt['artist'],alt['url'])
  mal = maltine.maltine(0)
  if mal['key']==1:
      linetransmit(mal['label'],mal['title'],mal['artist'],mal['url'])
  bun = bunkai.bunkai(0)
  if bun['key']==1:
      linetransmit(bun['label'],bun['title'],bun['artist'],bun['url'])
  tre = trekkie.trekkie(0)
  if tre['key']==1:
      linetransmit(tre['label'],tre['title'],tre['artist'],tre['url'])
  sen = sense.sense(0)
  if sen['key']==1:
      linetransmit(sen['label'],sen['title'],sen['artist'],sen['url'])

  takahashi(3)

  #if dig['key']==1:
   #linetransmit(dig['label'],dig['title'],dig['artist'],dig['url'])

  return HttpResponse(p)



def labelcheck2(request):
    p = "done2"
    pro = progressive.progressive(0)
    if pro['key']==1:
        linetransmit(pro['label'],pro['title'],pro['artist'],pro['url'])
    fla = flau.flau(0)
    if fla['key']==1:
     linetransmit(fla['label'],fla['title'],fla['artist'],fla['url'])
    war = warp.warp(0)
    if war['key']==1:
     linetransmit(war['label'],war['title'],war['artist'],war['url'])
    pla = planet.planet(0)
    if pla['key']==1:
     linetransmit(pla['label'],pla['title'],pla['artist'],pla['url'])
    ows = owsla.owsla(0)
    if ows['key']==1:
     linetransmit(ows['label'],ows['title'],ows['artist'],ows['url'])

    return HttpResponse(p)


def labelcheck3(request):
    p = "done3"
    rev = revealed.revealed(0)
    if rev['key']==1:
        linetransmit(rev['label'],rev['title'],rev['artist'],rev['url'])


    return HttpResponse


def lineidinput(request):
    request_json = json.loads(request.body.decode('utf-8'))
    p = "ok"
    for e in request_json['events']:
        if e['type'] == 'follow':
         userid = e['source']['userId']
         db = lineid(user=userid)
         db.save()

    return HttpResponse(p)