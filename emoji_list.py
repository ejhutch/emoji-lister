import re
import emoji

with open('emoji-list.txt','r') as f:
    
    for e in map(emoji.emojize, f):
        # If emojize does not find an emoji
        # it will just return the :emoji: text.
        if ":" not in e:
            print(f.readline() + e)
        else:
            print("No emoji for " + e)
