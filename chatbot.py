import re
from dataset import words
from wedontwant import those_words
from greetings import greet
from doub import doubl
from doub import doublr
b=[]
my_list=[]
m=''
def check(b):
    #count3=0
    for x in b:
        for y in b:
            if(x!=y):
                global m
                m=x+' '+y
                if(doubl.__contains__(m)):
                    #print("Come on Roger")
                    return True
    return False
def main_like():
    a=input().lower()
    b=[x for x in re.split('\W',a) if x]
    count1=0
    for x in b:
        if those_words.__contains__(x):
            count1+=1
    if count1==0:
        chatbattter(b)
    else:
        print('Please don\'t abuse!!! We at JUET don\'t tolerate it!!')
    return
def chatbattter(b):
    count2=0
    for x in b:
        if greet.__contains__(x):
            c=x
            count2+=1
    if count2!=0:
        print(greet[c])
    count=0
    my_list=[]
    for x in b:
        if words.__contains__(x):
            my_list.append(x)
            count+=1
    #if count==1:
        #c=my_list[0]
    if(check(b)):
        global m
        print('You mentioned '+m)
        print(doublr[m]['0'])
        if len(doublr[m])>1:
            temp=input().lower()
            try:
                print(doublr[m][temp])
                if temp!='no' and temp!='n':
                    temp=input().lower()
                    if temp=='yes' or temp=='no' or temp=='0' or temp=='n' or temp=='y':
                        raise Exception("Sorry i don't understand you. Please make another query .\nYou can also call the college reception for you are not satisfied with my answer\n. The number is: 9876543210. ")
                    else:
                        try:
                            print(doublr[m][temp])
                        except:
                            print("Sorry i don't understand you. Please make another query.\nYou can also call the college reception for you are not satisfied with my answer\n. The number is: 9876543210.")
            except:
                print("Sorry i don't understand you. Please make another query.\nYou can also call the college reception for you are not satisfied with my answer\n. The number is: 9876543210.")
    elif count==1:
        c=my_list[0]
        print('You mentioned '+c)
        print(words[c]['0'])
        if len(words[c])>1:
            temp=input().lower()
            try:
                print(words[c][temp])
                if temp!='no' and temp!='n':
                    temp=input().lower()
                    if temp=='yes' or temp=='no' or temp=='0' or temp=='n' or temp=='y':
                        raise Exception("Sorry i don't understand you. Please make another query .\nYou can also call the college reception.\nThe number is: 9876543210.")
                    else:
                        try:
                            print(words[c][temp])
                        except:
                            print("Sorry i don't understand you. Please make another query.\nYou can also call the college reception.\nThe number is: 9876543210.")
            except:
                print("Sorry i don't understand you.Please make another query.\nYou can also call the college reception.\nThe number is: 9876543210.")
    elif count==0 and count2==0:
        print("Sorry i don't understand you.\nYou can also call the college reception.\nThe number is: 9876543210.")
    elif count2!=0:
        print('Don\'t just greet me!! Ask something!!')
    else:
        print('You have mentioned:-')
        i=1
        for x in my_list:
            print(str(i)+':'+x)
            i+=1
        print('But I can help you one by one')
        print('So please select one entry at a time from the above')
        main_like()
    return
print('========= Welcome to JUET FAQ Service =========')
print('=========== I am a Reception Bot!!! ===========')
print('==== Please try to make meaningful Queries ====')
print('============= I am still learning =============')
while True:
    print("How may I help you?")
    main_like()
    print("Do you have any other Query? [Y]es or [N]o ")
    temp=input().lower()
    if temp=='n' or temp=='no':
        break
    if temp!='y' and temp!='yes':
        print("You have entered the wrong choice so i am closing the session.\n"+
              "Feel free to Query any time you want.\nYou can also call the college reception for you are not satisfied with my answers\n. The number is: 9876543210.")
        break
