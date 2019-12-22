#Count number of SubStrings in a file

filename=input("Enter name of file? ")
a=open(filename,'r')
word=input("Enter word to search: ")
length=len(word)
count=0
for line in a.readlines():
    line=line.strip()
    line=line.split(' ')
    for s in line:
        if len(s)<length:
            continue 
        if s==word:
            count=count+1
        

print("Number of word: \""+word+"\"in "+filename+" is: "+ str(count))
input("Enter to Quit.")