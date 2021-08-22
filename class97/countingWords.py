introstring=input("enter your introduction")
characterCount=0
wordCount=1
for i in introstring:
        characterCount=characterCount+1
        if (i==""):
                wordCount=wordCount+1
print ("No. of words in the string: ")
print (wordCount)
print ("No. of characters in the string: ")
print (characterCount)