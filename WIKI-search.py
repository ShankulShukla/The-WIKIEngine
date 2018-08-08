import json
from nltk.stem import SnowballStemmer
#including the index into the program
print("Loading the parsed dictionary...")
with open('data.json','r') as inp:
    index=json.load(inp)

#input the keyword to be searched
print("Search for a keyword - ")
raw_input=input()
t=raw_input.split(' ')
#converting the input search into the type of value stored in the index by using stemming
st=SnowballStemmer('english')
temp=[]
for i in t:
    temp.append(st.stem(i))
actual_input=' '.join(temp)
result=[] #to store the resultant links so that links do not occur more than twice as it can occur with similar looking keys in index and concurrent links at different stages of search
print('For the keyword "{}" related wikipedia pages are-'.format(raw_input))
## First stage of extracting the links related to the input keyword
## Criteria would be to search the exact word in the index serving as keys.

if actual_input in index.keys():
    print('\nMain link-',end=' ')
    for g in index[actual_input]:
        print(g)
        result.append(g)

## Second stage of extracting the links related to the input keyword
## Criteria would if in any of the key value contain the searched keyword as substring
print('*'*150)
print('SECOND STAGE RESULTS -')
for i in index.keys():
    if i.find(actual_input) != -1:
        for g in index[i]:
            if g not in result:
                print(g)
                result.append(g)


## Third stage of extracting the links related to the input keyword
## Criteria would to extract all links whose key value contain keyword in any form
print('*'*150)
print('THIRD STAGE RESULTS -')
for i in index.keys():
    q=actual_input.split(' ')
    for j in q:
        if i.find(j) !=-1:
            for g in index[i]:
                if g not in result:
                    print(g)
                    result.append(g)
            break

#if no result is found
if len(result) == 0:
    print('PLEASE !!! Do update the crawler for this keyword for future purposes....')
# for running the code purpose
print("*"*150)
print("See the code to understand what stages mean..")
