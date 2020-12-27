inputstr="SecondMostFrequentCharacterInTheString"
safe=inputstr
countar=[]
count=0
for i in inputstr:
    if(i!='#'):
        countar.append(inputstr.count(i))
        print(i,inputstr.count(i),end=", ")
        inputstr=inputstr.replace(i,'#')
    else:
        continue
firstmax=max(countar)
countar.remove(max(countar))
maxnum=max(countar)
print()
if(firstmax==maxnum):
    for i in safe:
        if(maxnum==safe.count(i)):
            count+=1
            if(count==2):
                print(i,maxnum)
                break
    
else:
    for i in safe:
        if(maxnum==safe.count(i)):
            print(i,maxnum)
            break
    
    
