import re
from dataset import ans
from wedontwant import those_words
from greetings import greet
from actions import weird
from actions import not_sure
from doub import doubl
from doub import doublr
from doub import doubwords
import random
from actions import pact
from actions import nact
b=[]
my_list=[]
m=''
doub_list=[]
doubw=[]
foo = ['Moreover', 'Furthermore', 'Also', 'And']
counter=0
def check():
    global b
    global doub_list
    global doubw
    doubw=[]
    doub_list=[]
    for x in b:
        if(doubwords.__contains__(x)):
            doubw.append(x)
    for x in doubw:
        for y in doubw:
            if(x!=y):
                global m
                m=x+' '+y
                if(doubl.__contains__(m)):
                    doub_list.append(m)
    return
def query(counter,type):
    global b
    if(type==1):
        global my_list
        c=my_list[counter]
        #countpact=0
        countnact=0
        countns=0
        #print('You mentioned '+c)
        for x in b:
            #if pact.__contains__(x):
                #countpact+=1
            if nact.__contains__(x):
                countnact+=1
            if not_sure.__contains__(x):
                countns+=1
        #if(pact>=1):
            #print(ans[c])
        if(countnact==0):
            if(countns==0):
                print(ans[c])
            else:
                print('Well why not??')
                print('I can tell you all you need to know about '+c)
                print('Do you want to know about it??')
                flag=-1
                temp=input().lower()
                if(temp=='y' or temp=='y '):
                    flag=1
                if(temp=='n' or temp=='n '):
                    flag=0
                if(flag==-1):
                    count1=0
                    right=[x for x in re.split('\W',temp) if x]
                    for x in right:
                        if those_words.__contains__(x):
                            count1+=1
                    if count1>0:
                        print('Please don\'t abuse!!! We at JUET don\'t tolerate it!!')
                        return
                    if(right.__contains__('yes') or right.__contains__('yup')):
                        flag=1
                    if(right.__contains__('no') or right.__contains__('nope')):
                        flag=0
                if(flag==0):
                    print('Maybe I misunderstood you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
                elif(flag==1):
                    print(ans[c])
                else:
                    print('Sorry I don\'t understand you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
        else:
            flag=-1
            print('You mentioned '+c)
            print('But I am not sure if you really want to know about it.')
            print('Would you like to know about it??')
            temp=input().lower()
            if(temp=='y' or temp=='y '):
                flag=1
            if(temp=='n' or temp=='n '):
                flag=0
            if(flag==-1):
                count1=0
                right=[x for x in re.split('\W',temp) if x]
                for x in right:
                    if those_words.__contains__(x):
                        count1+=1
                if count1>0:
                    print('Please don\'t abuse!!! We at JUET don\'t tolerate it!!')
                    return
                if(right.__contains__('yes') or right.__contains__('yup')):
                    flag=1
                if(right.__contains__('no') or right.__contains__('nope')):
                    flag=0
            if(flag==0):
                print('Maybe I misunderstood you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
            elif(flag==1):
                print(ans[c])
            else:
                print('Sorry I don\'t understand you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
    else:
        global doub_list
        c=doub_list[counter]
        #countpact=0
        countnact=0
        countns=0
        #print('You mentioned '+c)
        for x in b:
            #if pact.__contains__(x):
                #countpact+=1
            if nact.__contains__(x):
                countnact+=1
            if not_sure.__contains__(x):
                countns+=1
        #if(pact>=1):
            #print(ans[c])
        if(countnact==0):
            if(countns==0):
                print(doublr[c])
            else:
                print('Well why not??')
                print('I can tell you all you need to know about '+c)
                print('Do you want to know about it??')
                flag=-1
                temp=input().lower()
                if(temp=='y' or temp=='y '):
                    flag=1
                if(temp=='n' or temp=='n '):
                    flag=0
                if(flag==-1):
                    count1=0
                    right=[x for x in re.split('\W',temp) if x]
                    for x in right:
                        if those_words.__contains__(x):
                            count1+=1
                    if count1>0:
                        print('Please don\'t abuse!!! We at JUET don\'t tolerate it!!')
                        return
                    if(right.__contains__('yes') or right.__contains__('yup')):
                        flag=1
                    if(right.__contains__('no') or right.__contains__('nope')):
                        flag=0
                if(flag==0):
                    print('Maybe I misunderstood you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
                elif(flag==1):
                    print(doublr[c])
                else:
                    print('Sorry I don\'t understand you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
        else:
            flag=-1
            print('You mentioned '+c)
            print('But I am not sure if you really want to know about it.')
            print('Would you like to know about it??')
            temp=input().lower()
            if(temp=='y' or temp=='y '):
                flag=1
            if(temp=='n' or temp=='n '):
                flag=0
            if(flag==-1):
                count1=0
                right=[x for x in re.split('\W',temp) if x]
                for x in right:
                    if those_words.__contains__(x):
                        count1+=1
                if count1>0:
                    print('Please don\'t abuse!!! We at JUET don\'t tolerate it!!')
                    return
                if(right.__contains__('yes') or right.__contains__('yup')):
                    flag=1
                if(right.__contains__('no') or right.__contains__('nope')):
                    flag=0
            if(flag==0):
                print('Maybe I misunderstood you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
            elif(flag==1):
                print(doublr[c])
            else:
                print('Sorry I don\'t understand you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
    return
def main_like():
    a=input().lower()
    #a=a+' '
    if(a==''):
        main_like()
        return
    global b
    b=[x for x in re.split('\W',a) if x]
    y=len(b)
    for i in range(0,y):
        if(i<y-1 and weird.__contains__(b[i]) and b[i+1]=='t'):
            del b[i+1]
            b[i]=b[i]+"'"+"t"
    count1=0
    for x in b:
        if those_words.__contains__(x):
            count1+=1
    if count1==0:
        chatbatter(b)
    else:
        print('Please don\'t abuse!!! We at JUET don\'t tolerate it!!')
    return
def chatbatter(b):
    count2=0
    for x in b:
        if greet.__contains__(x):
            c=x
            count2+=1
    if count2!=0:
        print(greet[c])
    count=0
    global my_list
    my_list=[]
    for x in b:
        if ans.__contains__(x):
            my_list.append(x)
    my_list=list(set(my_list))
    count=len(my_list)
    global doub_list
    global foo
    check()
    if (len(doub_list)>0):
        yo=0
        length=len(doub_list)
        if(len(doub_list)==1):
            query(yo,2)
        else:
            for x in doub_list:
                if(yo!=0):
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
                    print("Also,")
                else:
                    print("Lastly,")
                query(len(doub_list)-1,2)
            for x in hellno:
                if(yo==length-1):
                    print("Lastly,")
                else:
                    print(random.choice(foo)+',')
                query(yo,1)
                yo+=1
    elif count==1:
        query(0,1)
    elif count==0 and count2==0:
        print("Sorry i don't understand you.\nYou can call the college reception to get your answer.\nThe number is: 9876543210.")
    elif count2!=0:
        print('You can ask me queries related to new admissions.\nI can also tell you about Faculty members and placements!!')
    else:
        for yo in range(0,count):
            if(yo==count-1):
                print("Lastly,")
            elif(yo!=0):
                print(random.choice(foo)+',')
            query(yo,1)
    return
print('======================= Welcome to JUET FAQ Service ========================')
print('========================= I am a Reception Bot!!! ==========================')
print("====================I'll be taking new admission queries====================")
print("==You can also ask me about courses offered, placement and faculty members==")
print('================== Please try to make meaningful Queries ===================')
print('============================ I am still learning ===========================')
print("How may I help you?")
while True:
    main_like()

