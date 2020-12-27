inputstr="SecondMostFrequentCharacterInTheString"
countar=[]
maxnum=0
for i in inputstr:
    if(i!='#'):
        countar.append(inputstr.count(i))
        print(i,inputstr.count(i),end=", ")
        inputstr=inputstr.replace(i,'#')
        if(maxnum==max(countar)):
            continue
        elif(maxnum<max(countar)):
            maxnum=max(countar)
            char=i
    else:
        continue
print()
print(char,maxnum)
