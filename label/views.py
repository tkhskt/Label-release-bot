from label.scraping import scrape
# Create your views here.
from .models import releases
import json
import requests
from label.models import lineid,update,labelset
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
    'ne':['neRecords','ne ','Ne ','NE ','NeRecords','Nerecords','ネレコーズ','ネ ','ね '],
    'outlier':['OUTLIER RECORDINGS','Outlier','outlier','OUTLIER','アウトライアー','アウトライヤー'],
    'king':['King Deluxe','King','king','KING','キング','きんぐ'],
    'gondwana':['Gondwana Records','Gondwana','gondwana','GONDWANA','Gondowana','gondowana','GONDOWANA','ゴンドワナ','ごんどわな'],
    'alphaversion':['AlphaVersion Records','alphaversion','アルファバージョン','あるふぁばーじょん','AlphaVersion','Alphaversion','Alpha version','Alpha Version','alpha version'],
    'eklektik':['EKLEKTIK RECORDS','Eklektik','eklektik','エクレクティック','エクレクチック'],
    'otographic':['Otographic Music','otographic','Otographic','OTOGRAPHIC','オトグラフィック','オートグラフィック','おとぐらふぃっく','おーとぐらふぃっく'],
    'young':['Young Turks','Young','young','turks','Turks','YOUNG','ヤング','やんぐ'],
    'n5md':['n5MD','n5md','N5MD','N5md','m5nd','M5nd','M5ND'],
    'wavemob':['wavemob','Wavemob','WAVEMOB','Wave mob','wave mob','Wave Mob','ウェーブモブ','ウェーブ　モブ','ウェーブ・モブ','うぇーぶもぶ']
}


labelname = {
             1:['altema','maltine','bunkai-kei','trekkie trax','sense'],
             2:['flau', 'progressive form','warp','planet mu','owsla'],
             3:['revealed', 'ghostly international',"spinnin'",'wedidit','never slept'],
             4:['mad decent','r&s','ed banger','brainfeeder','luckyme'],
             5:['moose','anticon','orikami','ne','outlier'],
             6:['king','gondwana','alphaversion','eklektik','otographic'],
             7:['young','n5md','wavemob'],
}


def linetransmit(label,title,artist,url): #label,title,artist,url
    p = "done"
    text = "New Release!\n" +label+"\n"+title+" - "+artist+"\n"+url
    userid = []
    for ids in lineid.objects.all():
        if ids.rec == 'on':
            for lb in ids.label.all():
               n = lb.label
               if words[n][0] == label:
                  userid.append(ids.user)
        elif ids.rec == 'off':
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



def push(text,token):

    payload = {
        "replyToken":token,#'U9cffcfa9f62705b889bfc4470efea951',
        "messages":[
            {
                "type":"text",
                "text": text
            }
        ]
    }
    requests.post(REPLY_ENDPOINT,headers=HEADER,data=json.dumps(payload))




def labelcheck(request,page):
     res = 'OK' + page
     er = 'error' + page
     try:
       for lb in labelname[int(page)]:
         info = scrape().doscraping(lb)
         if info['key']==1:
           linetransmit(info['label'],info['title'],info['artist'],info['url'])
           db = update(label=info['label'],url=info['url'].replace('\n複数のリリースがあります',''))
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




def setLabel(text,id,token):
    us = lineid.objects.get(user=id)
    if us.toroku == "off" and us.kaijo == "off":
        if "登録" in text:
           us.toroku = "on"
           push_text = "登録を開始します、レーベル名を入力してください。"
           us.rec = "on"
           push(push_text,token)
           us.save()
           return -1

        elif "解除" in text:
            us.kaijo = "on"
            push_text = "解除するレーベル名を入力してください。"
            push(push_text,token)
            us.save()
            return -1

        else:
           us.save()
           return 0


    elif us.toroku == "on" or us.kaijo == "on":
        if "完了" in text:
            if us.toroku == "on":
                us.toroku = "off"
                us.save()
                push_done = "登録が完了しました。"
                push(push_done,token)
            elif us.kaijo == "on":
                us.kaijo = "off"
                us.save()
                push_done = "解除が完了しました。"
                push(push_done,token)

        else:
            us.save()
            for i in labelname:
                for lb in labelname[i]:
                    key = True
                    for wd in words[lb]:
                        if wd in text:
                            if key:
                                db = labelset.objects.filter(label=lb).order_by('id').first()
                                if us.toroku == "on":
                                  us.label.add(db)
                                elif us.kaijo == "on":
                                  us.label.remove(db)
                                key = False
        return -1

    elif "確認" in text:
        push_text_kakunin = "現在の登録レーベル\n"
        for ulb in us.label.all():
            push_text_kakunin += ulb + "\n"
        push(push_text_kakunin,token)

        return -1








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
      text = text + "{title:" + '"' + label[i] + '",' + "url:" + "'" + url[i] + "'," + "start:" + "'" + date[i].strftime('%Y/%m/%d') + "'},"

    return render(request,'calendar.html',{'text':text})



def lineidinput(request):
    request_json = json.loads(request.body.decode('utf-8'))
    p = "ok"
    id =[]
    for e in request_json['events']:

        if e['type'] == 'follow':
           userid = e['source']['userId']
           db = lineid(user=userid,toroku='off',kaijo="off",rec='off')
           db.save()

        elif e['type'] == 'unfollow':
           userid = e['source']['userId']

           delete = lineid.objects.filter(user=userid).first()
           delete.delete()

        if e['type']=='message':
            if e['message']['type']=='text':
                rptoken = e['replyToken']
                key = setLabel(e['message']['text'],e['source']['userId'],rptoken)
                if key == 0:
                    data = wordcheck(e['message']['text'],rptoken)
                    reply(data)
                else:
                    pass

    return HttpResponse(p)


def dbadd(request):
    for i in range(7):
        for ln in labelname[i+1]:
            db = labelset(label=ln)
            db.save()