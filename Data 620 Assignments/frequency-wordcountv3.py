"""
Data 620 Assignment 12.1 text analysis with Python
Written by James Nicholson
Last Update April 24, 2019
This program analysis text in a file and finds the most common words and the frequency of the
words in the file. The user is able to select the number of common words to display. 
"""

import collections
import sys

import nltk
from nltk.corpus import stopwords

# Read input file
#User will enter the file name here

file = open('teddysou1908.txt')

a= file.read()

# Stopwords. These are the 250 most common words according to http://www.anglik.net/english250.htm
stopwords = set(line.strip() for line in open('trumpsou2017.txt'))

stopwords = set(stopwords.words('english')) 
"""
stopwords.union(set(['mr','mrs','one','two','said','the','of','to','and','a','in','is','it',
'you','that','he','was','for','on','are','with','as','i','his','they','be','at','one','have','this','from','or',
'had','by','hot','but','some','what','there','we','can','out','other','were','all','your','when','up','use','word',
'how','said','an','each','she','which','do','their','time','if','will','way','about','many','then','them','would',
'write','like','so','these','her','long','make','thing','see','him','two','has','look','more','day','could','go',
'come','did','my','sound','no','most','number','who','over','know','water','than','call','first','people','may',
'down','side','been','now','find','any','new','work','part','take','get','place','made','live','where','after',
'back','little','only','round','man','year','came','show','every','good','me','give','our','under','name','very',
'through','just','form','much','great','think','say','help','low','line','before','turn','cause','same','mean',
'differ','move','right','boy','old','too','does','tell','sentence','set','three','want','air','well','also','play',
'small','end','put','home','read','hand','port','large','spell','add','even','land','here','must','big','high','such',
'follow','act','why','ask','men','change','went','light','kind','off','need','house','picture','try','us','again','animal',
'point','mother','world','near','build','self','earth','father','head','stand','own','page','should','country','found','answer',
'school','grow','study','still','learn','plant','cover','food','sun','four','thought','let','keep','eye','never','last','door',
'between','city','tree','cross','since','hard','start','might','story','saw','far','sea','draw','left','late','run',"don't",
'while','press','close','night','real','life','few','stop',':','•']))
"""

# Instantiate a dictionary, and for every word in the file, 
# Add to the dictionary if it doesn't exist. If it does, increase the count.
wordcount = {}
# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
# Print most common word
# Wrap this within a try-except code block to exit gracefully if the user supplied a non-numeric input!
try:
    n_print = int(input("How many most common words to print: "))
except:
    print('Must be an integer! Please try again. Goodbye.')
    sys.exit()
          
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)
# Close the file
file.close()


#End Script
