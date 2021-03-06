import os
import math
def makeIndex():
    dic={}
    dic2={}#the number of particular word appear in documents
    dic3={}#total number of particular word
    diccount={}
    numberOfDocuments=0
    for i in range(0,75):
        for j in range(0,500):
            fpstring='WEBPAGES_RAW/%d/%dnotrashoutcount'%(i,j)
            if os.path.exists(fpstring):
                numberOfDocuments=numberOfDocuments+1
                fInput=open(fpstring,'r')
                wordNum=fInput.readline()
                wordNum=wordNum[:len(wordNum)-1]
                for line in fInput:
                    data=line.split(' ')
                    word=data[0]
                    num=data[1]
                    diccount.setdefault('%d/%d'%(i,j)+word,num)
                    if dic2.has_key(word):
                        dic2[word]=dic2[word]+1
                        dic3[word]=dic3[word]+int(num)
                    else:
                        dic2.setdefault(word,1)
                        dic3.setdefault(word,int(num))
                    dic.setdefault(word,[]).append(['%d/%d'%(i,j),num])
                fInput.close()
                #fOutput.close()
        print('in folder %d\n'%(i))
    fOutput=open('index.txt','w')
    fOutput.write('%d %d\n'%(len(dic2),numberOfDocuments))
    wordList=dic2.keys()
    wordList.sort()
    for key in wordList:
        dic4={}
        for data in dic[key]:
            '''
            tf=math.log10(float(data[1])/float(dic3[key]))
            if tf<0:
                tf=0
            else:
                tf=tf+1
            #tf=1+math.log10(float(data[1]))
            '''
            tf=float(data[1])/float(dic3[key])
            lgidf=math.log10(float(numberOfDocuments)/float(dic2[key]))
            tfidf=tf*lgidf
            dic4.setdefault(data[0],tfidf)
        list4=sorted(dic4.items(),key=lambda d:d[1],reverse=True)
        fOutput.write(key+' %d '%(len(list4)))
        for data in list4:
            #tmpstring='WEBPAGES_RAW/'+data[0]+'notrashoutcount'
            #tmpInput=open(tmpstring,'r')
            #tmpdata=tmpInput.readline()
            #while True:
            #    tmpdata=tmpInput.readline()
            #    cut=tmpdata.split(' ')
            #    if cut[0]==key:
            #        break
            tmpstring=data[0]+key
            fOutput.write(data[0]+' '+diccount[tmpstring]+' %.8f '%(data[1]))
            #tmpInput.close()
        fOutput.write('\n')
    fOutput.close()
    print('job done\n')
    #print(dic)
    #print(dic2)
makeIndex()
