import re
import emoji

with open('emoji-list.txt','r') as f:
    
    for e in map(emoji.emojize, f):
        
        if ":" not in e:
            print(e)
        else:
            print(e, "no emoji\n")
        
