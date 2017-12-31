from tkinter import *
import webbrowser
import os
import json
import re
import math
import requests

def calculateScore(inputString):
    #print(inputString)
    global inputdic
    global dic4out
    global dic4angle
    global dic1
    global dic2
    global dic3
    global dic12
    global dic22
    global dicr
    global dicp
    global dicn
    inputdic={}
    inputString=re.sub('[^a-zA-Z0-9]',' ',inputString.lower())
    words=inputString.split(' ')
    for word in words:
        if (word!=''):
            if inputdic.has_key(word):
                inputdic[word]=inputdic[word]+1
            else:
                inputdic.setdefault(word,1)
    if len(inputdic)==0:
        return(0)
    else:
        dic4out={}
        dic4angle={}
        for key in inputdic.keys():
            for i in range(0,int(dic2[key])):
                doc=dic1[key][i*3]
                occur=int(dic1[key][i*3+1])
                tfidf=float(dic1[key][i*3+2])
                if tfidf>0:
                    if dic4out.has_key(doc):
                        dic4out[doc]=dic4out[doc]+tfidf
                    else:
                        if dic3[doc].find('/doku.php/')<0:
                            dic4out.setdefault(doc,tfidf)
                    tmpstring=doc+key
                    dic4angle.setdefault(tmpstring,occur)
                else:
                    break
        vecNum=len(inputdic)
        inputV=0.0
        for key in inputdic.keys():
            inputV=inputV+inputdic[key]*inputdic[key]
        inputV=math.sqrt(inputV)
        listTmp=[]
        dica={}
        dich={}
        for keyf in dic4out.keys():
            fileV=0.0
            timesV=0.0
            for key in inputdic.keys():
                tmpstring=keyf+key
                if dic4angle.has_key(tmpstring):
                    fileV=fileV+dic4angle[tmpstring]*dic4angle[tmpstring]
                    timesV=timesV+dic4angle[tmpstring]*inputdic[key]
            dic4out[keyf]=dic4out[keyf]+2*timesV/math.sqrt(fileV)/inputV#-math.log(float(len(dic3[keyf]))/100)/10
            #if dicr.has_key(keyf):
            #    dic4out[keyf]=dic4out[keyf]+dicr[keyf]
            listTmp.append(keyf)
            listTmp.sort()
            dica.setdefault(keyf,0.15)
            dich.setdefault(keyf,0.15)
        dicTh={}
        dicTa={}
        maxh=0
        maxa=0
        for ii in range(0,3):
            dicTa={}
            dicTh={}
            for key in dic4out.keys():
                dicTa.setdefault(key,float(0))
                dicTh.setdefault(key,float(0))
            print('round %d'%(ii+1))
            for key in dic4out.keys():
                if dicn.has_key(key):
                    for j in range(0,len(dicn[key])):
                        tmpS=dicn[key][j]
                        if dic4out.has_key(tmpS):
                            dicTh[key]=dicTh[key]+0.85*dica[tmpS]/len(dicp[tmpS])
                            dicTa[tmpS]=dicTa[tmpS]+0.85*dich[key]/len(dicn[key])
            dica={}
            dich={}
            for key in dic4out.keys():
                dica.setdefault(key,dicTa[key])
                if dicTa[key]>maxa:
                    maxa=dicTa[key]
                dich.setdefault(key,dicTh[key])
                if dicTh[key]>maxh:
                    maxh=dicTh[key]
        for key in dic4out.keys():
            dic4out[key]=dic4out[key]+float(dica[key])/100+float(dich[key])/100
            '''
            if maxa>0:
                dic4out[key]=dic4out[key]+float(dica[key])/float(maxa)
            if maxh>0:
                dic4out[key]=dic4out[key]+float(dich[key])/float(maxh)
            '''
            #print('%f'%(dic4out[keyf]))
        #dic4out=sorted(dic4out.iteritems(),key=lambda d:d[0])
        
        if len(words)>1:
            for i in range(0,len(words)-1):
                tmpString=words[i]+' '+words[i+1]
                for j in range(0,int(dic22[tmpString])):
                    doc=dic12[tmpString][j*3]
                    occur=int(dic12[tmpString][j*3+1])
                    tfidf=float(dic12[tmpString][j*3+2])
                    if dic4out.has_key(doc):
                        dic4out[doc]=dic4out[doc]+tfidf
        
        dic5out={}
        for key in listTmp:
            dic5out.setdefault(key,dic4out[key])
        dic4out=sorted(dic5out.iteritems(),key=lambda d:d[1],reverse=True)
        #print(dic4out[0])
        return(len(dic4out))

def loadDic():
    fInput=open('index.txt','r')
    tmpstring=fInput.readline()
    global dic1#record the values
    global dic2#record total number
    global dic3#record urls
    global dic12
    global dic22
    global dicr
    global dicp
    global dicn
    dicp={}
    dicn={}
    dic1={}
    dic2={}
    dic3={}
    dic12={}
    dic22={}
    dicr={}
    for line in fInput:
        data=line.split(' ')
        key=data[0]
        totalNum=data[1]
        dic2.setdefault(key,totalNum)
        for i in range(0,int(totalNum)):
            j=i*3
            dic1.setdefault(key,[]).append(data[j+2])
            dic1.setdefault(key,[]).append(data[j+3])
            dic1.setdefault(key,[]).append(data[j+4])
    fInput.close()
    fInput=open('bookkeeping.json','r')
    dic3=json.load(fInput)
    fInput.close()
    print('index file loaded\n')
    fInput=open('index2.txt','r')
    tmpstring=fInput.readline()
    for line in fInput:
        data=line.split(' ')
        key=data[0]+' '+data[1]
        totalNum=data[2]
        dic22.setdefault(key,totalNum)
        for i in range(0,int(totalNum)):
            j=i*3
            dic12.setdefault(key,[]).append(data[j+3])
            dic12.setdefault(key,[]).append(data[j+4])
            dic12.setdefault(key,[]).append(data[j+5])    
    fInput.close()
    print('index2 file loaded\n')
    fInput=open('pageRank','r')
    line=fInput.readline()
    #line=line.split(' ')
    #numMax=line[0]
    for line in fInput:
        line=line.split(' ')
        filen=line[0]
        filehnum=line[1]
        dicr.setdefault(filen,float(filehnum))
    fInput.close()
    print('pageRank loaded')
    fInput=open('connection','r')
    for line in fInput:
        line=line.split(' ')
        num=line[1]
        for j in range (0,int(num)):
            dicn.setdefault(line[0],[]).append(line[j+2])
            dicp.setdefault(line[j+2],[]).append(line[0])
    fInput.close()
    print('connection loaded')
    print('finish loading part')

def sysInit():
    global filePp
    global pageNum
    global maxNum
    global maxPageNum
    global prev_tagnum
    prev_tagnum=0
    pageNum=0
    maxNum=0
    maxPageNum=0
    filePp=10
    loadDic()
    
def btnSearch_click():
    #global bSearch
    #bSearch.pack_forget()
    inputString=entryT.get()
    global pageNum
    global maxNum
    global maxPageNum
    global filePp
    maxNum=calculateScore(inputString)
    maxPageNum=int(maxNum)/int(filePp)
    if int(maxNum)%int(filePp)>0:
        maxPageNum=maxPageNum+1
    if maxPageNum>0:
        pageNum=1
    else:
        pageNum=0
    pageShow()   
    #print(maxNum)
    #print(inputString)
    #print(len(inputString))

def btnPref_click():
    global pageNum
    if pageNum>1:
        pageNum=pageNum-1
        print('go to %d'%(pageNum))
        pageShow()

def btnNext_click():
    global pageNum
    global maxPageNum
    if pageNum<maxPageNum:
        pageNum=pageNum+1
        print('go to %d'%(pageNum))
        pageShow()

def pageShow():
    global pageNum
    global maxNum
    global prev_tagnum
    global dic4out
    global dic3
    global filePp
    text.delete(1.0,END)
    for i in range(0,prev_tagnum):
        text.tag_delete('link%d'%(i))
    startn=(pageNum-1)*filePp
    endn=startn+filePp-1
    if endn>=maxNum:
        endn=maxNum-1
    print('%d %d'%(startn,endn))
    if startn>=0:
        for i in range(startn,endn+1):
            text.insert('%d.0'%(i+1-startn),dic3[dic4out[i][0]]+'\n')
            j=i-startn
            if j==0:
                text.tag_bind('link0','<Button-1>',clickText0)
            elif j==1:
                text.tag_bind('link1','<Button-1>',clickText1)
            elif j==2:
                text.tag_bind('link2','<Button-1>',clickText2)
            elif j==3:
                text.tag_bind('link3','<Button-1>',clickText3)
            elif j==4:
                text.tag_bind('link4','<Button-1>',clickText4)
            elif j==5:
                text.tag_bind('link5','<Button-1>',clickText5)
            elif j==6:
                text.tag_bind('link6','<Button-1>',clickText6)
            elif j==7:
                text.tag_bind('link7','<Button-1>',clickText7)
            elif j==8:
                text.tag_bind('link8','<Button-1>',clickText8)
            elif j==9:
                text.tag_bind('link9','<Button-1>',clickText9)
            text.tag_add('link%d'%(i-startn),'%d.0'%(i+1-startn),'%d.%d'%(i+1-startn,len(dic3[dic4out[i][0]])-1))
        prev_tagnum=endn-startn+1

def clickText0(event):
    global pageNum
    global dic4out
    global dic3
    webbrowser.open(dic3[dic4out[(pageNum-1)*10+0][0]])

def clickText1(event):
    global pageNum
    global dic4out
    global dic3
    webbrowser.open(dic3[dic4out[(pageNum-1)*10+1][0]])

def clickText2(event):
    global pageNum
    global dic4out
    global dic3
    webbrowser.open(dic3[dic4out[(pageNum-1)*10+2][0]])

def clickText3(event):
    global pageNum
    global dic4out
    global dic3
    webbrowser.open(dic3[dic4out[(pageNum-1)*10+3][0]])

def clickText4(event):
    global pageNum
    global dic4out
    global dic3
    webbrowser.open(dic3[dic4out[(pageNum-1)*10+4][0]])

def clickText5(event):
    global pageNum
    global dic4out
    global dic3
    webbrowser.open(dic3[dic4out[(pageNum-1)*10+5][0]])

def clickText6(event):
    global pageNum
    global dic4out
    global dic3
    webbrowser.open(dic3[dic4out[(pageNum-1)*10+6][0]])

def clickText7(event):
    global pageNum
    global dic4out
    global dic3
    webbrowser.open(dic3[dic4out[(pageNum-1)*10+7][0]])

def clickText8(event):
    global pageNum
    global dic4out
    global dic3
    webbrowser.open(dic3[dic4out[(pageNum-1)*10+8][0]])

def clickText9(event):
    global pageNum
    global dic4out
    global dic3
    webbrowser.open(dic3[dic4out[(pageNum-1)*10+9][0]])
    
#def get_clickpoint(event):
#    print(event.x)
#    print(event.y)
        
pageNum=0
maxNum=0
root=Tk()
root.geometry('600x400')
#root.state('zoomed')
root.title('My Search Engine')

frame1=Frame(root)
frame1.pack(side='top')

entryT=Entry(root,text='Enter Query Here')
entryT.pack(side='left',in_=frame1)

bSearch=Button(root,text='Search',command=btnSearch_click)
bSearch.pack(side='right',in_=frame1)

frame2=Frame(root)
frame2.pack(side='top')
frame2l=Frame(root)
frame2r=Frame(root)
frame2l.pack(side='left',in_=frame2)
frame2r.pack(side='right',fill=Y,in_=frame2)

text=Text(root,height=20,width=60,wrap=NONE,cursor='hand2')
text.pack(side='top', in_=frame2l)
#text.insert(1.0,'click here link')
#text.tag_add('link1','1.0','1.4')

global prev_tagnum
prev_tagnum=0

'''
text.tag_bind('link0','<Button-1>',clickText0)
text.tag_bind('link1','<Button-1>',clickText1)
text.tag_bind('link2','<Button-1>',clickText2)
text.tag_bind('link3','<Button-1>',clickText3)
text.tag_bind('link4','<Button-1>',clickText4)
text.tag_bind('link5','<Button-1>',clickText5)
text.tag_bind('link6','<Button-1>',clickText6)
text.tag_bind('link7','<Button-1>',clickText7)
text.tag_bind('link8','<Button-1>',clickText8)
text.tag_bind('link9','<Button-1>',clickText9)
'''

#text.bind('<Button-1>',get_clickpoint)
#text.config(state=DISABLED)
S1=Scrollbar(root)
S1.pack(side='right',fill=Y,in_=frame2r)
S1.config(command=text.yview)
text.config(yscrollcommand=S1.set)
S2=Scrollbar(root,orient=HORIZONTAL)
S2.pack(side='bottom',fill=X,in_=frame2l)
S2.config(command=text.xview)
text.config(xscrollcommand=S2.set)
#text.insert(1.0,'this is the test txt lalala00000000000000000000000')

frame3=Frame(root)
frame3.pack(side='bottom')

bP=Button(root,text='PrevPage',command=btnPref_click)
bP.pack(side='left',in_=frame3)

bN=Button(root,text='NextPage',command=btnNext_click)
bN.pack(side='right',in_=frame3)

sysInit()

root.mainloop()
