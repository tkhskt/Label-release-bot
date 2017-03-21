from django.shortcuts import render
from label.scraping import scrape,digger
# Create your views here.
from .models import releases
import json
import requests
from label.models import lineid,update
from django.shortcuts import render
from django.http import HttpResponse


ACCESS_TOKEN = "VfiERPUAyZgGItiV0P7xYRuJLPL1krT9jB81YbK1V4hFoxDbMSSwRvTJzG4K7+eFFH0mobhsF5tcXtLtlSGWKq0uho67eg3Dh6Z6eImDBo8WKnwD63Do+Nfwa/PN9UQnG9c01HJgTk07RX0mquWUBQdB04t89/1O/w1cDnyilFU="

HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

ENDPOINT = 'https://api.line.me/v2/bot/message/multicast'
PUSH_ENDPOINT = 'https://api.line.me/v2/bot/message/push'
REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'

words = {
    'altema':['Altema Records','altema','アルテマ','あるてま','altima','Altima','アルティマ','アルティメ','Altema','ALTEMA'],
    'maltine':['Maltine Records','maltine','マルチネ','マルティネ','malutine','marutine','martine','MALTINE','Maltine','まるちね'],
    'bunkai-kei':['Bunkai-kei Records','bunkai','Bunkai','BUNKAI','分解','ぶんかい','ブンカイ'],
    'trekkie trax':['TREKKIE TRAX','Trekkie','TREKKIE','trekkie','トレッキー','とれっきー'],
    'sense':['SenSe','SENSE','sense','Sense','senSe','センス','せんす','sence','Sence'],
    'flau':['flau','FLAU','FLAW','Flau','ふらう','ふらー','flaw','Flaw','フル―','フラ','フラー','ふる','ふるー','フラウ'],
    'progressive form':['PROGRESSIVE FOrM','PROGRESSIVE','progressive','Progressive','プログレッシブ','プログレッシヴ','ぷろぐれっしぶ'],
    'warp':['Warp Records','Warp','warp','WARP','ウォープ','ワープ','うぉーぷ','わーぷ'],
    'planet mu':['Planet Mu','Planet','planet','PLANET','ぷらねっと','プラネット'],
    'owsla':['OWSLA','owsla','Owsla','オウスラ','おうすら','オースラ','オウズラ','おーずら'],
    'revealed':['Revealed Recordings','Revealed','REVEALED','revealed','リヴィールド','リビールド'],
    'ghostly international':['Ghostly International','Ghostly','GHOSTLY','ghostly','Ghosty','GHOSTTY','ghosty','ゴーストリー','ごーすとりー','ごーすてぃー','ゴースティー'],
    "spinnin'":["Spinnin' Records",'Spinnin','spinnin','SPINNIN','スピニン','すぴにん'],
    'wedidit':['WEDIDIT','wedidit','Wedidit','ウィーディドイット','ウィーディドゥイット','うぃーでぃどいっと'],
    'never slept':['Never Slept','Never','NEVER','never','ネヴァー','ネバー','ねばー'],
    'mad decent':['Mad Decent','Mad','MAD','mad','マッド','まっど'],
    'r&s':['R&S Records','R&S','RandS','rands','r&s','Rands','R&s','アール','あーる'],
    'ed banger':['Ed Banger Records','Ed Banger','ED BANGER','ed banger','Ed banger','ed Banger','EdBanger','EDBANGER','edbanger','Edbanger','edBanger','エドバンガー','エド・バンガー','エド　バンガー'],
    'brainfeeder':['Brainfeeder','Brain','brain','BRAIN','ブレイン','ブレーン','ぶれいん','ぶれーん'],
    'luckyme':['LuckyMe','Lucky','lucky','LUCKY','ラッキー','らっきー'],
    'moose':['Moose Records','Moose','moose','MOOSE','モーセ','ムース','もーせ','むーす'],
    'anticon':['anticon.','anticon','Anticon','ANTICON','アンチコン','あんちこん','あんてぃこん','アンティコン'],
    'orikami':['Orikami Records','Orikami','orikami','ORIKAMI','Origami','origami','ORIGAMI','折り紙','おりかみ','折紙','オリカミ','オリガミ','おりがみ'],

}


labelname = {
             1:['altema','maltine','bunkai-kei','trekkie trax','sense'],
             2:['flau', 'progressive form','warp','planet mu','owsla'],
             3:['revealed', 'ghostly international',"spinnin'",'wedidit','never slept'],
             4:['mad decent','r&s','ed banger','brainfeeder','luckyme'],
             5:['moose','anticon','orikami'],
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




def labelcheck(request,page):
     res = 'OK' + page
     er = 'error' + page
     try:
       for lb in labelname[int(page)]:
         info = scrape().doscraping(lb)
         if info['key']==1:
           linetransmit(info['label'],info['title'],info['artist'],info['url'])
           db = update(label=info['label'],url=info['url'])
           db.save()
       return HttpResponse(res)
     except:
       return HttpResponse(er)





def wordcheck(text,token):
    data = {
            'label':[],
            'url':[],

            'token':token,
            }

    for i in labelname:
        for lb in labelname[i]:
            key = True
            for wd in words[lb]:
                if wd in text:
                    if key:
                        db = releases.objects.filter(label=lb).order_by('id').first()
                        data['label'].append(words[lb][0])
                        data['url'].append(db.url)
                        key = False
    '''
    for wd in words['altema']:
        if wd in text:
            db = releases.objects.filter(label='altema').order_by('id').first()
            data['label'].append('Altema Records')
            data['url'].append(db.url)

    '''
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




def calendar(request):
    label = []
    url = []
    date = []
    text = ""
    for dbs in update.objects.all():
        label.append(dbs.label)
        url.append(dbs.url)
        date.append(dbs.date)

    for i in range(len(label)):
      text = text + "{\ntitle:" + '"' + label[i].replace('複数のリリースがあります','') + '",' + "\n" + "url:" + "'"  + url[i] + "'," + "\n" + "start:" + "'"  + date[i].strftime('%Y/%m/%d') + "'\n},\n"

    return render(request,'calendar.html',{'text':text})

def lineidinput(request):
    request_json = json.loads(request.body.decode('utf-8'))
    p = "ok"
    id =[]
    for e in request_json['events']:

        if e['type'] == 'follow':
           userid = e['source']['userId']
           db = lineid(user=userid)
           db.save()

        elif e['type'] == 'unfollow':
           userid = e['source']['userId']

           delete = lineid.objects.filter(user=userid).first()
           delete.delete()
           #db = lineid(user='unfollow')
           #db.save()

        if e['type']=='message':
            if e['message']['type']=='text':
                rptoken = e['replyToken']
                data = wordcheck(e['message']['text'],rptoken)
                reply(data)

    return HttpResponse(p)

