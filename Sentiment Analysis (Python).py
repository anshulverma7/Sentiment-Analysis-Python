# Author: Anshul Verma

# Sentiment Analysis 

# EM624 - Exercise 07

import nltk

# to open the text files
file1 = open("DemocraticDebate_NYT.txt","r")
file2 = open("DemocraticDebate_WSJ.txt","r")
file3 = open("stopwords_en.txt","r")

# to remove \n and generate text
text1 = file1.read()
text1.replace('\n', ' ')
text2 = file2.read()
text2.replace('\n', ' ')
text3 = file3.read()
text3.replace('\n', ' ')

# to remove stopwords and create list of words
words1 = []
for i in text1.strip().split():
    if i not in text3:
        words1.append(i)
words2 = []
for i in text2.strip().split():
    if i not in text3:    
        words2.append(i)

# to calculate and print the most frequent words    
fdist1 = nltk.FreqDist(words1)
fdist2 = nltk.FreqDist(words2)
print "\nThe top 10 words in DemocraticDebate_NYT.txt are:\n", fdist1.most_common(10)
print "\nThe top 10 words in DemocraticDebate_WSJ.txt are:\n", fdist2.most_common(10)

# to extract and print most frequent bigrams of frequency greater than 2
bigram1 = list(nltk.bigrams(words1))
bigram2 = list(nltk.bigrams(words2))
f1 = nltk.FreqDist(bigram1)
f2 = nltk.FreqDist(bigram2)
print "\nThe most frequent bigrams in DemocraticDebate_NYT.txt are:\n", list(filter(lambda x: x[1]>2, f1.most_common()))
print "\nThe most frequent bigrams in DemocraticDebate_WSJ.txt are:\n", list(filter(lambda x: x[1]>2, f2.most_common()))

# to create and print word clouds
from wordcloud import WordCloud
import matplotlib.pyplot as plt

string1 = ' '.join(words1)
string2 = ' '.join(words2)
wc1 = WordCloud(background_color="white", max_words=2000,stopwords=text3)
wc2 = WordCloud(background_color="white", max_words=2000,stopwords=text3)
wc1.generate(string1)
wc2.generate(string2)

plt.subplot(2, 1, 1)
plt.imshow(wc1)
plt.axis('off')
plt.title('New York Times')
plt.subplot(2, 1, 2)
plt.imshow(wc2)
plt.axis('off')
plt.title('Wall Street Journal')
plt.show()