# Word frequency analysis

from easygui import *

import re
from banned_words import isBanned,version

linecount = 0

def histogram(s):
    freqdict = dict()
    for c in s:
        if c not in freqdict:
            freqdict[c] = 1
        else:
            freqdict[c] += 1
    return freqdict

filename = fileopenbox(msg="What file should I open? ", title = "Word Frequency Processor", filetypes=["*.txt","*.csv"])
doc=open(filename)
fout = open('freq.csv','w')

temp =[]
h = dict()
punctuation = re.compile(r'[.?!,":@^%$&*;\']')

for line in doc:
    line = line.strip()
    line = line.lower() # make lowercase
    line = punctuation.sub("",line) # remove punctuation
    word_list = re.split('\s+', line) # divide at whitespace
    #print (word_list)
    for word in word_list:
        if isBanned(word) == False:
            temp.append(word) 
    word_list = temp
    h = histogram(word_list)
    #print(h)
    hsorted = sorted(h, key=h.get, reverse=True)
    #print(hsorted)
    for item in hsorted:
        #print(item, ': ', h.get(item,'NotFound'))
        fout.write(item +',' + str(h.get(item,'NotFound')))
        fout.write('\n')
        linecount = linecount + 1
doc.close()
fout.close()
print('done!')
msg = 'There were '+ str(linecount) +  ' unique words processed and saved to freq.csv.'
msgbox(msg)
