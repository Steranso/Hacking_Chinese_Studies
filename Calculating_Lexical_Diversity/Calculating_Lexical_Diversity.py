#!/usr/bin/env python
# coding: utf-8

# In[1]:


# For this assignment you will need to submit a text file containing some document to analyze,/n
# a python script, and a short essay.
# Find a text document related to China that you want to analyze. This can be an article from
# Wikipedia, a text from Project Gutenberg, or a text from one of the corpora we have seen in
# class. Your file can be in either English or Chinese.
# The python script should do the following:
# Open the file and clean the text, calculate the frequencies of all words in the document,
# and calculate the text's lexical diversity. At the end, the script should print the document's
# lexical diversity, as well as the top ten most frequent words in the document.
# In a short 300-500 word essay, please address the following:
# Which text did you pick, and why? Who wrote it, and for what purpose (if it was anonymously
# written, tell me that)? Where did you find it? What other kinds of texts are available from the
# same source? What is the text's lexical diversity? What are the most common words? Are lexical
# diversity/common words useful measures for understanding your text? Why or why not? How might
# you filter the common words to learn something more useful?
# Speculate on how you might push your analysis futher. What would you do next, if you knew how?
# Upload all three documents here (I need to be able to run your code to properly grade your work).


# In[5]:


#Reading in the file, may run into problem and may need to add .txt onto script
with open("Project_1_text_file",'r', encoding='utf8') as rf:
    text=rf.read()


#need to standarize all characters, remove unnecessary characters that an possibly impact word counts
text=text.lower().replace(",","").replace(".","").replace("[]","").replace("\n", " ")

#get the words in the texts
words = text.split(" ")
#get the unique words
unique_words = set(words)

word_freq = {}
#iterate through all of the words and count hteir frequency
for word in unique_words:
    freq = words.count(word)
    word_freq[word] = freq
print(word_freq)

#sort the keys by their values
sorted_words = sorted(word_freq, key = word_freq.get, reverse = True)
#print(sorted_words[:10])
#or we could print how often the words occur
print("These are the counts of the ten most common words and how often they appear:")
for word in sorted_words[:10]:
    print(word, word_freq[word])

#Finding the lexical diversity of the passage
lex_diversity = len(unique_words)/len(words)
lex_diversity = str(lex_diversity)
print("The lexical diversity of this document is " + lex_diversity)


# In[4]:





# In[ ]:




