from django.db import models

# Create your models here.


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



class lineid(models.Model):
    user = models.CharField('userid',max_length=500)

    def __str__(self):
        return self.user


class diggerdb(models.Model):
    artist = models.CharField('userid',max_length=500)

    def __str__(self):
        return self.artist