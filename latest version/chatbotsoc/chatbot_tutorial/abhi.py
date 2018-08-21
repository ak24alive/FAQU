import re
import sqlite3
import pandas as pd
import datetime
import os
ridi=''
fat=''
b=[]
my_list=[]
m=''
fat=''
doub_list=[]
doubw=[]
foo = ['Moreover', 'Furthermore', 'Also', 'And']
counter=0
doubl=[]
doublr=[]
doubwords=[]
my_keys=[]
ans=[]
def driver(req):
    print("here"+req)
    global ridi
    global fat
    global b
    global my_list
    global m
    global fat
    global doub_list
    global doubw
    global foo 
    global counter
    ridi=''
    b=[]
    my_list=[]
    m=''
    doub_list=[]
    doubw=[]
    foo = ['Moreover', 'Furthermore', 'Also', 'And']
    counter=0
    fat=req
    from .  import wedontwant 
    from . import greetings 
    from . import actions 
    import random
    df=pd.read_excel('F:\Projects\chatbotSocket\chatbotsoc\chatbot_tutorial/doub.xlsx')
    bf=pd.read_excel('F:\Projects\chatbotSocket\chatbotsoc\chatbot_tutorial/doub_split.xlsx')
    global doubl
    global doublr
    global doubwords
    doubl=list(df['keys'])
    doublr=list(df['values'])
    doubwords=list(set(bf['splitkeys']))
    cf=pd.read_excel('F:\Projects\chatbotSocket\chatbotsoc\chatbot_tutorial/datasetr.xlsx')
    global my_keys
    my_keys=list(cf['keys'])
    global ans
    ans=list(cf['values'])


    def compute(index,type):
        global ans
        global doublr
        if type==0:
            l=ans[index]
        else:
            l=doublr[index]
        global ridi
        ridi=ridi+'<br>'+l
        return
    def check():
        global b
        global doub_list
        global doubw
        global doubwords
        global doubl
        doubw=[]
        doub_list=[]
        for x in b:
            if(doubwords.__contains__(x)):
                doubw.append(x)
        for x in doubw:
            for y in doubw:
                if(x!=y):
                    m=x+' '+y
                    if(doubl.__contains__(m)):
                        doub_list.append(m)
        return
    def query(counter,type):
        global b
        global ridi
        global doubl
        global doublr
        global doub_list
        global fat
        global my_list
        if(type==1):
            global my_list
            c=my_list[counter]
            countnact=0
            countns=0
            for x in b:
                if (actions.nact).__contains__(x):
                    countnact+=1
                if (actions.not_sure).__contains__(x):
                    countns+=1
            if(countnact==0):
                if(countns==0):
                    compute(my_keys.index(c),0)
                else:
                    ridi=ridi+'<br>Well why not??'+'<br>I can tell you all you need to know about '+c+'<br>Do you want to know about it??'
                    print('Well why not??')
                    print('I can tell you all you need to know about '+c)
                    print('Do you want to know about it??')
                    con=sqlite3.Connection('users')
                    cur=con.cursor()
                    cur.execute("update "+fat+" set data='"+ridi+"' where flag=1")
                    con.commit()
                    cur.execute('update '+fat+' set flag=0 where flag=1')
                    con.commit()
                    while True:
                        cur.execute('select * from '+fat)
                        l=cur.fetchone()
                        if l[0]==1:
                            break
                    print('success')
                    cur.close()
                    con=sqlite3.Connection('users')
                    cur=con.cursor()
                    cur.execute('drop table if exists '+fat)
                    cur.execute('create table if not exists '+fat+' (flag int(5),data varchar(10000))')
                    cur.execute('insert into '+fat+' values(?,?)',(0,'NULL'))
                    con.commit()
                    while True:
                        cur.execute('select * from '+fat)
                        l=cur.fetchone()
                        if l[0]==1:
                            break
                    print('success')
                    con.commit()
                    cur.close()
                    temp=l[1]
                    temp=temp.lower()
                    ridi=''
                    flag=-1
                    print('')
                    if(temp=='y' or temp=='y '):
                        flag=1
                    if(temp=='n' or temp=='n '):
                        flag=0
                    if(flag==-1):
                        count1=0
                        right=[x for x in re.split('\W',temp) if x]
                        for x in right:
                            if (wedontwant.those_words).__contains__(x):
                                count1+=1
                        if count1>0:
                            ridi=ridi+'<br>Please don&apos;t abuse!!!<br>We at JUET don&apos;t tolerate it!!'
                            print('Please don\'t abuse!!! We at JUET don\'t tolerate it!!')
                            return
                        if(right.__contains__('yes') or right.__contains__('yup')):
                            flag=1
                        if(right.__contains__('no') or right.__contains__('nope')):
                            flag=0
                    if(flag==0):
                        ridi=ridi+'<br>Maybe I misunderstood you.<br>For this query you can contact the reception to get your answer.<br>The number is: 9876543210'
                        print('Maybe I misunderstood you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
                    elif(flag==1):
                        compute(my_keys.index(c),0)
                    else:
                        ridi=ridi+'<br>Sorry I don&apos;t understand you.<br>For this query you can contact the reception to get your answer.<br>The number is: 9876543210'
                        print('Sorry I don\'t understand you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
            else:
                flag=-1
                ridi=ridi+'<br>You mentioned '+c+'<br>But I am not sure if you really want to know about it.'+'<br>Would you like to know about it??'
                print('You mentioned '+c)
                print('But I am not sure if you really want to know about it.')
                print('Would you like to know about it??')
                con=sqlite3.Connection('users')
                cur=con.cursor()
                cur.execute("update "+fat+" set data='"+ridi+"' where flag=1")
                con.commit()
                cur.execute('update '+fat+' set flag=0 where flag=1')
                con.commit()
                while True:
                    cur.execute('select * from '+fat)
                    #con.commit()
                    l=cur.fetchone()
                    if l[0]==1:
                        break
                print('success')
                cur.close()
                con=sqlite3.Connection('users')
                cur=con.cursor()
                cur.execute('drop table if exists '+fat)
                con.commit()
                cur.execute('create table if not exists '+fat+' (flag int(5),data varchar(10000))')
                cur.execute('insert into '+fat+' values(?,?)',(0,'NULL'))
                con.commit()
                while True:
                    cur.execute('select * from '+fat)
                    l=cur.fetchone()
                    if l[0]==1:
                        break
                print('success')
                con.commit()
                cur.close()
                temp=l[1]
                temp=temp.lower()
                ridi=''
                print('')
                if(temp=='y' or temp=='y '):
                    flag=1
                if(temp=='n' or temp=='n '):
                    flag=0
                if(flag==-1):
                    count1=0
                    right=[x for x in re.split('\W',temp) if x]
                    for x in right:
                        if (wedontwant.those_words).__contains__(x):
                            count1+=1
                    if count1>0:
                        ridi=ridi+'<br>Please don&apos;t abuse!!!<br>We at JUET don&apos;t tolerate it!!'
                        print('Please don\'t abuse!!! We at JUET don\'t tolerate it!!')
                        return
                    if(right.__contains__('yes') or right.__contains__('yup')):
                        flag=1
                    if(right.__contains__('no') or right.__contains__('nope')):
                        flag=0
                if(flag==0):
                    ridi=ridi+'<br>Maybe I misunderstood you.<br>For this query you can contact the reception to get your answer.<br>The number is: 9876543210'
                    print('Maybe I misunderstood you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
                elif(flag==1):
                    compute(my_keys.index(c),0)
                else:
                    ridi=ridi+'<br>Sorry I don&apos;t understand you.<br>For this query you can contact the reception to get your answer.<br>The number is: 9876543210'
                    print('Sorry I don\'t understand you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
        else:
            c=doub_list[counter]
            countnact=0
            countns=0
            for x in b:
                if (actions.nact).__contains__(x):
                    countnact+=1
                if (actions.not_sure).__contains__(x):
                    countns+=1
            if(countnact==0):
                if(countns==0):
                    compute(doubl.index(c),1)
                else:
                    ridi=ridi+'<br>Well why not??'+'<br>I can tell you all you need to know about '+c+'<br>Do you want to know about it??'
                    print('Well why not??')
                    print('I can tell you all you need to know about '+c)
                    print('Do you want to know about it??')
                    flag=-1
                    con=sqlite3.Connection('users')
                    cur=con.cursor()
                    cur.execute("update "+fat+" set data='"+ridi+"' where flag=1")
                    con.commit()
                    cur.execute('update '+fat+' set flag=0 where flag=1')
                    con.commit()
                    while True:
                        cur.execute('select * from '+fat)
                        #con.commit()
                        l=cur.fetchone()
                        if l[0]==1:
                            break
                    print('success')
                    cur.execute('drop table if exists '+fat)
                    #con.commit()
                    cur.close()
                    con=sqlite3.Connection('users')
                    cur=con.cursor()
                    cur.execute('drop table if exists '+fat)
                    con.commit()
                    cur.execute('create table if not exists '+fat+' (flag int(5),data varchar(10000))')
                    cur.execute('insert into '+fat+' values(?,?)',(0,'NULL'))
                    con.commit()
                    while True:
                        cur.execute('select * from '+fat)
                        l=cur.fetchone()
                        if l[0]==1:
                            break
                    print('success')
                    con.commit()
                    cur.close()
                    temp=l[1]
                    temp=temp.lower()
                    ridi=''
                    print('')
                    if(temp=='y' or temp=='y '):
                        flag=1
                    if(temp=='n' or temp=='n '):
                        flag=0
                    if(flag==-1):
                        count1=0
                        right=[x for x in re.split('\W',temp) if x]
                        for x in right:
                            if (wedontwant.those_words).__contains__(x):
                                count1+=1
                        if count1>0:
                            ridi=ridi+'<br>Please don&apos;t abuse!!!<br>We at JUET don&apos;t tolerate it!!'
                            print('Please don\'t abuse!!! We at JUET don\'t tolerate it!!')
                            return
                        if(right.__contains__('yes') or right.__contains__('yup')):
                            flag=1
                        if(right.__contains__('no') or right.__contains__('nope')):
                            flag=0
                    if(flag==0):
                        ridi=ridi+'<br>Maybe I misunderstood you.<br>For this query you can contact the reception to get your answer.<br>The number is: 9876543210'
                        print('Maybe I misunderstood you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
                    elif(flag==1):
                        compute(doubl.index(c),1)
                    else:
                        ridi=ridi+'<br>Sorry I don&apos;t understand you.<br>For this query you can contact the reception to get your answer.<br>The number is: 9876543210'
                        print('Sorry I don\'t understand you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
            else:
                flag=-1
                ridi=ridi+'<br>You mentioned '+c+'<br>But I am not sure if you really want to know about it.'+'<br>Would you like to know about it??'
                print('You mentioned '+c)
                print('But I am not sure if you really want to know about it.')
                print('Would you like to know about it??')
                con=sqlite3.Connection('users')
                cur=con.cursor()
                cur.execute("update "+fat+" set data='"+ridi+"' where flag=1")
                con.commit()
                cur.execute('update '+fat+' set flag=0 where flag=1')
                con.commit()
                while True:
                    cur.execute('select * from '+fat)
                    l=cur.fetchone()
                    if l[0]==1:
                        break
                print('success')
                cur.close()
                con=sqlite3.Connection('users')
                cur=con.cursor()
                cur.execute('drop table if exists '+fat)
                con.commit()
                cur.execute('create table if not exists '+fat+' (flag int(5),data varchar(10000))')
                cur.execute('insert into '+fat+' values(?,?)',(0,'NULL'))
                con.commit()
                while True:
                    cur.execute('select * from '+fat)
                    l=cur.fetchone()
                    if l[0]==1:
                        break
                print('success')
                con.commit()
                cur.close()
                temp=l[1]
                temp=temp.lower()
                ridi=''
                print('')
                if(temp=='y' or temp=='y '):
                    flag=1
                if(temp=='n' or temp=='n '):
                    flag=0
                if(flag==-1):
                    count1=0
                    right=[x for x in re.split('\W',temp) if x]
                    for x in right:
                        if (wedontwant.those_words).__contains__(x):
                            count1+=1
                    if count1>0:
                        ridi=ridi+'<br>Please don&apos;t abuse!!!<br>We at JUET don&apos;t tolerate it!!'
                        print('Please don\'t abuse!!! We at JUET don\'t tolerate it!!')
                        return
                    if(right.__contains__('yes') or right.__contains__('yup')):
                        flag=1
                    if(right.__contains__('no') or right.__contains__('nope')):
                        flag=0
                if(flag==0):
                    ridi=ridi+'<br>Maybe I misunderstood you.<br>For this query you can contact the reception to get your answer.<br>The number is: 9876543210'
                    print('Maybe I misunderstood you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
                elif(flag==1):
                    compute(doubl.index(c),1)
                else:
                    ridi=ridi+'<br>Sorry I don&apos;t understand you.<br>For this query you can contact the reception to get your answer.<br>The number is: 9876543210'
                    print('Sorry I don\'t understand you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
        return
    def main_like():
        global fat
        global ridi
        print('')
        print("fdgd"+fat)
        con=sqlite3.Connection('users')
        cur=con.cursor()
        cur.execute('drop table if exists "'+fat+'"')
        con.commit()
        cur.execute('create table if not exists "'+fat+'" (flag int(5),data varchar(10000))')
        cur.execute('insert into "'+fat+'" values(?,?)',(0,'NULL'))
        con.commit()
        while True:
            cur.execute('select * from "'+fat+'"')
            #con.commit()
            l=cur.fetchone()
            if l[0]==1:
                break
        print('success')
        con.commit()
        cur.close()
        a=l[1]
        a=a.replace("`","'")
        a=a.lower()
        print("fbfb")
        print(a)
        print('')
        if(a==''):
            main_like()
            return
        global b
        b=[x for x in re.split('\W',a) if x]
        y=len(b)
        for i in range(0,y):
            if(i<y-1 and (actions.weird).__contains__(b[i]) and b[i+1]=='t'):
                del b[i+1]
                b[i]=b[i]+"'"+"t"
        count1=0
        for x in b:
            if (wedontwant.those_words).__contains__(x):
                count1+=1
        if(a=='null'):
            ridi='NULL'
            con=sqlite3.Connection('users')
            cur=con.cursor()
            cur.execute("update '"+fat+"' set data='"+ridi+"' where flag=1")
            con.commit()
            cur.execute('update "'+fat+'" set flag=0 where flag=1')
            con.commit()
            while True:
                cur.execute('select * from "'+fat+'"')
                l=cur.fetchone()
                if l[0]==1:
                    break
            print('success')
            cur.close()
        elif count1==0:
            chatbatter(b)
        else:
            ridi="Please don&apos;t abuse!!!<br>We at JUET don&apos;t tolerate it!!"
            con=sqlite3.Connection('users')
            cur=con.cursor()
            cur.execute("update '"+fat+"' set data='"+ridi+"' where flag=1")
            con.commit()
            cur.execute('update "'+fat+'" set flag=0 where flag=1')
            con.commit()
            while True:
                cur.execute('select * from "'+fat+'"')
                l=cur.fetchone()
                if l[0]==1:
                    break
            print('success')
            cur.close()
            print("Please don't abuse!!! We at JUET don't tolerate it!!")
        return
    def chatbatter(b):
        global ridi
        global fat
        global doub_list
        global foo
        ridi=''
        count2=0
        for x in b:
            if (greetings.greet).__contains__(x):
                c=x
                count2+=1
        if count2!=0:
            ridi=(greetings.greet)[c]
            print((greetings.greet)[c])
        count=0
        global my_list
        my_list=[]
        for x in b:
            if my_keys.__contains__(x) and (not(doub_list.__contains__(x))):
                my_list.append(x)
        my_list=list(set(my_list))
        count=len(my_list)
        check()
        doub_list=list(set(doub_list))
        if (len(doub_list)>0):
            yo=0
            length=len(doub_list)
            if(len(doub_list)==1):
                query(yo,2)
            else:
                for x in doub_list:
                    if(yo!=0 and yo!=length-1):
                        ridi=ridi+'<br>'+random.choice(foo)+','
                        print(random.choice(foo)+',')
                    if(yo!=length-1):
                        query(yo,2)
                    yo+=1
            if(count>0):
                ohcomeon_list=[]
                for y in doub_list:
                    p=y.split()
                    ohcomeon_list.append(p[0])
                    ohcomeon_list.append(p[1])
                ohcomeon_list=list(set(ohcomeon_list))
                hellno=[]
                for x in my_list:
                    if(not ohcomeon_list.__contains__(x)):
                        hellno.append(x)
                length=len(hellno)
                yo=0
                my_list=hellno
                if(len(doub_list)>1):
                    if(len(hellno)):
                        ridi=ridi+'<br>'+"Also,"
                        print("Also,")
                    else:
                        ridi=ridi+'<br>'+"Lastly,"
                        print("Lastly,")
                    query(len(doub_list)-1,2)
                for x in hellno:
                    if(yo==length-1):
                        ridi=ridi+'<br>'+"Lastly,"
                        print("Lastly,")
                    else:
                        ridi=ridi+'<br>'+random.choice(foo)+','
                        print(random.choice(foo)+',')
                    query(yo,1)
                    yo+=1
            else:
                if(len(doub_list)!=1):
                    ridi=ridi+'<br>'+"Lastly,"
                    query(len(doub_list)-1,2)

        elif count==1:
            query(0,1)
        elif count==0 and count2==0:
            ridi=ridi+'<br>'+"Sorry i don&apos;t understand you.<br>You can call the college reception to get your answer.<br>The number is: 9876543210."
            print("Sorry i don't understand you.\nYou can call the college reception to get your answer.\nThe number is: 9876543210.")
        elif count2!=0:
            ridi=ridi+' &nbsp;'+"You can ask me queries related to new admissions.I can also tell you about Faculty members and placements!!"
            print('You can ask me queries related to new admissions.\nI can also tell you about Faculty members and placements!!')
        else:
            for yo in range(0,count):
                if(yo==count-1):
                    ridi=ridi+'<br>'+"Lastly,"
                    print("Lastly,")
                elif(yo!=0):
                    ridi=ridi+'<br>'+random.choice(foo)+','
                    print(random.choice(foo)+',')
                query(yo,1)
        if(ridi!=''):
            con=sqlite3.Connection('users')
            cur=con.cursor()
            cur.execute("update "+fat+" set data='"+ridi+"' where flag=1")
            con.commit()
            cur.execute('update '+fat+' set flag=0 where flag=1')
            con.commit()
            while True:
                cur.execute('select * from '+fat)
                l=cur.fetchone()
                if l[0]==1:
                    break
            print('success')
            cur.close()
        return
    print('======================= Welcome to JUET FAQ Service ========================')
    print('========================= I am a Reception Bot!!! ==========================')
    print("====================I'll be taking new admission queries====================")
    print("==You can also ask me about courses offered, placement and faculty members==")
    print('================== Please try to make meaningful Queries ===================')
    print('============================ I am still learning ===========================')
    print("How may I help you?")
    while True:
        ridi=''
        main_like()

