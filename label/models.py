from django.db import models

# Create your models here.

class releases(models.Model):
    LABEL_SET = (
        ('no','no'),
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
    )
    label = models.CharField('Label',max_length=500,choices=LABEL_SET,default='no')
    url = models.CharField('URL',max_length=500)

    def __str__(self):
        return self.label


class altemadb(models.Model):
    artist =  models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist


class maltinedb(models.Model):
    artist =  models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist


class bunkaidb(models.Model):
    artist =  models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist


class sensedb(models.Model):
    artist =  models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist


class warpdb(models.Model):
    artist =  models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist


class planetdb(models.Model):
    artist =  models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist


class flaudb(models.Model):
    artist =  models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist


class progressivedb(models.Model):
    artist =  models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist

class trekkiedb(models.Model):
    artist =  models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist


class owsladb(models.Model):
    artist =  models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist


class revealeddb(models.Model):
    artist =  models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist



class ghostlydb(models.Model):
    artist = models.CharField('アーティスト名',max_length=500)
    title = models.CharField('タイトル',max_length=500)
    url = models.CharField('タイトル',max_length=500)

    def __str__(self):
        return self.artist



class spinnindb(models.Model):
    artist = models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist




class wediditdb(models.Model):
    artist = models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist



class neverdb(models.Model):
    artist = models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist



class maddb(models.Model):
    artist = models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist



class rsdb(models.Model):
    artist = models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist



class edbangerdb(models.Model):
    artist = models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist



class brainfeederdb(models.Model):
    artist = models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist



class luckymedb(models.Model):
    artist = models.CharField('アーティスト名',max_length=500)

    def __str__(self):
        return self.artist



class lineid(models.Model):
    user = models.CharField('userid',max_length=500)

    def __str__(self):
        return self.user


class diggerdb(models.Model):
    artist = models.CharField('userid',max_length=500)

    def __str__(self):
        return self.artist