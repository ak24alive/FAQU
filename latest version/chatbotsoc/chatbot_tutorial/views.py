from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import sqlite3
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
import xlsxwriter
from . import abhi
import os
fatt=''
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_port(request):
    if 'SERVER_PORT' in request.META:
        return request.META['SERVER_PORT']
    else:
        return None



def run_file(request):
    #from . import abhi
    print("xxxxxx")
    ip1= get_client_ip(request)
    port_run=get_port(request)
    #print(ip1)
    #print(port_run)
    global fatt
    fatt='a'
    lister=ip1.split('.')
    for x in lister:
        fatt=fatt+x
    lister=port_run.split('.')
    for x in lister:
        fatt=fatt+x
    #fatt=ip1+"."+port_run
    print("WWWWWWWWWWWWWWWWWWWWWwWOWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
    abhi.driver(fatt)
    return HttpResponse("")

def chat(request):
    xxx=get_client_ip(request)
    #print("harsh")
    #print(xxx)
    ip1= get_client_ip(request)
    port_run=get_port(request)
    global fatt
    fatt='a'
    lister=ip1.split('.')
    for x in lister:
        fatt=fatt+x
    lister=port_run.split('.')
    for x in lister:
        fatt=fatt+x
    
    context = {"sockVar":fatt}
    return render(request, 'chatbot_tutorial/chatbot.html', context)


def respond_to_websockets(message):
#def respond_to_websockets(message,request):
    jokes = {
     'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
     'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
     'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
     }
    #print()
    #print("aa rha hai")   
    #print(message['text'])
    #print(ip1)
    #print(port_run)
    flug=0
    while True:
        global fatt
        result_message = {
            'type': 'text'
        }
        fatt=message['sock']
        print("hgfhdsvhgfh   "+fatt)
        con=sqlite3.Connection('users')
        cur=con.cursor()
        cur.execute('create table if not exists "'+fatt+'" (flag int(5),data varchar(10000))')
        #cur.execute('insert into "'+fatt+'" values(?,?)',(0,'NULL'))
        con.commit()
        a=message['text']
        a=a.replace("'","`")
        if(a.lower()=='null'):
            result_message['text']="Sorry i don&apos;t understand you.<br>You can call the college reception to get your answer.<br>The number is: 9876543210."
            return result_message
        if(flug==1):
            while True:
                try:
                    cur.execute('select * from "'+fatt+'"')
                    l=cur.fetchone()
                    if l[0]==0:
                        break
                except e:
                    pass
        '''
        i=0
        for x in a:
            if(x=="'" or x=='"'):
                a=a[0:i]+'\\'+a[i:]
            i+=1
        '''
        print(a)
        cur.execute("update '"+fatt+"' set data='"+a+"' where flag=0")
        cur.execute('update "'+fatt+'" set flag=1 where flag=0')
        con.commit()
        while True:
            cur.execute('select * from "'+fatt+'"')
            l=cur.fetchone()
            if l[0]==0:
                result_message['text']=l[1]
                #cur.execute("update '"+fatt+"' set data='"+a+"' where flag=0")
                cur.execute('update "'+fatt+'" set flag=1 where flag=0')
                con.commit()
                if(result_message['text']=='NULL'):
                    flug=1
                    cur.execute('update "'+fatt+'" set flag=1 where flag=0')
                    con.commit()
                    cur.close()
                    break
                else:
                    con.commit()
                return result_message
'''
def new(request):
#def respond_to_websockets(message,request):
    global fatt
    fatt='a'
    lister=ip1.split('.')
    for x in lister:
        fatt=fatt+x
    lister=port_run.split('.')
    for x in lister:
        fatt=fatt+x
    return redirect("/new")
        #cur.execute('drop table if exists '+fatt)
    #os.remove('users')
    #ansh=message['text']
    if 'fat' in message['text']:
        result_message['text'] = random.choice(jokes['fat'])
    
    elif 'stupid' in message['text']:
        result_message['text'] = random.choice(jokes['stupid'])
    
    elif 'dumb' in message['text']:
        result_message['text'] = random.choice(jokes['dumb'])

    elif message['text'] in ['hi', 'hey', 'hello']:
        result_message['text'] = "Hello to you too! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and i'll tell you an appropriate joke."
    else:
        result_message['text'] = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, stupid or dumb."
    '''
    