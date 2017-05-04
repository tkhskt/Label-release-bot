from django.db import models

# Create your models here.




class releases(models.Model):
    LABEL_SET = (
        ('--','--'),
        ('altema','Altema Records'),
        ('maltine','Maltine Records'),
        ('bunkai-kei','Bunkai-Kei Records'),
        ('trekkie trax','TREKKIE TRAX'),
        ('sense','SenSe'),
        ('flau','flau'),
        ('progressive form','PROGRESSIVE FOrM'),
        ('warp','Warp Records'),
        ('planet mu','Planet Mu'),
        ('owsla','OWSLA'),
        ('revealed','Revealed Recordings'),
        ('ghostly international','Ghostly International'),
        ("spinnin'","Spinnin' Records"),
        ('wedidit','WEDIDIT'),
        ('never slept','Never Slept'),
        ('mad decent','Mad Decent'),
        ('r&s','R&S Records'),
        ('ed banger','Ed Banger Records'),
        ('brainfeeder','brainfeeder'),
        ('luckyme','luckyme'),
        ('moose','Moose Records'),
        ('anticon','anticon.'),
        ('orikami','Orikami Records'),
        ('ne','neRecords'),
        ('outlier','OUTLIER RECORDINGS'),
        ('king','King Deluxe'),
        ('gondwana','Gondwana Records'),
        ('alphaversion','AlphaVersion Records'),
        ('eklektik','EKLEKTIK RECORDS'),
    )
    label = models.CharField('Label',max_length=500,choices=LABEL_SET,default='--')
    url = models.CharField('URL',max_length=500)

    def __str__(self):
        return self.label



class update(models.Model):
    label = models.CharField('Label',max_length=500,default='no')
    url = models.CharField('URL',max_length=500)
    date = models.DateField('Date',auto_now=True)

    def __str__(self):
        strd = self.date.strftime('%Y/%m/%d')
        return strd


class maltinedb(models.Model):
    artist =  models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist



class ghostlydb(models.Model):
    artist = models.CharField('アーティスト名',max_length=500)
    title = models.CharField('タイトル',max_length=500)
    url = models.CharField('タイトル',max_length=500)

    def __str__(self):
        return self.artist


class lineid(models.Model):
    user = models.CharField('userid',max_length=500)

    def __str__(self):
        return self.user

