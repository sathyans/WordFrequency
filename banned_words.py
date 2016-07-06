#!/usr/bin/python
# Filename: banned_words.py
import re

bannedWords = []

banned=open('banned.txt')

for line in banned:
    line = line.strip()
    bannedWords.append(line)
    #bannedWords = re.split('\n+', line) # divide at whitespace

#print(bannedWords)
#bannedWords = ['the', 'a', 'as', 'am', 'is' 'are', 'was', 'were', 'be', 'been', 'do', 'did', 'does',  'can', 'could', 'have', 'has' , 'do', 'of']

def isBanned(word):
	for currentWord in bannedWords:
		if currentWord == word:
			return True
	return False

version = '0.1'

# End of banned_words.py
