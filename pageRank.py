import os
import json
def pageRank():
    fInput=open('bookkeeping.json','r')
    dic1=json.load(fInput)
    fInput.close()
    dica={}
    dich={}
    dic2={}
    dicr={}
    for value in dic1.values():
        dica.setdefault(value,float(1))
        dich.setdefault(value,float(1))
        dicr.setdefault(value,float(1))
    for key in dic1.keys():
        dic2.setdefault(dic1[key],key)
    dicp={}
    dicn={}
    dicnOfp={}
    #print(dic1['0/7'])
    
    for i in range(0,75):
        for j in range(0,500):
            fpstring='WEBPAGES_RAW/%d/%dnotrashout'%(i,j)
            if os.path.exists(fpstring):
                numOfLink=0
                fInput=open('WEBPAGES_RAW/%d/%d'%(i,j))
                allText=fInput.read().lower()
                fInput.close()
                startp=allText.find('<a href="')
                if startp>=0:
                    allText=allText[startp+9:]
                    startp=0
                    endp=allText.find('"')
                baseU=dic1['%d/%d'%(i,j)]
                dicTmp={}
                while startp>=0:
                    numOfLink=numOfLink+1
                    Url=''
                    subU=allText[:endp]
                    if subU.find('http://')==0:
                        Url=subU[7:]
                    elif subU.find('https://')==0:
                        Url=subU[8:]
                    elif subU.find('www.')==0:
                        Url=subU
                    else:
                        if (subU.find('../')==0):
                            Url=baseU
                            while subU.find('../')==0:
                                subU=subU[3:]
                                Url=Url[0:(Url.rfind('/'))]
                            Url=Url+'/'+subU
                        elif (subU.find('./')==0):
                            Url=baseU
                            while subU.find('./')==0:
                                subU=subU[2:]
                                Url=subU[:subU.rfind('/')+1]
                            Url=Url+subU
                        elif (subU.find('/')==0):
                            if baseU.find('https://')==0:
                                tmpurl=base[8:]
                                tmpint=tmpurl.find('/')
                                if tmpint<0:
                                    Url=baseU+subU
                                else:
                                    Url='https://'+tmpurl[:tmpint]+subU
                            elif baseU.find('http://')==0:
                                tmpurl = base[7:]
                                tmpint = tmpurl.find('/')
                                if tmpint < 0:
                                    Url = baseU + subU
                                else:
                                    Url = 'http://' + tmpurl[:tmpint] + subU
                            else:
                                Url=baseU[:baseU.find('/')]+subU
                        '''
                        else:
                            #print(baseU+' '+subU)
                            Url=''
                            for tmpi in range(0,len(baseU)):
                                Url=Url+baseU[tmpi]
                            Url=Url+'/'
                            for tmpi in range(0,len(subU)):
                                Url=Url+subU[tmpi]
                        '''
                        
                    if dicTmp.has_key(Url)==False:
                        dicTmp.setdefault(Url,1)
                        if dica.has_key(Url):
                            dicn.setdefault(baseU,[]).append(Url)
                            dicp.setdefault(Url,[]).append(baseU)
                    allText=allText[endp:]
                    startp = allText.find('<a href="')
                    if startp>=0:
                        allText=allText[startp+9:]
                        startp=0
                        endp=allText.find('"')
                dicnOfp.setdefault(baseU,numOfLink)
        print('in folder %d'%(i))
    print('conection created')
    fOutput=open('connection','w')
    for key in dic1.keys():
        if dicn.has_key(dic1[key]):
            fOutput.write(key+' ')
            fOutput.write('%d '%(len(dicn[dic1[key]])))
            for j in range(0,len(dicn[dic1[key]])):
                fOutput.write(dic2[dicn[dic1[key]][j]]+' ')
            fOutput.write('\n')
    fOutput.close()
    maxa=0
    maxh=0
    maxr=0
    for i in range(0,5):
        dicTa={}
        dicTh={}
        dicTr={}
        for key in dic1.values():
            dicTa.setdefault(key,float(0))
            dicTh.setdefault(key,float(0))
            dicTr.setdefault(key,0.15)
        print('round %d'%(i+1))
        for key in dic1.values():
            if dicn.has_key(key):
                for j in range(0,len(dicn[key])):
                    tmpS=dicn[key][j]
                    dicTr[tmpS]=dicTr[tmpS]+0.85*(float(dicr[key])/float(dicnOfp[key]))
                    dicTh[key]=dicTh[key]+dica[tmpS]
                    dicTa[tmpS]=dicTa[tmpS]+dich[key]
                    '''
                    if dicTa[tmpS]>max:
                        max=dicTa[tmpS]
                        maxK=tmpS
                    '''
                    
        dich={}
        dica={}
        dicr={}
        for key in dicTr.keys():
            dicr.setdefault(key,dicTr[key])
            if dicTr[key]>maxr:
                maxr=dicTr[key]
        
        for key in dicTh.keys():
            dich.setdefault(key,dicTh[key])
            if dicTh[key]>maxh:
                maxh=dicTh[key]
        for key in dicTa.keys():
            dica.setdefault(key,dicTa[key])
            if dicTa[key]>maxa:
                maxa=dicTa[key]
        
    #print('%d'%(max))
    #print(maxK)
    #for key in dica.keys():
    #    print(dic2[key]+' %d'%(dica[key]))
    #print(' %d'%(dica[maxK]))
    #print(' %d'%(dich[maxK]))
    fOutput2=open('pageRank2','w')
    fOutput=open('pageRank','w')
    fOutput2.write('%d %d\n'%(maxh,maxa))
    fOutput.write('%.6f \n'%(maxr))
    for key in dic1.keys():
        
        a1=False
        a2=False
        if dich.has_key(dic1[key]):
            if dich[dic1[key]]>0:
                a1=True
        if dica.has_key(dic1[key]):
            if dica[dic1[key]]>0:
                a2=True
        if a1==True or a2==True:
            fOutput2.write(key+' ')
            if dich.has_key(dic1[key]):
                fOutput2.write('%d '%(dich[dic1[key]]))
            else:
                fOutput2.write('0 ')
            if dica.has_key(dic1[key]):
                fOutput2.write('%d '%(dica[dic1[key]]))
            else:
                fOutput2.write('0 ')
            fOutput2.write('\n')
        
        if dicr.has_key(dic1[key]):
            if dicr[dic1[key]]>0:
                fOutput.write(key+' ')
                fOutput.write('%.6f \n'%(dicr[dic1[key]]))
    fOutput.close()
    fOutput2.close()
    '''
    key=dic1['0/1']
    print(key)
    #print('%d'%(len(dicn[key])))
    print (dicn.has_key(key))
    '''
pageRank()
    
