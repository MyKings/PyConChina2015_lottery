# coding: utf-8

from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

from lottery.models import Person
from lottery.models import Result
from lottery.common import filterTel

import json
import time

def index(request):
    user_obj_list = Person.objects.filter(isWin=0)
    user_list = []
    for user_obj in user_obj_list:
        tel = filterTel(user_obj.tel)
        user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel})
    return render(request, 'index.html', {
        'userlist': json.dumps(user_list)
    })


def update(request):
    uid = request.GET['uid']
    try:
        hour = time.strftime('%H', time.localtime(time.time()))
        uid = int(uid)
        p = Person.objects.get(id=uid)
        Person.objects.filter(id=uid).update(isWin=1)
        Result.objects.create(uid=uid, name=p.name,tel=p.tel, hours=hour)
        return HttpResponse(1)
    except Exception, e:
        raise e
        return HttpResponse(0)


def get(request):
    user_obj_list = Person.objects.filter(isWin=0)
    user_list = []
    for user_obj in user_obj_list:
        tel = filterTel(user_obj.tel)
        user_list.append({'id': user_obj.id, 'name': user_obj.name, 'tel': tel})
    return HttpResponse(json.dumps(user_list))


def syr(request):
    user_obj_list = Person.objects.filter(isWin=0)
    return HttpResponse(len(user_obj_list))

def zjr(request):
    user_zjr_list = Person.objects.filter(isWin=1)
    return HttpResponse(len(user_zjr_list))