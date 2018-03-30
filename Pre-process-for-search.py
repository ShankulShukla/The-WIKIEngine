""""
This is basically the pre-processing of the index created in the crawling step.
Pre-processing gives us advantage over variation in words tackled in the search and efficiently mapping the search it to the correct result in the index.
For this purpose we are going to use two tools from the nltk (natural language tool kit) library ,which are stopwords and stemmer.
Description to the function of the tools can be found in the following links :
STEMMER -> https://en.wikipedia.org/wiki/Stemming
STOPWORDS -> https://en.wikipedia.org/wiki/Stop_words
"""

import json
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# loading the index structure in the program
with open('index.json','r') as inp:
    index=json.load(inp)

#used for storing processed indexing
data={}

st=SnowballStemmer('english')
s=stopwords.words('english')
for i in index.keys():
    si=i.split(" ")
    temp=[]
    for j in si:
        if j not in temp:
            temp.append(st.stem(j))
    k=' '.join(map(str,temp))
    if k in data:
        for l in index[i]:
            data[k].append(l)
    else:
        data[k]=index[i]


#creating a new database for the processed index, specially used for searching
with open('data.json','w') as op:
    json.dump(data,op)
