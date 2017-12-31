import os
import math
def testTfIdf():
    dic={}
    numOfDoc=0
    for i in range(0,75):
        for j in range(0,500):
            fpstring='WEBPAGES_RAW/%d/%dnotrashoutcount'%(i,j)
            if os.path.exists(fpstring):
                numOfDoc=numOfDoc+1
                fInput=open(fpstring,'r')
                wordNum=fInput.readline()
                for line in fInput:
                    data=line.split(' ')
                    word=data[0]
                    if dic.has_key(word):
                        dic[word]=dic[word]+1
                    else:
                        dic.setdefault(word,1)
                fInput.close()
        print('%d'%(i))
    for key in dic.keys():
        dic[key]=math.log10(float(numOfDoc)/float(dic[key]))
    dic2=sorted(dic.iteritems(),key=lambda d:d[1], reverse=True)
    fOutput=open('idftest','w')
    num=0
    for item in dic2:
        fOutput.write(item[0]+' %.8f %d\n'%(item[1],num))
        num=num+1
    fOutput.close()
testTfIdf()
