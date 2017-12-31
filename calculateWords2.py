import os
import re
def calculateWords2():
    for i in range(0,75):
        print('in file %i'%(i))
        for j in range(0,500):
            fpstring='WEBPAGES_RAW/%d/%dnotrashout'%(i,j)
            if os.path.exists(fpstring):
                fpstringout=fpstring+'count2'
                fInput=open(fpstring,'r')
                fOutput=open(fpstringout,'w')
                list1=[]
                for line in fInput:
                    line=re.sub('[^a-zA-Z0-9]',' ',line.lower())
                    words=line.split(' ')
                    for word in words:
                        if (word!=''):
                            list1.append(word)
                fInput.close()
                dic={}
                for num in range(0,len(list1)-1):
                    tmpString=list1[num]+' '+list1[num+1]
                    if dic.has_key(tmpString):
                        dic[tmpString]=dic[tmpString]+1
                    else:
                        dic.setdefault(tmpString,1)
                dicOut=sorted(dic.iteritems(),key=lambda d:d[0])
                fOutput.write('%d\n'%(len(list1)-1))
                for num in range(0,len(dicOut)):
                    fOutput.write(dicOut[num][0]+' %d\n'%(dicOut[num][1]))
                fOutput.close()
calculateWords2()
