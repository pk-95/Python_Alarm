#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pygame import mixer as mx
import time
from time import localtime


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[40]:


def alarm():
    mx.init()
    mx.music.load('Tame Impala.mp3')
    f=open('alarms.txt','r+')
    n=eval(input("Enter the number of alarms you want to create:\n"))
    print("\nEnter time in 24 hour format")
    for i in  range(n):
        print("For alarm ",i+1)
        h=input("Enter hours: ")
        m=input("Enter mins: ")
        s=input("Enter seconds: ")
        p=str([h,m,s])
        f.write(p+"\n")
    f.close()
    f=open('alarms.txt','r')
    x=f.readlines()
    e=[]
    for g in x:
        k=[]
        d=eval(g)
        for i in d:
            i=int(i)
            k.append(i)
        e.append(k)
    while True:
        time_now = [localtime().tm_hour,localtime().tm_min,localtime().tm_sec]
        if time_now in e:
             mx.music.play()
             print("ALARM IS RINGING"*8)
             time.sleep(20)
             mx.music.stop()
             break
        
    f.close()
alarm()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


""""    k=[]
    for i in x:
        h=[]
        for j in i:
            print(type(j))
           # h.append(int(j))
        k.append(h)
    print(k)
    time_now = [localtime().tm_hour,localtime().tm_min,localtime().tm_sec]
    if time_now in k:
             mixer.music.play()
             print("WAKE UP!!!!")
             time.sleep(50)
             mixer.music.stop()"""""


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # 
