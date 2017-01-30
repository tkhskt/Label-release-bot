from django.shortcuts import render
from label.scraping import altema,maltine,bunkai,sense,trekkie,warp,planet,flau,progressive,digger
# Create your views here.
import json
import requests
from label.models import lineid,sensedb
from django.shortcuts import render
from django.http import HttpResponse


ACCESS_TOKEN = "VfiERPUAyZgGItiV0P7xYRuJLPL1krT9jB81YbK1V4hFoxDbMSSwRvTJzG4K7+eFFH0mobhsF5tcXtLtlSGWKq0uho67eg3Dh6Z6eImDBo8WKnwD63Do+Nfwa/PN9UQnG9c01HJgTk07RX0mquWUBQdB04t89/1O/w1cDnyilFU="

HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

ENDPOINT = 'https://api.line.me/v2/bot/message/multicast'


def linetransmit(): #label,title,artist,url
    text = "New Release!"#+label+" "+title+" - "+artist+" "+url
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
    requests.post(ENDPOINT,header=HEADER,data=json.dumps(payload))
    tx = "kokomadedekitayo"
    db = sensedb(artist=tx)
    db.save()


def labelcheck(request):
  p = "done"
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

  dig = digger.digger(0)
  #if dig['key']==1:
  linetransmit()

  return HttpResponse(p)








def lineidinput(request):
    request_json = json.loads(request.body.decode('utf-8'))
    p = "ok"
    for e in request_json['events']:
        if e['type'] == 'follow':
         userid = e['source']['userId']
         db = lineid(user=userid)
         db.save()

    return HttpResponse(p)