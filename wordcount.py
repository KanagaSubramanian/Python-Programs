#wordCount
inputstr='''Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
	tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
	quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
	consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
	cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
	proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''
inputstr=inputstr.upper()
words=inputstr.split()
#print("WORDS: ",words)
print("LENGTH:",len(words))
counts=dict()
for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
#print("COUNTS:",counts)
for word in counts:
    if(counts[word]==max(counts.values())):
        print("MAX:   ",word,"-",max(counts.values()))
        break
    
