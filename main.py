import language_tool_python
tool = language_tool_python.LanguageTool('en-US')

def spellcheck(text,lentext):
    mismatches = tool.check(text)
    mismatchlen = len(mismatches)
    return (mismatchlen/lentext)*100

def checkbadwords(text,lentext):
    my_file = open("badwords.txt", "r")

    data = my_file.read()
    
    bad_word = data.split("\n")
    my_file.close()

    badcount = 0
    for b in bad_word:
        if b in text:
            badcount += 1
    
    return ((badcount*5)/lentext)*100 

def checkSpam(text,lentext):
    my_file = open("spamwords.txt", "r")
    data = my_file.read()
    
    spam_word = data.split("\n")
    my_file.close()

    spamcount = 0
    for spam in spam_word:
        if spam in text:
            spamcount += 1
            # print(spam)
            
    return ((spamcount*3)/lentext)*100   

    

def rating(text):
    
    lentext = 1
    for i in range(len(text)):
        if(text[i] == " "):
            lentext += 1

    spelmistake = spellcheck(text,lentext)
    badwords = checkbadwords(text,lentext)
    spamwords = checkSpam(text,lentext)

    rating = 100 - ((spelmistake+badwords+spamwords)//3) 
    if rating < 0: 
        rating = 0
    return rating
