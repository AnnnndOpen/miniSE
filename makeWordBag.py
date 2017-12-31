import os
import math
def makeWordBag():
    dic={}
    dic2={}#the number of particular word appear in documents
    dic3={}#total number of particular word
    numberOfDocuments=0
    for i in range(0,75):
        j=0
        fpstring='WEBPAGES_RAW/%d/%dout'%(i,j)
        while os.path.exists(fpstring):
            numberOfDocuments=numberOfDocuments+1
            fInput=open(fpstring,'r')
            wordNum=fInput.readline()
            wordNum=wordNum[:len(wordNum)-1]
            for line in fInput:
                data=line.split(' ')
                word=data[0]
                num=data[1]
                if dic2.has_key(word):
                    dic2[word]=dic2[word]+1
                    dic3[word]=dic3[word]+int(num)
                else:
                    dic2.setdefault(word,1)
                    dic3.setdefault(word,int(num))
                dic.setdefault(word,[]).append(['%i/%d'%(i,j),num])
            j=j+1
            fInput.close()
            #fOutput.close()
            fpstring='WEBPAGES_RAW/%d/%dout'%(i,j)
        print('in folder %d\n'%(i))
    fOutput=open('index.txt','w')
    fOutput.write('%d %d\n'%(len(dic2),numberOfDocuments))
    wordList=dic2.keys()
    wordList.sort()
    for key in wordList:
        dic4={}
        for data in dic[key]:
            tf=float(data[1])/float(dic3[key])
            lgidf=math.log10(float(numberOfDocuments)/float(dic2[key]))
            tfidf=tf*lgidf
            dic4.setdefault(data[0],tfidf)
        list4=sorted(dic4.items(),key=lambda d:d[1],reverse=True)
        fOutput.write(key+' ')
        for data in list4:
            fOutput.write(data[0]+' %.8f '%(data[1]))
        fOutput.write('\n')
    fOutput.close()
    print('job done\n')
    #print(dic)
    #print(dic2)
makeWordBag()
