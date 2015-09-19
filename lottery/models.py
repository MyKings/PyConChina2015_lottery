# coding: utf-8

from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    # 是否中奖, 1 为中奖，0为没中奖
    isWin = models.IntegerField()


class Result(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    hours = models.IntegerField()