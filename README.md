# The WIKIEngine

## Introdution -

- **WIKIEngine** is a Wikipedia-based search engine built on top of a multi-threaded and efficient web crawler. 
- The *WIKIEngine* is capable of querying relevant Wikipedia **pages as well as images** associated with the user search. 
- Currently, *WIKIEngine* queries over **100,000 pages** and over **50,000 images** indexed by the web crawler. 
- In addition to searching, the *WIKIEngine* is also able to provide **search suggestions (do you mean functionality)**, if the *WIKIEngine* is not able to find any relevant results under the user search. 
- *WIKIEngine* categorizes search results into **most relevant** and **other relevant** results, based on the relevance of the result page or image with respect to the user search. 
- *WIKIEngine*'s web crawler scrapes the pages for the most relevant data and then indexes them into its database. Creating union pages under the same key, noting page references for keys, and using NLP to optimize the key indexing corresponding to the pages are some features of the crawler.
- Visit appropriate files to understand the functionality in detail, I have tried to add a brief comment for each function.

## Deployed WIKIEngine -

> The WIKIEngine is publicly deployed on Heroku Server [here](https://wikiengine.herokuapp.com/) or at https://wikiengine.herokuapp.com. 

![image](https://drive.google.com/uc?export=view&id=1AlOrTbZ3rM3IuBuAZ9KiOqoq4x1X_UtH)

> Spell check/ Search suggestion functionality -

![image](https://drive.google.com/uc?export=view&id=12BDkz_0hhTetSMChJ-nAViiuEBjYDqI1)

![project](https://user-images.githubusercontent.com/30331393/38129174-7fa1bf22-341b-11e8-98a9-0ee809ca1144.png)

## Code overview -


## How to use it...
1. Just git clone the repo.
2. In command prompt, cd to the directory of WIKIEngine.
3. Run the main_spider.py with python.(parsing the web)
4. Run the WIKI-search.py with python to search over different word in new parsed dictionary formed
> For more understanding look forward to see the code.

## FUTURE SCOPE

> For maintaining the simplicity following ideas are being ignored, but one can implement these ideas for providing optimizations to **WIKIEngine** -
- Users can the store the index dictionary into an [hash table](https://en.wikipedia.org/wiki/Hash_function) for fast accessing.
- [Suffix tree](https://en.wikipedia.org/wiki/Suffix_tree) implementation for efficient searching over the index. 

