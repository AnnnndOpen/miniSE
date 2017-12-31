import os
def calculateWords():
    for i in range(0,75):
        for j in range(0,500):
            fpstring='WEBPAGES_RAW/%d/%dnotrashout'%(i,j)
            if os.path.exists(fpstring):
                fpstringout=fpstring+'count'
                fInput=open(fpstring,'r')
                fOutput=open(fpstringout,'w')
                count4line=0
                wordInThisFile=0
                dic={}
                #wordList=[]
                for line in fInput:
                    count4char=0
                    tmpChar=''
                    startChar=0
                    haveWord=0
                    for z in line:
                        if z.isdigit() or z.isalpha():
                            tmpChar=tmpChar+z.lower()
                            if haveWord==0:
                                haveWord=1
                                startChar=count4char
                        else:
                            if haveWord==1:
                               haveWord=0
                               #tmpChar.lower()
                               dic.setdefault(tmpChar,[]).append([count4line,startChar])
                               tmpChar=''
                               wordInThisFile=wordInThisFile+1
                            startChar=count4char
                        count4char=count4char+1
                    if haveWord==1:
                        dic.setdefault(tmpChar,[]).append([count4line,startChar])
                        wordInThisFile=wordInThisFile+1
                    count4line=count4line+1
                wordList=dic.keys()
                wordList.sort()
                fOutput.write('%d\n'%(wordInThisFile))
                for word in wordList:
                #for item,value in dic2.items():
                    value=dic[word]
                    fOutput.write(word+' %d '%(len(value)))
                    for location in value:
                        fOutput.write('%d %d '%(location[0],location[1]))
                    fOutput.write('\n')
                fInput.close()
                fOutput.close()
                print('%d/%d'%(i,j))
calculateWords()
print('job done')
