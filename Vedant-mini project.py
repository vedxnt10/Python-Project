#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"]=(18,10)


# # Reading CSV file

# In[3]:


ab = pd.read_csv(r'D:\health.csv')
ab


# # Reading columns

# In[ ]:


gen = ab['gender']
st = ab['stroke']
w = ab['work_type']
smoke = ab['smoking_status']
mry = ab['ever_married']
res = ab['Residence_type']
heart = ab['heart_disease']
hyper = ab['hypertension']


# # Defining Functions for plotting graphs

# In[ ]:





# In[90]:


def disease():
    l=0
    s=0
    t=0
    h=0
    g=0
    f=0
    x=0
    y=0
    for i in range(4981):
        if(heart[i]==1 and hyper[i]==1 and gen[i]=='Male'):
            l=l+1
        elif(heart[i]==1 and hyper[i]==1 and gen[i]=='Female'):
            s=s+1
        elif(heart[i]==1 and hyper[i]==0 and gen[i]=='Male'):
            t=t+1
        elif(heart[i]==1 and hyper[i]==0 and gen[i]=='Female'):
            h=h+1
        elif(heart[i]==0 and hyper[i]==1 and gen[i]=='Male'):
            g=g+1
        elif(heart[i]==0 and hyper[i]==1 and gen[i]=='Female'):
            f=f+1
        elif(heart[i]==0 and hyper[i]==0 and gen[i]=='Male'):
            x=x+1
        elif(heart[i]==0 and hyper[i]==0 and gen[i]=='Female'):
            y=y+1
    name = ['Male suffer from hypertension and heart disease','Male suffer from heart disease',
            'Male suffer from hypertension','Male with no hypertension and no heart disease',
            'Female suffer from hypertension and heart disease','Female suffer from heart disease',
           'Female suffer from hypertension','Female with no hypertension and no heart disease']
    num = [l,t,g,x,s,h,f,y]
    fig=plt.figure(1)
    ax=fig.add_subplot(111)
    ax.set_xticklabels(name,rotation=45)
    plt.plot(name,num,color = 'green',linewidth='4', marker='o',ms='8')
    plt.show()


# In[ ]:





# In[91]:


def place():
    m=0
    n=0
    o=0
    p=0
    for i in range(4981):
        if(res[i]=='Urban' and st[i]==1):
            m=m+1
        elif(res[i]=='Rural' and st[i]==1):
            n=n+1

    for j in range(4981):
        if(res[j]=='Urban' and st[j]==0):
            o=o+1
        elif(res[j]=='Rural' and st[j]==0):
            p=p+1
            
    x = ['Urban people with 1 stroke','Urban people with 0 stroke','Rural people with 1 stroke','Rural people with 0 stroke']
    y = [m,o,n,p]
    print(m,n)
    plt.plot(x,y,color='r',linewidth='4',marker='o',ms='8')


# In[4]:


def vedzz():
    print("Analysis of persons suffered 1 stroked with work-type")
    l=0
    s=0
    t=0
    h=0
    g=0
    f=0
    x=0
    y=0
    for i in range(0,4981):
        if(w[i]=='Private' and gen[i] == 'Male' and st[i]==1):
            l=l+1
        elif(w[i]=='Self-employed' and gen[i] == 'Male' and st[i]==1):
            s=s+1
        elif(w[i]=='Govt_job' and gen[i] == 'Male' and st[i]==1):
            t=t+1
        elif(w[i]=='Private' and gen[i] == 'Female' and st[i]==1):
            h=h+1
        elif(w[i]=='Self-employed' and gen[i] == 'Female' and st[i]==1):
            g=g+1
        elif(w[i]=='Govt_job' and gen[i] == 'Female' and st[i]==1):
            f=f+1
        elif(gen[i]=='Male'and st[i]==1):
            x=x+1
        elif(gen[i]=='Female'and st[i]==1):
            y=y+1
    ved = ['Males with Private work type', 'Males with Self-employed work type','Males with Govt-job work type',
      'Females with Private work type','Females with Self-employed work type','Females with Govt-job work type',
      'Males with Other work type','Females with Other work type']
    yas = [l,s,t,h,g,f,x,y]
    fig=plt.figure(1)
    ax=fig.add_subplot(111)
    ax.set_xticklabels(ved,rotation=45)
    plt.bar(ved,yas)
    print(l,s,t,h,g,f,x,y)
    plt.title("Data Analysis of victims of brain strome")
    plt.xlabel("No of cases")
    plt.ylabel("Type of Peoples")
    plt.show()


# In[28]:


def mohod():
    print("Analysis of persons suffered 0 stroked with work-type")
    l=0
    s=0
    t=0
    h=0
    g=0
    f=0
    x=0
    y=0
    for i in range(0,4981):
        if(w[i]=='Private' and gen[i] == 'Male' and st[i]==0):
            l=l+1
        elif(w[i]=='Self-employed' and gen[i] == 'Male' and st[i]==0):
            s=s+1
        elif(w[i]=='Govt_job' and gen[i] == 'Male' and st[i]==0):
            t=t+1
        elif(w[i]=='Private' and gen[i] == 'Female' and st[i]==0):
            h=h+1
        elif(w[i]=='Self-employed' and gen[i] == 'Female' and st[i]==0):
            g=g+1
        elif(w[i]=='Govt_job' and gen[i] == 'Female' and st[i]==0):
            f=f+1
        elif(gen[i]=='Male'and st[i]==1):
            x=x+1
        else:
            y=y+1
    ved = ['Males with Private work type', 'Males with Self-employed work type','Males with Govt-job work type',
      'Females with Private work type','Females with Self-employed work type','Females with Govt-job work type',
      'Males with Other work type','Females with Other work type']
    yas = [l,s,t,h,g,f,x,y]
    fig=plt.figure(1)
    ax=fig.add_subplot(111)
    ax.set_xticklabels(ved,rotation=45)
    print(l,s,t,h,g,f,x,y)
    plt.pie(yas,labels=ved)
    plt.title("Data Analysis of persons who doesnt affected by of brain strome")
    plt.show()


# In[38]:


smoke = ab['smoking_status']
def utkarsh():
    print("Analysis of persons suffered 1 stroked v/s smoking")
    l=0
    s=0
    t=0
    h=0
    g=0
    f=0
    x=0
    y=0
    for i in range(0,4981):
        if(smoke[i]=='formerly smoked' and gen[i] == 'Male' and st[i]==1):
            l=l+1
        elif(smoke[i]=='never smoked' and gen[i] == 'Male' and st[i]==1):
            s=s+1
        elif(smoke[i]=='smokes' and gen[i] == 'Male' and st[i]==1):
            t=t+1
        elif(smoke[i]=='formerly smoked' and gen[i] == 'Female' and st[i]==1):
            h=h+1
        elif(smoke[i]=='never smoked' and gen[i] == 'Female' and st[i]==1):
            g=g+1
        elif(smoke[i]=='smokes' and gen[i] == 'Female' and st[i]==1):
            f=f+1
        elif(smoke[i]=='Unknown' and gen[i]=='Male'and st[i]==1):
            x=x+1
        elif(smoke[i]=='Unknown' and gen[i]=='Female'and st[i]==1):
            y=y+1
    ved = ['Males smokes formly', 'Males never smoked','Males addictive smoking',
      'Females smokes formly','Females never smoked','Females addictive smoking',
      'Males with unknown data','Females with unknown data']
    yas = [l,s,t,h,g,f,x,y]
    fig=plt.figure(1)
    ax=fig.add_subplot(111)
    ax.set_xticklabels(ved,rotation=45)
    print(l,s,t,h,g,f,x,y)
    plt.bar(ved,yas, color='pink')
    plt.title("Data Analysis of persons who affected by of brain strome")
    plt.xlabel("No of cases")
    plt.ylabel("Type of Peoples")
    plt.show()


# In[40]:


def nikhil():
    print("Analysis of persons suffered 0 stroked v/s smoking")
    l=0
    s=0
    t=0
    h=0
    g=0
    f=0
    x=0
    y=0
    for i in range(0,4981):
        if(smoke[i]=='formerly smoked' and gen[i] == 'Male' and st[i]==0):
            l=l+1
        elif(smoke[i]=='never smoked' and gen[i] == 'Male' and st[i]==0):
            s=s+1
        elif(smoke[i]=='smokes' and gen[i] == 'Male' and st[i]==0):
            t=t+1
        elif(smoke[i]=='formerly smoked' and gen[i] == 'Female' and st[i]==0):
            h=h+1
        elif(smoke[i]=='never smoked' and gen[i] == 'Female' and st[i]==0):
            g=g+1
        elif(smoke[i]=='smokes' and gen[i] == 'Female' and st[i]==0):
            f=f+1
        elif(smoke[i]=='Unknown' and gen[i]=='Male'and st[i]==0):
            x=x+1
        elif(smoke[i]=='Unknown' and gen[i]=='Female'and st[i]==0):
            y=y+1
    ved = ['Males smokes formly', 'Males never smoked','Males addictive smoking',
      'Females smokes formly','Females never smoked','Females addictive smoking',
      'Males with unknown data','Females with unknown data']
    yas = [l,s,t,h,g,f,x,y]
    fig=plt.figure(1)
    ax=fig.add_subplot(111)
    ax.set_xticklabels(ved,rotation=45)
    print(l,s,t,h,g,f,x,y)
    plt.bar(ved,yas, color='black')
    plt.title("Data Analysis of persons who doesnt affected by of brain strome")
    plt.xlabel("No of cases")
    plt.ylabel("Type of Peoples")
    plt.show()


# In[86]:


def vish():
    l=0
    s=0
    t=0
    h=0
    g=0
    f=0
    x=0
    y=0
    vs = ['Married males who got brain stroke','Married males who doesnt got brain stroke',
          'Unmarried males who got brain stroke','Unmarried males who doesnt got brain stroke',
          'Married females who got brain stroke','Married females who doesnt got brain stroke',
          'Unmarried females who got brain stroke','Unmarried females who doesnt got brain stroke']
    for i in range(0,4981):
        if(mry[i]=='Yes' and gen[i]=='Male' and st[i]==1):
            l=l+1
        elif(mry[i]=='Yes' and gen[i]=='Male'and st[i]==0):
            s=s+1
        elif(mry[i]=='No' and gen[i]=='Male'and st[i]==1):
            t=t+1
        elif(mry[i]=='No' and gen[i]=='Male'and st[i]==0):
            h=h+1
        elif(mry[i]=='Yes' and gen[i]=='Female'and st[i]==1):
            g=g+1
        elif(mry[i]=='Yes' and gen[i]=='Female'and st[i]==0):
            f=f+1
        elif(mry[i]=='No' and gen[i]=='Female'and st[i]==1):
            x=x+1
        elif(mry[i]=='No' and gen[i]=='Female'and st[i]==1):
            y=y+1
    yas = [l,s,t,h,g,f,x,y]
    fig=plt.figure(1)
    ax=fig.add_subplot(111)
    ax.set_xticklabels(vs,rotation=45)
    print(l,s,t,h,g,f,x,y)
    plt.plot(vs,yas,color='Orange',linewidth='4',marker='o',ms='8')
    plt.title("Data Analysis of brain strome")
    plt.xlabel("No of cases")
    plt.ylabel("Type of Peoples")
    plt.show()
    


# # Plotting Graphs

# In[9]:


vedzz()


# In[29]:


mohod()


# In[39]:


utkarsh()


# In[41]:


nikhil()


# In[87]:


vish()


# In[88]:


disease()


# In[89]:


place()


# In[ ]:




