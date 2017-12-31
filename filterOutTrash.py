import os
def filterOutTrash():
    for i in range(0,75):
        for j in range(0,500):
            fpstring='WEBPAGES_RAW/%d/%d'%(i,j)
            if os.path.exists(fpstring):
                fpstringout=fpstring+'notrashout'
                fInput=open(fpstring,'r')
                allText=fInput.read().lower()
                fInput.close()
                if (allText.find('<!doctype html')>=0) or (allText.find('</html>')>=0) or (allText.find('<html')>=0):
                    a1=''
                    if allText.find('</head>')>=0:
                        a1=allText[allText.find('<head'):allText.find('</head>')]
                    elif allText.find('</header>')>=0:
                        a1=allText[allText.find('<header'):allText.find('</header>')]
                    a2=allText[allText.find('<body'):allText.find('</body>')]
                    allText=a1+a2
                    while (allText.find('<script')>=0) and (allText.find('</script>')>=0):
                        q1=allText.find('<script')
                        q2=allText.find('</script>')
                        amount=1
                        half=allText[q1+7:]
                        allText=allText[:q1]
                        while amount>0:
                            q1=half.find('<script')
                            q2=half.find('</script>')
                            if (q1<0) and (q2>=0):
                                amount=amount-1
                                half=half[q2+9:]
                            elif (q1>=0) and (q2>=0):
                                if q1<q2:
                                    amount=amount+1
                                    half=half[q1+7:]
                                else:
                                    amount=amount-1
                                    half=half[q2+9:]
                            else:
                                break
                        allText=allText+half

                    while (allText.find('<style')>=0) and (allText.find('</style>')>=0):
                        q1=allText.find('<style')
                        q2=allText.find('</style>')
                        amount=1
                        half=allText[q1+6:]
                        allText=allText[:q1]
                        while amount>0:
                            q1=half.find('<style')
                            q2=half.find('</style>')
                            if (q1<0) and (q2>=0):
                                amount=amount-1
                                half=half[q2+8:]
                            elif (q1>=0) and (q2>=0):
                                if q1<q2:
                                    amount=amount+1
                                    half=half[q1+6:]
                                else:
                                    amount=amount-1
                                    half=half[q2+8:]
                            else:
                                break
                        allText=allText+half

                    while (allText.find('<select')>=0) and (allText.find('</select>')>=0):
                        q1=allText.find('<select')
                        q2=allText.find('</select>')
                        amount=1
                        half=allText[q1+7:]
                        allText=allText[:q1]
                        while amount>0:
                            q1=half.find('<select')
                            q2=half.find('</select>')
                            if (q1<0) and (q2>=0):
                                amount=amount-1
                                half=half[q2+9:]
                            elif (q1>=0) and (q2>=0):
                                if q1<q2:
                                    amount=amount+1
                                    half=half[q1+7:]
                                else:
                                    amount=amount-1
                                    half=half[q2+9:]
                            else:
                                break
                        allText=allText+half

                    while (allText.find('<form')>=0) and (allText.find('</form>')>=0):
                        q1=allText.find('<form')
                        q2=allText.find('</form>')
                        amount=1
                        half=allText[q1+5:]
                        allText=allText[:q1]
                        while amount>0:
                            q1=half.find('<form')
                            q2=half.find('</form>')
                            if (q1<0) and (q2>=0):
                                amount=amount-1
                                half=half[q2+7:]
                            elif (q1>=0) and (q2>=0):
                                if q1<q2:
                                    amount=amount+1
                                    half=half[q1+5:]
                                else:
                                    amount=amount-1
                                    half=half[q2+7:]
                            else:
                                break
                        allText=allText+half
                    while (allText.find('<dl')>=0) and (allText.find('</dl>')>=0):
                        q1=allText.find('<dl')
                        q2=allText.find('</dl>')
                        amount=1
                        half=allText[q1+3:]
                        allText=allText[:q1]
                        while amount>0:
                            q1=half.find('<dl')
                            q2=half.find('</dl>')
                            if (q1<0) and (q2>=0):
                                amount=amount-1
                                half=half[q2+5:]
                            elif (q1>=0) and (q2>=0):
                                if q1<q2:
                                    amount=amount+1
                                    half=half[q1+3:]
                                else:
                                    amount=amount-1
                                    half=half[q2+5:]
                            else:
                                break
                        allText=allText+half
                    while (allText.find('<a')>=0) and (allText.find('</a>')>=0):
                        q1=allText.find('<a')
                        q2=allText.find('</a>')
                        amount=1
                        half=allText[q1+2:]
                        allText=allText[:q1]
                        while amount>0:
                            q1=half.find('<a')
                            q2=half.find('</a>')
                            if (q1<0) and (q2>=0):
                                amount=amount-1
                                half=half[q2+4:]
                            elif (q1>=0) and (q2>=0):
                                if q1<q2:
                                    amount=amount+1
                                    half=half[q1+2:]
                                else:
                                    amount=amount-1
                                    half=half[q2+4:]
                            else:
                                break
                        allText=allText+half
                    while (allText.find('<ol')>=0) and (allText.find('</ol>')>=0):
                        q1=allText.find('<ol')
                        q2=allText.find('</ol>')
                        amount=1
                        half=allText[q1+3:]
                        allText=allText[:q1]
                        while amount>0:
                            q1=half.find('<ol')
                            q2=half.find('</ol>')
                            if (q1<0) and (q2>=0):
                                amount=amount-1
                                half=half[q2+5:]
                            elif (q1>=0) and (q2>=0):
                                if q1<q2:
                                    amount=amount+1
                                    half=half[q1+3:]
                                else:
                                    amount=amount-1
                                    half=half[q2+5:]
                            else:
                                break
                        allText=allText+half
                    while (allText.find('<ul')>=0) and (allText.find('</ul>')>=0):        
                        q1=allText.find('<ul')
                        q2=allText.find('</ul>')
                        amount=1
                        half=allText[q1+3:]
                        allText=allText[:q1]
                        while amount>0:
                            q1=half.find('<ul')
                            q2=half.find('</ul>')
                            if (q1<0) and (q2>=0):
                                amount=amount-1
                                half=half[q2+5:]
                            elif (q1>=0) and (q2>=0):
                                if q1<q2:
                                    amount=amount+1
                                    half=half[q1+3:]
                                else:
                                    amount=amount-1
                                    half=half[q2+5:]
                            else:
                                break
                        allText=allText+half
                        
                    noBk=''
                    ii=0
                    pos=0
                    found=False
                    while ii<len(allText):
                        if found==False:
                            if allText[ii]=='<':
                                found=True
                                pos=ii
                            else:
                                noBk=noBk+allText[ii]
                        else:
                            if allText[ii]=='<':
                                noBk=noBk+allText[pos:ii]
                                pos=ii
                            elif allText[ii]=='>':
                                found=False
                        ii=ii+1
                    if found>True:
                        noBk=noBk+allText[pos:]
                    fOutput=open(fpstringout,'w')
                    ii=0
                    noBk2=''
                    j1=noBk.find('&')
                    j2=noBk.find(';')
                    while (j1>=0)and(j2>=0):
                        if j2<j1:
                            noBk2=noBk2+noBk[:j2+1]
                            noBk=noBk[j2+1:]
                        else:
                            if noBk[j1+1]=='#':
                                tmp=noBk[j1+2:j2]
                                if tmp.isdigit()==True:
                                    noBk2=noBk2+noBk[:j1]+' '
                                    noBk=noBk[j2+1:]
                                else:
                                    noBk2=noBk2+noBk[:j2+1]
                                    noBk=noBk[j2+1:]
                            else:
                                tmp=noBk[j1+1:j2]
                                if tmp.isalpha()==True:
                                    noBk2=noBk2+noBk[:j1]+' '
                                    noBk=noBk[j2+1:]
                                else:
                                    noBk2=noBk2+noBk[:j2+1]
                                    noBk=noBk[j2+1:]
                        j1=noBk.find('&')
                        j2=noBk.find(';')
                    if noBk!='':
                        noBk2=noBk2+noBk
                    noBk=noBk2
                    
                    ii=0
                    dellete=False
                    noBk2=''
                    while ii<len(noBk):
                        while (ii<len(noBk)):
                            if ((noBk[ii]=='')or(noBk[ii]==' ')or(noBk[ii]=='\n')or(noBk[ii]=='\r')):
                                dellete=True
                                ii=ii+1
                            else:
                                break
                        if (ii<len(noBk)):
                            if dellete==True:
                                dellete=False
                                noBk2=noBk2+' '
                            noBk2=noBk2+noBk[ii]
                            ii=ii+1
                    fOutput.write(noBk2)
                    fOutput.close()
                    print('%d/%d'%(i,j))
filterOutTrash()

