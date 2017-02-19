from django.shortcuts import render
from label.scraping import altema,maltine,bunkai,sense,trekkie,warp,planet,flau,progressive,\
      digger,owsla,revealed,ghostly,spinnin,wedidit,never,mad,rs,edbanger,brainfeeder
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
        "to":['U9cffcfa9f62705b889bfc4470efea951',],#userid,
        "messages":[
            {
                "type":"text",
                "text": text
            }
        ]
    }
    requests.post(ENDPOINT,headers=HEADER,data=json.dumps(payload))



def takahashi():

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
 try:
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
  takahashi()
  return HttpResponse(p)
 except:
  return HttpResponse("error")




def labelcheck2(request):
   p = "done2"
   try:
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
   except:
    return HttpResponse("error")



def labelcheck3(request):
   p = "done3"
   try:
    rev = revealed.revealed(0)
    if rev['key']==1:
        linetransmit(rev['label'],rev['title'],rev['artist'],rev['url'])
    gho = ghostly.ghostly(0)
    if gho['key']==1:
        linetransmit(gho['label'],gho['title'],gho['artist'],gho['url'])
    spi = spinnin.spinnin(0)
    if spi['key']==1:
        linetransmit(spi['label'],spi['title'],spi['artist'],spi['url'])
    wed = wedidit.wedidit(0)
    if wed['key']==1:
        linetransmit(wed['label'],wed['title'],wed['artist'],wed['url'])
    nev = never.never(0)
    if nev['key']==1:
        linetransmit(nev['label'],nev['title'],nev['artist'],nev['url'])
    return HttpResponse(p)
   except:
    return HttpResponse("error")





def labelcheck4(request):
    p = "done4"
   #try:
    ma = mad.mad(0)
    if ma['key']==1:
        linetransmit(ma['label'],ma['title'],ma['artist'],ma['url'])
    r = rs.rs(0)
    if r['key']==1:
        linetransmit(r['label'],r['title'],r['artist'],r['url'])
    ed = edbanger.edbanger(0)
    if ed['key']==1:
        linetransmit(ed['label'],ed['title'],ed['artist'],ed['url'])
    br = brainfeeder.brainfeeder(0)
    if br['key']==1:
        linetransmit(br['label'],br['title'],br['artist'],br['url'])
    return HttpResponse(p)
   #except:
    #return HttpResponse("error4")


def lineidinput(request):
    request_json = json.loads(request.body.decode('utf-8'))
    p = "ok"
    id =[]
    for e in request_json['events']:
        if e['type'] == 'follow':
         userid = e['source']['userId']
         db = lineid(user=userid)
         db.save()

        if e['type'] == 'unfollow':
           for i in lineid.objects.all():
               id.append(i.user)

           delete = lineid.objects.all()
           delete.delete()

           userid = e['source']['userId']

           id.remove(userid)

           for i in range(len(id)):
            db = lineid(user=id[i])
            db.save()
    return HttpResponse(p)