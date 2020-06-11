fileName=input("Enter the FileName:")
outPut={}
with open(fileName,'r') as file:
    for l in file:
        wordlist=l.split()
        for word in wordlist:
            if word.lower() in outPut:
                outPut[word.lower()]+=1
            else:
                outPut[word.lower()]=1
print(outPut)
wordfile=open("wordcount.txt","w")
for key,val in outPut.items():
    wordfile.write("{} {}\n".format(key,val))
wordfile.close()

