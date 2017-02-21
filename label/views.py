from django.shortcuts import render
from label.scraping import altema,maltine,bunkai,sense,trekkie,warp,planet,flau,progressive,\
      digger,owsla,revealed,ghostly,spinnin,wedidit,never,mad,rs,edbanger,brainfeeder,luckyme
# Create your views here.
from .models import releases
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
REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'

words = {
    'altema':['altema','アルテマ','あるてま','altima','Altima','アルティマ','アルティメ','Altema','ALTEMA'],
    'maltine':['maltine','マルチネ','マルティネ','malutine','marutine','martine','MALTINE','Maltine','まるちね'],
    'bunkai-kei':['bunkai','Bunkai','BUNKAI','分解','ぶんかい','ブンカイ'],
    'trekkie trax':['Trekkie','TREKKIE','trekkie','トレッキー','とれっきー'],
    'sense':['SenSe','SENSE','sense','Sense','senSe','センス','せんす','sence','Sence'],
    'flau':['flau','FLAU','FLAW','Flau','ふらう','ふらー','flaw','Flaw','フル―','フラ','フラー','ふる','ふるー','フラウ'],
    'progressive form':['PROGRESSIVE','progressive','Progressive','プログレッシブ','プログレッシヴ','ぷろぐれっしぶ'],
    'warp':['Warp','warp','WARP','ウォープ','ワープ','うぉーぷ','わーぷ'],
    'planet mu':['Planet','planet','PLANET','ぷらねっと','プラネット'],
    'owsla':['OWSLA','owsla','Owsla','オウスラ','おうすら','オースラ','オウズラ','おーずら'],
    'revealed':['Revealed','REVEALED','revealed','リヴィールド','リビールド'],
    'ghostly international':['Ghostly','GHOSTLY','ghostly','Ghosty','GHOSTTY','ghosty','ゴーストリー','ごーすとりー','ごーすてぃー','ゴースティー'],
    "spinnin'":['Spinnin','spinnin','SPINNIN','スピニン','すぴにん'],
    'wedidit':['WEDIDIT','wedidit','Wedidit','ウィーディドイット','ウィーディドゥイット','うぃーでぃどいっと'],
    'never slept':['Never','NEVER','never','ネヴァー','ネバー','ねばー'],
    'mad decent':['Mad','MAD','mad','マッド','まっど'],
    'r&s':['R&S','RandS','rands','r&s','Rands','R&s','アール','あーる'],
    'ed banger':['Ed Banger','ED BANGER','ed banger','Ed banger','ed Banger','EdBanger','EDBANGER','edbanger','Edbanger','edBanger','エドバンガー','エド・バンガー','エド　バンガー'],
    'brainfeeder':['Brain','brain','BRAIN','ブレイン','ブレーン','ぶれいん','ぶれーん'],
    'luckyme':['Lucky','lucky','LUCKY','ラッキー','らっきー'],
}




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
  #dig = digger.digger(0)
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
  #takahashi()
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
   try:
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
    lc = luckyme.luckyme(0)
    if lc['key']==1:
        linetransmit(lc['label'],lc['title'],lc['artist'],lc['url'])
    return HttpResponse(p)
   except:
    return HttpResponse("error4")




def wordcheck(text,token):
    data = {
            'label':[],
            'url':[],
            'token':token,
            }
    for wd in words['altema']:
        if wd in text:
            db = releases.objects.filter(label='altema').order_by('id').first()
            data['label'].append('Altema Records')
            data['url'].append(db.url)
    for wd in words['maltine']:
        if wd in text:
            db = releases.objects.filter(label='maltine').order_by('id').first()
            data['label'].append('Maltine Records')
            data['url'].append(db.url)
    for wd in words['bunkai-kei']:
        if wd in text:
            db = releases.objects.filter(label='bunkai-kei').order_by('id').first()
            data['label'].append('Bunkai-Kei Records')
            data['url'].append(db.url)
    for wd in words['trekkie trax']:
        if wd in text:
            db = releases.objects.filter(label='trekkie trax').order_by('id').first()
            data['label'].append('TREKKIE TRAX')
            data['url'].append(db.url)
    for wd in words['sense']:
        if wd in text:
            db = releases.objects.filter(label='sense').order_by('id').first()
            data['label'].append('SenSe')
            data['url'].append(db.url)
    for wd in words['flau']:
        if wd in text:
            db = releases.objects.filter(label='flau').order_by('id').first()
            data['label'].append('flau')
            data['url'].append(db.url)
    for wd in words['progressive form']:
        if wd in text:
            db = releases.objects.filter(label='progressive form').order_by('id').first()
            data['label'].append('PROGRESSIVE FOrM')
            data['url'].append(db.url)
    for wd in words['warp']:
        if wd in text:
            db = releases.objects.filter(label='warp').order_by('id').first()
            data['label'].append('Warp Records')
            data['url'].append(db.url)
    for wd in words['planet mu']:
        if wd in text:
            db = releases.objects.filter(label='planet mu').order_by('id').first()
            data['label'].append('Planet Mu')
            data['url'].append(db.url)
    for wd in words['owsla']:
        if wd in text:
            db = releases.objects.filter(label='owsla').order_by('id').first()
            data['label'].append('OWSLA')
            data['url'].append(db.url)
    for wd in words['revealed']:
        if wd in text:
            db = releases.objects.filter(label='revealed').order_by('id').first()
            data['label'].append('Revealed Recordings')
            data['url'].append(db.url)
    for wd in words['ghostly international']:
        if wd in text:
            db = releases.objects.filter(label='ghostly international').order_by('id').first()
            data['label'].append('Ghostly International')
            data['url'].append(db.url)
    for wd in words["spinnin'"]:
        if wd in text:
            db = releases.objects.filter(label="spinnin'").order_by('id').first()
            data['label'].append("Spinnin' Records")
            data['url'].append(db.url)
    for wd in words['wedidit']:
        if wd in text:
            db = releases.objects.filter(label='wedidit').order_by('id').first()
            data['label'].append('WEDIDIT')
            data['url'].append(db.url)
    for wd in words['never slept']:
        if wd in text:
            db = releases.objects.filter(label='never slept').order_by('id').first()
            data['label'].append('Never Slept')
            data['url'].append(db.url)
    for wd in words['mad decent']:
        if wd in text:
            db = releases.objects.filter(label='mad decent').order_by('id').first()
            data['label'].append('Mad Decent')
            data['url'].append(db.url)
    for wd in words['r&s']:
        if wd in text:
            db = releases.objects.filter(label='r&s').order_by('id').first()
            data['label'].append('R&S Records')
            data['url'].append(db.url)
    for wd in words['ed banger']:
        if wd in text:
            db = releases.objects.filter(label='ed banger').order_by('id').first()
            data['label'].append('Ed Banger Records')
            data['url'].append(db.url)
    for wd in words['brainfeeder']:
        if wd in text:
            db = releases.objects.filter(label='brainfeeder').order_by('id').first()
            data['label'].append('Brainfeeder')
            data['url'].append(db.url)
    for wd in words['luckyme']:
        if wd in text:
            db = releases.objects.filter(label='luckyme').order_by('id').first()
            data['label'].append('LuckyMe')
            data['url'].append(db.url)
    return data





def reply(data):
    payload = {
        "replyToken":data['token'],
        "messages":[]
    }

    if len(data['url'])>5:
        payload['messages'].append(
            {
             'type':'text',
             'text':'一度に調べられるレーベルは５つまでです。'
            }
        )
    if len(data['url'])<=5:
        for i in range(len(data['label'])):
            payload['messages'].append(
                {
                    'type':'text',
                    'text':data['label'][i]+"\n"+data['url'][i]
                }
            )
    requests.post(REPLY_ENDPOINT,headers=HEADER,data=json.dumps(payload))




def lineidinput(request):
    request_json = json.loads(request.body.decode('utf-8'))
    p = "ok"
    id =[]
    for e in request_json['events']:
        rptoken = e['replyToken']

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


        if e['type']=='message':
            if e['message']['type']=='text':
                data = wordcheck(e['message']['text'],rptoken)
                reply(data)
    return HttpResponse(p)