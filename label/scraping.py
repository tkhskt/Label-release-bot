from bs4 import BeautifulSoup
import urllib.request
from label.models import altemadb,maltinedb,sensedb,bunkaidb,trekkiedb,flaudb,progressivedb,warpdb,planetdb,diggerdb,owsladb,revealeddb,ghostlydb,spinnindb,wediditdb,neverdb
import re

class altema:
    def altema(number):
        url = 'http://www.altemarecords.jp/release/'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        info = {"label":"Altema Records","title":"","artist":"","url":"","key":0}
        title = [] #タイトル
        artist = [] #アーティスト名
        url = [] #リンク

        artistdb = [] #dbから取得したアーティスト情報

        for artdb in altemadb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        tn = soup.find_all(class_='track_name')
        ta = soup.find_all(class_ = 'track_artist')
        link = soup.find_all('a',href=True)

        dl = soup.find_all("dl")



        for i in soup.find_all('a',href=True):
         #print(i['href'])
          url.append(i['href'])

        for i in range(5):
          url.pop(0)


        for i in range(len(tn)):
          n = str(tn[i])
          n2 = n.replace('<li class="track_name">','').replace('</li>','').replace('[','').replace(']','').replace('<del>','').replace('</del>','')
          title.append(n2)
          a = str(ta[i])
          a2 = a.replace('<li class="track_artist">','').replace('</li>','').replace('[','').replace(']','').replace('<del>','').replace('</del>','')
          artist.append(a2)

        title.remove("K2")#.remove("SCHOOL GIRL AKATHISIA").remove("dots")
        title.remove("SCHOOL GIRL AKATHISIA")
        title.remove("dots")

        artist.remove("V.A")#.remove("PandaBoY")
        artist.remove("V.A")#.remove("PandaBoY")
        artist.remove("PandaBoY")

        for i in range(len(url)):
            url[i] = 'http://www.altemarecords.jp/rel' \
                     'ease/'+url[i].replace("./","")

        if len(artist)>len(artistdb):
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = altemadb.objects.all()
        delete.delete()

        for i in range(len(artist)):
            at = artist[i]
            db = altemadb(artist=at)
            db.save()

        return info


class maltine:
    def maltine(self):
        url = 'http://maltinerecords.cs8.biz/release.html'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        release = []
        url = []
        info =  {"label":"Maltine Records","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報

        for artdb in maltinedb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        h2tag = soup.find("h2")

        title = h2tag.text.replace('\n','rep').split('rep')

        for i in range(4):
          title.remove('')

        for i in h2tag.find_all("a",href=True):
         link = i['href']

         if 'http://' in link:
             url.append(link)

         if not 'http://' in link:
             if not '/'in link:
                 link = 'http://maltinerecords.cs8.biz/' + link
                 url.append(link)
             else:
                  link = 'http://maltinerecords.cs8.biz' + link
                  url.append(link)
                  #print(link)


         if len(url)>len(artistdb):
             info['title']=title[0]
             #info['artist']=artist[0]
             info['url']=url[0]
             info['key']=1

        delete = maltinedb.objects.all()
        delete.delete()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            db = maltinedb(artist=at)
            db.save()

        return info

class bunkai:
    def bunkai(self):
        url = 'http://bunkai-kei.com/release/'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        artist = []
        title = []
        url = []
        info =  {"label":"Bunkai-kei Records","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報

        for artdb in bunkaidb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for ri2 in soup.find_all(class_='ri2'):
            ta = ri2.text
            artist.append(ta)

        for ri3 in soup.find_all(class_='ri3'):
         tn = ri3.text
         title.append(tn)

        for href in soup.find_all(class_='side_content'):
         link = href.find_all('a',href=True)
         for urls in link:
               url.append(urls['href'])

        if len(url)>len(artistdb):
            info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = bunkaidb.objects.all()
        delete.delete()

        for i in range(len(url)):
            at = artist[i]
            #tit = title[i]
            #ur =  url[i]
            db = bunkaidb(artist=at)
            db.save()

        return info


class sense:
    def sense(self):
        url = 'http://sense-sapporo.jp/release'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        artist = []
        title = []
        url = []

        info =  {"label":"SenSe","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報

        for artdb in sensedb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for cts in soup.find_all(class_="content_title_single"):
          title.append(cts.text)

        for sh in soup.find_all(class_="subtitle_head"):
          artist.append(sh.text)

        for link in soup.find_all(class_="hover-content"):
         link2 = link.find_all("a")
         for urls in link2:
               url.append(urls['href'])

        if len(artist)>len(artistdb):
             info['title']=title[0]
             info['artist']=artist[0]
             info['url']=url[0]
             info['key']=1

        delete = sensedb.objects.all()
        delete.delete()

        for i in range(len(url)):
            at = artist[i]
            #tit = title[i]
            #ur =  url[i]
            db = sensedb(artist=at)
            db.save()

        return info


class trekkie:
    def trekkie(self):
        url = 'http://www.trekkie-trax.com/ep/'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        artist = []
        title = []
        url = []

        info =  {"label":"Trekkie Trax","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報

        for artdb in trekkiedb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for link in soup.find_all('div', style='text-align:center;'):
            link2 = link.find_all("a")
            for urls in link2:
                url.append(urls['href'])

        if len(url)>len(artistdb):
            #info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = trekkiedb.objects.all()
        delete.delete()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = trekkiedb(artist=at)
            db.save()

        return info

class planet:
    def planet(self):
        url = 'http://planet.mu/releases/'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        artist = []
        title = []
        url = []

        info =  {"label":"Planet Mu","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報

        for artdb in planetdb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for bbr in soup.find_all(class_="box-inner"):
         ra = bbr.find_all(class_="release-artist")
         rt = bbr.find_all(class_="release-title")


         for art in ra:
              artist.append(art.text)
         for tit in rt:
              title.append(tit.text)
              for link in tit.find_all("a"):
                   url.append(link['href'])

        if artist[0]!=artistdb[0]:
             info['title']=title[0]
             info['artist']=artist[0]
             info['url']=url[0]
             info['key']=1

        delete = planetdb.objects.all()
        delete.delete()

        for i in range(len(url)):
            at = artist[i]
            #tit = title[i]
            #ur =  url[i]
            db = planetdb(artist=at)
            db.save()

        return info


class warp:
    def warp(self):
        url = 'https://warp.net/releases/'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        pre = []
        pre2 = []

        artist = []
        title = []
        url = []

        info =  {"label":"Warp Records","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報

        for artdb in warpdb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for art in soup.find_all("p",class_="GridItem-title"):
          pre.append(art.text)

        for i in range(len(pre)):
           b =  pre[i].replace('\n','')
           pre2.append(b)

        for i in range(1,int((len(pre2)+2)/2)):
          title.append(pre2[i*2-1])
          #print(title[i])

        for i in range(0,int((len(pre2))/2)):
         artist.append(pre2[i*2])

        for i in range(len(title)):
         for link in soup.find_all("a",class_="GridItem-link",href=True,title=title[i]):
             url.append('https://warp.net' + link['href'])

        if artist[0]!=artistdb[0]:
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = warpdb.objects.all()
        delete.delete()

        for i in range(len(url)):
            at = artist[i]
            #tit = title[i]
            #ur =  url[i]
            db = warpdb(artist=at)
            db.save()

        return info


class progressive:
    def progressive(self):
        url = 'https://pform.thebase.in/'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        pre = []

        #artist = []
        title = []
        url = []

        info =  {"label":"PROGRESSIVE FOrM","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報

        for artdb in progressivedb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for tit in soup.find_all(class_="itemTitle"):
          pre.append(tit.text)

        for i in range(len(pre)):
          b = pre[i].replace("\n","")
          title.append(b)

        for link in soup.find_all(class_="itemImg"):
         link2 = link.find_all("a")
         for urls in link2:
               url.append(urls['href'])

        if len(title)>len(artistdb):
            info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = progressivedb.objects.all()
        delete.delete()

        for i in range(len(url)):
            at = title[i]
            #tit = title[i]
            #ur =  url[i]
            db = progressivedb(artist=at)
            db.save()

        return info


class flau:
    def flau(self):
        url = 'http://flau.jp/releases.html'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        artist = []
        title = []
        url = []

        artist = []
        title = []
        url = []


        info =  {"label":"flau","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報

        for artdb in flaudb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)



        for tit in soup.find_all("section",class_="unit"):
          for h3 in tit.find_all("h3"):
             title.append(h3.text)
          for p in tit.find_all("p"):
             if p.text!='\xa0' and p.text!=' ' and p.text!='':
                   artist.append(p.text)

          for link in tit.find_all("a",href=True):
             if link['href'] != '':
                if  'http://' in link['href']:
                       url.append(link['href'])
                else:
                       url.append('http://flau.jp/' + link['href'])

        if len(artist)>len(artistdb):
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = flaudb.objects.all()
        delete.delete()

        for i in range(len(url)):
            at = artist[i]
            #tit = title[i]
            #ur =  url[i]
            db = flaudb(artist=at)
            db.save()

        return info


class owsla:
    def owsla(self):

       info =  {"label":"OWSLA","title":"","url":"","artist":"","key":0}

       artistdb = [] #dbから取得したアーティスト情報

       for artdb in owsladb.objects.all().order_by('id'):
           artistdb.append(artdb.artist)

       url = 'http://owsla.com/releases/'
       req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
       response = urllib.request.urlopen(req)
       html = response.read()
       soup = BeautifulSoup(html, "lxml")

        #artist = []
       #title = []
       url = []

       p = soup.prettify()

       for link in soup.find_all(class_="view option valign"):
        url.append(link['href'])

       if url[0]!=artistdb[0]:
           #info['title']=title[0]
           #info['artist']=artist[0]
           info['url']=url[0]
           info['key']=1

       delete = owsladb.objects.all()
       delete.delete()

       for i in range(len(url)):
           at = url[i]
           #tit = title[i]
           #ur =  url[i]
           db = owsladb(artist=at)
           db.save()

       return info



class revealed:
    def revealed(self):

        info =  {"label":"Revealed Records","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報

        for artdb in revealeddb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)



        url = 'http://www.revealedrecordings.com/releases/'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        pre =[]

        #artist = []
        #title = []
        url = []

        p = soup.prettify()



        for link in soup.find_all(class_="releaseblock"):
           for link2 in link.find_all("a"):
             pre.append(link2['href'])

        for i in range(len(pre)):
          if 'http://www.revealedrecordings.com' in pre[i]:
               url.append(pre[i])

        if url[0]!=artistdb[0]:
            #info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = revealeddb.objects.all()
        delete.delete()

        for i in range(len(url)):
           at = url[i]
            #tit = title[i]
            #ur =  url[i]
           db = revealeddb(artist=at)
           db.save()

        return info



class ghostly:
    def ghostly(self):
        info =  {"label":"Ghostly International","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報
        titledb = []
        urldb = []

        for artdb in ghostlydb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)
            titledb.append(artdb.title)
            urldb.append(artdb.url)

        url = 'http://ghostly.com/releases'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")


        preurl = []
        pretitle = []
        preartist = []


        p = soup.prettify()

        for link in soup.find_all("dl",class_="artist-releases"):
          for link2 in link.find_all("a"):
             preurl.append(link2['href'])
          for art in link.find_all("dd",class_="artist"):
             preartist.append(art.text)
          for tit in link.find_all("dd",class_="title"):
             pretitle.append(tit.text)

        if len(preartist)>len(artistdb):
            artist = set(preartist)-set(artistdb)
            title = set(pretitle)-set(titledb)
            url = set(preurl)-set(urldb)
            artist = list(artist)
            title = list(title)
            url = list(url)

            for i in range(len(url)):
                url[i] = 'http://ghostly.com'+url[i]

            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1



        delete = ghostlydb.objects.all()
        delete.delete()

        for i in range(len(preurl)):
            at = preartist[i]
            tit = pretitle[i]
            ur = preurl[i]
            db = ghostlydb(artist=at,title=tit,url=ur)
            db.save()

        return info



class spinnin:
    def spinnin(self):
        url = 'https://www.spinninrecords.com/releases/'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        pre = []
        pre2 = []

        artist = []
        title = []
        url = []

        info =  {"label":"Spinnin' Records","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報

        for artdb in spinnindb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)


        for tit in soup.find_all("h2"):
         for link in tit.find_all("a"):
             title.append(link.text)
             url.append(link['href'])


        for art in soup.find_all(class_="item music jscroll-content"):
           for art2 in art.find_all("p"):
              pre.append(art2.text)

        for i in range(len(pre)):
          pre2.append(pre[i].replace("\n",""))

        for i in range(len(pre2)):
         moji = re.sub('\s{2}',"",pre2[i]) #連続した空白の削除
         artist.append(moji)

        for i in range(len(url)):
            url[i] = "https://www.spinninrecords.com" + url[i]

        if title[0]!=artistdb[0]:
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = spinnindb.objects.all()
        delete.delete()

        for i in range(len(url)):
            at = title[i]
            #tit = title[i]
            #ur =  url[i]
            db = spinnindb(artist=at)
            db.save()

        return info



class wedidit:
    def wedidit(self):
        url = 'http://www.wediditcollective.com/releases/'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        artist = []
        title = []
        url = []

        info =  {"label":"WEDIDIT","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報

        for artdb in wediditdb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for link in soup.find_all(class_="releases-wrapper"):
           for link2 in link.find_all("a"):
              url.append(link2['href'])
           for art in link.find_all("h4"):
              artist.append(art.text)
           for tit in link.find_all("h3"):
              title.append(tit.text)

           if len(title)>len(artistdb):
               info['title']=title[0]
               info['artist']=artist[0]
               info['url']=url[0]
               info['key']=1

        delete = wediditdb.objects.all()
        delete.delete()

        for i in range(len(url)):
            at = title[i]
            #tit = title[i]
            #ur =  url[i]
            db = wediditdb(artist=at)
            db.save()

        return info



class never:
    def never(self):
        url = 'https://never-slept.bandcamp.com/'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        #artist = []
        title = []
        url = []


        info =  {"label":"Never Slept","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報

        for artdb in neverdb.objects.all().order_by('id'):
            neverdb.append(artdb.artist)


        for tit in soup.find_all("p",class_="title"):
          title.append(tit.text)


        for i in range(len(title)):
           title[i] = title[i].replace("\n","")

        for i in range(len(title)):
           title[i] = re.sub("\s{2}","",title[i])

        for link in soup.find_all("div",class_="leftMiddleColumns"):
          for link2 in link.find_all("a"):
             url.append(link2['href'])

        for i in range(len(url)):
            url[i] = 'https://never-slept.bandcamp.com' + url[i]


        if len(title)>len(artistdb):
            info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = neverdb.objects.all()
        delete.delete()

        for i in range(len(url)):
            at = title[i]
            #tit = title[i]
            #ur =  url[i]
            db = neverdb(artist=at)
            db.save()

        return info

class digger:
    def digger(self):
        url = 'https://salty-lake-16271.herokuapp.com/results/'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        pre = []
        artist = []
        title = []
        url = []

        info =  {"label":"diggertools","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報

        for artdb in diggerdb.objects.all().order_by('id'):
         artistdb.append(artdb.artist)

        for art in soup.find_all(class_="type02"):
          for cla in art.find_all(class_='cell'):
              pre.append(cla.text)
          for tex in art.find_all(class_='text'):
              title.append(tex.text)

        for i in range(int(len(pre)/2)):
           url.append(pre[i])

        if len(title)>len(artistdb):
            info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = diggerdb.objects.all()
        delete.delete()

        for i in range(len(url)):
         at = title[i]
          #tit = title[i]
          #ur =  url[i]
         db = diggerdb(artist=at)
         db.save()

        return info