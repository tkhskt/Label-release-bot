from bs4 import BeautifulSoup
import urllib.request
from label.models import altemadb,maltinedb,sensedb,bunkaidb,trekkiedb,flaudb,\
      progressivedb,warpdb,planetdb,diggerdb,owsladb,revealeddb,ghostlydb,spinnindb,\
      wediditdb,neverdb,maddb,rsdb,edbangerdb,brainfeederdb,luckymedb,releases
import re

class scrape:

    def altema(self):
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
        artistdb2 = []

        for artdb2 in releases.objects.filter(label='altema').order_by('id'):
            artistdb2.append(artdb2.url)

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

        '''
        if len(artist)>len(artistdb):
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1
        '''
        if url[0]!=artistdb2[0]:
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1


        delete = altemadb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='altema')
        delete2.delete()

        for i in range(len(url)):
            at = url[i]
            db = releases(url=at,label='altema')
            db.save()

        for i in range(len(artist)):
            at = artist[i]
            db = altemadb(artist=at)
            db.save()

        return info



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
        artistdb2 = []

        for artdb2 in releases.objects.filter(label='maltine').order_by('id'):
            artistdb2.append(artdb2.url)


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



         if url[0]!=artistdb2[0]:
             info['title']=title[0]
             #info['artist']=artist[0]
             info['url']=url[0]
             info['key']=1
         '''
         if len(url)>len(artistdb):
             info['title']=title[0]
             #info['artist']=artist[0]
             info['url']=url[0]
             info['key']=1
         '''
        delete = maltinedb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='maltine')
        delete2.delete()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            db = releases(url=at,label='maltine')
            db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            db = maltinedb(artist=at)
            db.save()

        return info


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
        artistdb2 = []

        for artdb in bunkaidb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for artdb2 in releases.objects.filter(label='bunkai-kei').order_by('id'):
            artistdb2.append(artdb2.url)

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

        '''
        if len(url)>len(artistdb):
            info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1
        '''
        if url[0]!=artistdb2[0]:
            info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = bunkaidb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='bunkai-kei')
        delete2.delete()

        for i in range(len(url)):
            at = artist[i]
            #tit = title[i]
            #ur =  url[i]
            db = bunkaidb(artist=at)
            db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label='bunkai-kei')
            db.save()

        return info



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
        artistdb2 = []

        for artdb in sensedb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for artdb2 in releases.objects.filter(label='sense').order_by('id'):
            artistdb2.append(artdb2.url)

        for cts in soup.find_all(class_="content_title_single"):
          title.append(cts.text)

        for sh in soup.find_all(class_="subtitle_head"):
          artist.append(sh.text)

        for link in soup.find_all(class_="hover-content"):
         link2 = link.find_all("a")
         for urls in link2:
               url.append(urls['href'])

        '''
        if len(artist)>len(artistdb):
             info['title']=title[0]
             info['artist']=artist[0]
             info['url']=url[0]
             info['key']=1
        '''
        if url[0]!=artistdb2[0]:
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = sensedb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='sense')
        delete2.delete()

        for i in range(len(url)):
            at = artist[i]
            #tit = title[i]
            #ur =  url[i]
            db = sensedb(artist=at)
            db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label='sense')
            db.save()

        return info



    def trekkie(self):
        url = 'http://www.trekkie-trax.com/ep/'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        artist = []
        title = []
        url = []

        info =  {"label":"TREKKIE TRAX","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報
        artistdb2 = []

        for artdb in trekkiedb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for artdb2 in releases.objects.filter(label='trekkie trax').order_by('id'):
            artistdb2.append(artdb2.url)

        for link in soup.find_all('div', style='text-align:center;'):
            link2 = link.find_all("a")
            for urls in link2:
                url.append(urls['href'])

        '''
        if len(url)>len(artistdb):
            #info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1
        '''

        if url[0]!=artistdb2[0]:
            #info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = trekkiedb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='trekkie trax')
        delete2.delete()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = trekkiedb(artist=at)
            db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label='trekkie trax')
            db.save()

        return info


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
        artistdb2 =[]

        for artdb in planetdb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for artdb2 in releases.objects.filter(label='planet mu').order_by('id'):
            artistdb2.append(artdb2.url)

        for bbr in soup.find_all(class_="box-inner"):
         ra = bbr.find_all(class_="release-artist")
         rt = bbr.find_all(class_="release-title")


         for art in ra:
              artist.append(art.text)
         for tit in rt:
              title.append(tit.text)
              for link in tit.find_all("a"):
                   url.append(link['href'])

        '''
        if url[0]!=artistdb[0]:
             info['title']=title[0]
             info['artist']=artist[0]
             info['url']=url[0]
             info['key']=1
        '''
        if url[0]!=artistdb2[0]:
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = planetdb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='planet mu')
        delete2.delete()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = planetdb(artist=at)
            db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label='planet mu')
            db.save()

        return info



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
        artistdb2 = []

        for artdb in warpdb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for artdb2 in releases.objects.filter(label='warp').order_by('id'):
            artistdb2.append(artdb2.url)

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
        '''
        if url[0]!=artistdb[0]:
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1
        '''
        if url[0]!=artistdb2[0]:
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = warpdb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='warp')
        delete2.delete()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = warpdb(artist=at)
            db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label='warp')
            db.save()

        return info



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
        artistdb2 = []

        for artdb in progressivedb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for artdb2 in releases.objects.filter(label='progressive form').order_by('id'):
            artistdb2.append(artdb2.url)

        for tit in soup.find_all(class_="itemTitle"):
          pre.append(tit.text)

        for i in range(len(pre)):
          b = pre[i].replace("\n","")
          title.append(b)

        for link in soup.find_all(class_="itemImg"):
         link2 = link.find_all("a")
         for urls in link2:
               url.append(urls['href'])
        '''
        if len(title)>len(artistdb):
            info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1
        '''
        if url[0]>artistdb2[0]:
            info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = progressivedb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='progressive form')
        delete2.delete()

        for i in range(len(url)):
            at = title[i]
            #tit = title[i]
            #ur =  url[i]
            db = progressivedb(artist=at)
            db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label='progressive form')
            db.save()

        return info



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
        artistdb2 = []

        for artdb in flaudb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for artdb2 in releases.objects.filter(label='flau').order_by('id'):
            artistdb2.append(artdb2.url)


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
        '''
        if len(artist)>len(artistdb):
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1
        '''

        if len(url)>len(artistdb2):
            if url[1]!=artistdb2[0]:
                info['title']=title[0]
                info['artist']=artist[0]
                info['url']=url[0] + "\n複数のリリースがあります"
                info['key']=1
            else:
                info['title']=title[0]
                info['artist']=artist[0]
                info['url']=url[0]
                info['key']=1

        delete = flaudb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='flau')
        delete2.delete()

        for i in range(len(url)):
            at = artist[i]
            #tit = title[i]
            #ur =  url[i]
            db = flaudb(artist=at)
            db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label='flau')
            db.save()

        return info



    def owsla(self):

       info =  {"label":"OWSLA","title":"","url":"","artist":"","key":0}

       artistdb = [] #dbから取得したアーティスト情報
       artistdb2 = []

       for artdb in owsladb.objects.all().order_by('id'):
           artistdb.append(artdb.artist)

       for artdb2 in releases.objects.filter(label='owsla').order_by('id'):
           artistdb2.append(artdb2.url)

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

       if url[0]!=artistdb2[0]:
           #info['title']=title[0]
           #info['artist']=artist[0]
           info['url']=url[0]
           info['key']=1

       delete = owsladb.objects.all()
       delete.delete()

       delete2 = releases.objects.filter(label='owsla')
       delete2.delete()

       for i in range(len(url)):
           at = url[i]
           #tit = title[i]
           #ur =  url[i]
           db = owsladb(artist=at)
           db.save()

       for i in range(len(url)):
           at = url[i]
           #tit = title[i]
           #ur =  url[i]
           db = releases(url=at,label='owsla')
           db.save()

       return info



    def revealed(self):

        info =  {"label":"Revealed Recordings","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報
        artistdb2 = []

        for artdb in revealeddb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for artdb2 in releases.objects.filter(label='revealed').order_by('id'):
            artistdb2.append(artdb2.url)


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
        '''
        if url[0]!=artistdb[0]:
            #info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1
        '''
        if url[0]!=artistdb2[0]:
            #info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = revealeddb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='revealed')
        delete2.delete()

        for i in range(len(url)):
           at = url[i]
            #tit = title[i]
            #ur =  url[i]
           db = revealeddb(artist=at)
           db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label='revealed')
            db.save()

        return info




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

        artist = ''
        p = soup.prettify()

        for link in soup.find_all("dl",class_="artist-releases"):
          for link2 in link.find_all("a"):
             preurl.append(link2['href'])
          for art in link.find_all("dd",class_="artist"):
             preartist.append(art.text)
          for tit in link.find_all("dd",class_="title"):
             pretitle.append(tit.text)


        delete2 = releases.objects.filter(label='ghostly international')
        delete2.delete()

        if len(preartist)>len(artistdb):
            #artist = set(preartist)-set(artistdb)
            title = set(pretitle)-set(titledb)
            url = set(preurl)-set(urldb)
            #artist = list(artist)
            title = list(title)
            url = list(url)

            for i in range(len(preurl)):
                if url[0] in preurl[i]:
                    artist = preartist[i]

            for i in range(len(url)):
                url[i] = 'http://ghostly.com'+url[i]

            info['title']=title[0]
            info['artist']=artist
            info['url']=url[0]
            info['key']=1

            ul = url[0]
            db2 = releases(label='ghostly international',url=ul)
            db2.save()

        else:
            ul = 'http://ghostly.com'+preurl[0]
            db2 = releases(label='ghostly international',url=ul)
            db2.save()



        delete = ghostlydb.objects.all()
        delete.delete()


        for i in range(len(preurl)):
            at = preartist[i]
            tit = pretitle[i]
            ur = preurl[i]
            db = ghostlydb(artist=at,title=tit,url=ur)
            db.save()



        return info




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
        artistdb2 = []

        for artdb in spinnindb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for artdb2 in releases.objects.filter(label="spinnin'").order_by('id'):
            artistdb2.append(artdb2.url)


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
        '''
        if title[0]!=artistdb[0]:
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1
        '''

        if url[0]!=artistdb2[0]:
            if url[1]!=artistdb2[0]:
              info['title']=title[0]
              info['artist']=artist[0]
              info['url']=url[0] + "\n複数のリリースがあります"
              info['key']=1
            else:
              info['title']=title[0]
              info['artist']=artist[0]
              info['url']=url[0]
              info['key']=1

        delete = spinnindb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label="spinnin'")
        delete2.delete()

        for i in range(len(url)):
            at = title[i]
            #tit = title[i]
            #ur =  url[i]
            db = spinnindb(artist=at)
            db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label="spinnin'")
            db.save()

        return info




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
        artistdb2 = []

        for artdb in wediditdb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for artdb2 in releases.objects.filter(label='wedidit').order_by('id'):
            artistdb2.append(artdb2.url)

        for link in soup.find_all(class_="releases-wrapper"):
           for link2 in link.find_all("a"):
              url.append(link2['href'])
           for art in link.find_all("h4"):
              artist.append(art.text)
           for tit in link.find_all("h3"):
              title.append(tit.text)

           '''
           if len(title)>len(artistdb):
               info['title']=title[0]
               info['artist']=artist[0]
               info['url']=url[0]
               info['key']=1
            '''

           if len(url)>len(artistdb2):
               info['title']=title[0]
               info['artist']=artist[0]
               info['url']=url[0]
               info['key']=1

        delete = wediditdb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='wedidit')
        delete2.delete()

        for i in range(len(url)):
            at = title[i]
            #tit = title[i]
            #ur =  url[i]
            db = wediditdb(artist=at)
            db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label='wedidit')
            db.save()

        return info




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
        artistdb2 = []

        for artdb in neverdb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for artdb2 in releases.objects.filter(label='never slept').order_by('id'):
            artistdb2.append(artdb2.url)


        for link in soup.find_all("div",class_="leftMiddleColumns"):
          for link2 in link.find_all("a"):
             url.append(link2['href'])

        for i in range(len(url)):
            url[i] = 'https://never-slept.bandcamp.com' + url[i]

        '''
        if len(url)>len(artistdb):
            #info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1
        '''

        if len(url)>len(artistdb2):
            #info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = neverdb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='never slept')
        delete2.delete()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = neverdb(artist=at)
            db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label='never slept')
            db.save()

        return info




    def mad(self):
        url = 'http://maddecent.com/music/'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        artist = []
        title = []
        url = []

        info =  {"label":"Mad Decent","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報
        artistdb2 = []

        for artdb2 in releases.objects.filter(label='mad decent').order_by('id'):
           artistdb2.append(artdb2.url)

        for artdb in maddb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for link in soup.find_all("a",class_="thumb-link"):
           url.append(link['href'])

        for tit in soup.find_all("h1",itemprop="name"):
           title.append(tit.text)

        for art in soup.find_all("h2",class_="artist-name"):
           artist.append(art.text)
        '''
        if title[0]!=artistdb[0]:
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1
        '''

        if url[0]!=artistdb2[0]:
            if url[1]!=artistdb2[0]:
                info['title']=title[0]
                info['artist']=artist[0]
                info['url']=url[0] + "\n複数のリリースがあります"
                info['key']=1
            else:
                info['title']=title[0]
                info['artist']=artist[0]
                info['url']=url[0]
                info['key']=1

        delete = maddb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='mad decent')
        delete2.delete()

        for i in range(len(url)):
            at = title[i]
            #tit = title[i]
            #ur =  url[i]
            db = maddb(artist=at)
            db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label='mad decent')
            db.save()

        return info




    def edbanger(self):
        url = 'http://www.edbangerrecords.com/site/'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        artist = []
        title = []
        url = []

        info =  {"label":"Ed Banger Records","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報
        artistdb2 = []

        for artdb in edbangerdb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for artdb2 in releases.objects.filter(label='ed banger').order_by('id'):
            artistdb2.append(artdb2.url)


        pre = []

        for h2 in soup.find_all("h2",class_="entry-title"):
            for art in h2.find_all("a"):
                pre.append(art.text)
                url.append(art['href'])


        for i in range(len(pre)):
            if "“" in pre[i]:
                p = pre[i].split(" “")
                artist.append(p[0])
                q = p[1].replace("”","")
                title.append(q)
            elif "« " in pre[i]:
                p = pre[i].split("« ")
                artist.append(p[0])
                q = p[1].replace(" »","")
                title.append(q)
            else:
                artist.append("")
                title.append(pre[i])

        '''
        if len(url)>len(artistdb):
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1
        '''

        if len(url)>len(artistdb2):
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = edbangerdb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='ed banger')
        delete2.delete()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = edbangerdb(artist=at)
            db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label='ed banger')
            db.save()

        return info




    def brainfeeder(self):
        url = 'http://www.brainfeedersite.com/'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        artist = []
        title = []
        url = []

        info =  {"label":"Brainfeeder","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報
        artistdb2 = []


        for artdb in brainfeederdb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for artdb2 in releases.objects.filter(label='brainfeeder').order_by('id'):
            artistdb2.append(artdb2.url)


        pre = []

        for pc in soup.find_all(class_='list clear',id='loop'):
            for h2 in pc.find_all('h2'):
                for a in h2.find_all('a'):
                    title.append(a.text)
                    url.append(a['href'])

        '''
        at = pre[0].split(" – ")
        artist.append(at[0])
        title.append(at[1])
        '''

        '''
        if url[0]!=artistdb[0]:
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1
        '''

        if url[0]!=artistdb2[0]:
            info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = brainfeederdb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='brainfeeder')
        delete2.delete()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = brainfeederdb(artist=at)
            db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label='brainfeeder')
            db.save()

        return info



    def luckyme(self):
        url = 'https://luckyme.bleepstores.com/'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        artist = []
        title = []
        url = []

        info =  {"label":"LuckyMe","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報
        artistdb2 = []


        for artdb in luckymedb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for artdb2 in releases.objects.filter(label='luckyme').order_by('id'):
            artistdb2.append(artdb2.url)

        for id in soup.find_all(id="2017"):
            for dd in id.find_all("dd",class_="artist "):
                for a in dd.find_all("a"):
                    artist.append(a['title'])

        for id2 in soup.find_all(id="2017"):
            for dd2 in id2.find_all("dd",class_="release-title"):
                for a2 in dd2.find_all("a"):
                    title.append(a2['title'])
                    url.append("https://luckyme.bleepstores.com/"+a2['href'])

        '''
        if len(url)>len(artistdb):
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1
         '''

        if len(url)>len(artistdb2):
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = luckymedb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='luckyme')
        delete2.delete()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = luckymedb(artist=at)
            db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label='luckyme')
            db.save()

        return info



    def rs(self):
        url = 'http://www.randsrecords.com/releases'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        artist = []
        title = []
        url = []

        info =  {"label":"R&S Records","title":"","url":"","artist":"","key":0}

        artistdb = [] #dbから取得したアーティスト情報
        artistdb2 = []

        for artdb in rsdb.objects.all().order_by('id'):
            artistdb.append(artdb.artist)

        for artdb2 in releases.objects.filter(label='r&s').order_by('id'):
            artistdb2.append(artdb2.url)

        for art in soup.find_all(class_="artist"):
          artist.append(art.text)

        for link in soup.find_all(class_="title"):
          url.append(link['href'])
          title.append(link.text)

        '''
        if title[0]!=artistdb[0]:
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1
        '''

        if url[0]!=artistdb2[0]:
            info['title']=title[0]
            info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = rsdb.objects.all()
        delete.delete()

        delete2 = releases.objects.filter(label='r&s')
        delete2.delete()

        for i in range(len(url)):
            at = title[i]
            #tit = title[i]
            #ur =  url[i]
            db = rsdb(artist=at)
            db.save()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label='r&s')
            db.save()

        return info



    def moose(self):
        url = 'http://www.moose-records.com/releases/'

        key = True
        while key:
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                response = urllib.request.urlopen(req)
                html = response.read()
                key = False
            except:
                pass

        soup = BeautifulSoup(html, "lxml")

        url = []

        artistdb = []


        info =  {"label":"Moose Records","title":"","url":"","artist":"","key":0}

        for artdb in releases.objects.filter(label='moose').order_by('id'):
            artistdb.append(artdb.url)



        for ul in soup.find_all(class_='image-slide-anchor content-fit'):
            if 'www.moose-records' in ul['href']:
                url.append(ul['href'])
            else:
                url.append('http://www.moose-records.com'+ul['href'])


        if len(url)>len(artistdb):
            #info['title']=title[0]
            #info['artist']=artist[0]
            info['url']=url[0]
            info['key']=1

        delete = releases.objects.filter(label='moose')
        delete.delete()

        for i in range(len(url)):
            at = url[i]
            #tit = title[i]
            #ur =  url[i]
            db = releases(url=at,label='moose')
            db.save()
        return info




    def anticon(self):

        url = 'https://www.anticon.com/store/music/anticon-releases'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")


        artist = []
        url = []
        title = []
        artistdb = []


        info =  {"label":"anticon.","title":"","url":"","artist":"","key":0}

        for artdb in releases.objects.filter(label='anticon').order_by('id'):
            artistdb.append(artdb.url)


        for tit in soup.find_all(class_='product-meta'):
             for h3 in tit.find_all('h3'):
                 artist.append(h3.text)
             for h4 in tit.find_all('h4'):
                 title.append(h4.text)

        for ul in soup.find_all(class_='product-image'):
            for a in ul.find_all('a'):
                url.append('https://www.anticon.com'+a['href'])


        if url[0]!=artistdb[0]:
            if url[1]!=artistdb[0]:
                info['title']=title[0]
                info['artist']=artist[0]
                info['url']=url[0] + "\n複数のリリースがあります"
                info['key']=1
            else:
                info['title']=title[0]
                info['artist']=artist[0]
                info['url']=url[0]
                info['key']=1

        delete = releases.objects.filter(label='anticon')
        delete.delete()

        for i in range(len(url)):
            at = url[i]
            db = releases(url=at,label='anticon')
            db.save()

        return info



    def orikami(self):
        url = 'https://orikamirecords.bandcamp.com/music'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")


        artist = []
        title = []
        url = []
        artistdb = []


        info =  {"label":"Orikami Records","title":"","url":"","artist":"","key":0}

        for artdb in releases.objects.filter(label='orikami').order_by('id'):
            artistdb.append(artdb.url)


        for pn in soup.find_all('p',class_='title'):
            for ex in pn.find_all('span'):
                ex.extract()
            tit = re.sub('\s{2}',"",pn.text.replace("\n",''))
            title.append(tit)

        for ol in soup.find_all('ol',class_="editable-grid music-grid columns-4 public"):
            for a in ol.find_all('a'):
                url.append('https://orikamirecords.bandcamp.com'+a['href'])

        if url[0]!=artistdb[0]:
            if url[1]!=artistdb[0]:
                info['title']=title[0]
                #info['artist']=artist[0]
                info['url']=url[0] + "\n複数のリリースがあります"
                info['key']=1
            else:
                info['title']=title[0]
                #info['artist']=artist[0]
                info['url']=url[0]
                info['key']=1

        delete = releases.objects.filter(label='orikami')
        delete.delete()

        for i in range(len(url)):
            at = url[i]
            db = releases(url=at,label='orikami')
            db.save()

        return info



    def ne(self):
        url = 'http://nerecords.tokyo/release.html'
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")


        artist = []
        title = []
        url = []
        artistdb = []


        info =  {"label":"neRecords","title":"","url":"","artist":"","key":0}

        for artdb in releases.objects.filter(label='ne').order_by('id'):
            artistdb.append(artdb.url)


        for ul in soup.find_all(class_='box'):
            for a in ul.find_all('a'):
                url.append('http://nerecords.tokyo/'+a['href'])
            for tit in ul.find_all(class_='title'):
                title.append(tit.text)

        if url[0]!=artistdb[0]:
            if url[1]!=artistdb[0]:
                info['title']=title[0]
                #info['artist']=artist[0]
                info['url']=url[0] + "\n複数のリリースがあります"
                info['key']=1
            else:
                info['title']=title[0]
                #info['artist']=artist[0]
                info['url']=url[0]
                info['key']=1

        delete = releases.objects.filter(label='ne')
        delete.delete()

        for i in range(len(url)):
            at = url[i]
            db = releases(url=at,label='ne')
            db.save()

        return info




    def doscraping(self,name):
        if name == 'altema':
           return self.altema()
        elif name == 'maltine':
            return self.maltine()
        elif name == 'bunkai-kei':
            return self.bunkai()
        elif name == 'trekkie trax':
            return self.trekkie()
        elif name == 'sense':
            return self.sense()
        elif name == 'flau':
            return self.flau()
        elif name == 'progressive form':
            return self.progressive()
        elif name == 'warp':
            return self.warp()
        elif name == 'planet mu':
            return self.planet()
        elif name == 'owsla':
            return self.owsla()
        elif name == 'revealed':
            return self.revealed()
        elif name == 'ghostly international':
            return self.ghostly()
        elif name == "spinnin'":
            return self.spinnin()
        elif name == 'wedidit':
            return self.wedidit()
        elif name == 'never slept':
            return self.never()
        elif name == 'mad decent':
            return self.mad()
        elif name == 'r&s':
            return self.rs()
        elif name == 'ed banger':
            return self.edbanger()
        elif name == 'brainfeeder':
            return self.brainfeeder()
        elif name == 'luckyme':
            return self.luckyme()
        elif name == 'moose':
            return self.moose()
        elif name == 'anticon':
            return self.anticon()
        elif name == 'orikami':
            return self.orikami()
        #elif name == 'ne':
         #   return self.ne()

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