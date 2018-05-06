import re
import emoji

with open('emoji-list.txt','r') as f:
    
    for line in f:
    
        myemoji = (emoji.emojize(line))
    
        if ":" not in myemoji:
            print(line, myemoji)
        else:
            print(line, "no emoji\n")
        
       
