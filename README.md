# The WIKIEngine

## Introdution -

**WIKIEngine** is a Wikipedia-based search engine built on top of a multi-threaded and efficient web crawler. 

The *WIKIEngine* is capable of querying relevant Wikipedia **pages as well as images** associated with the user search. 

Currently, *WIKIEngine* queries over **100,000 pages** and over **50,000 images** indexed by the web crawler. 

In addition to searching, the *WIKIEngine* is also able to provide **search suggestions (do you mean functionality)**, if the *WIKIEngine* is not able to find any relevant results under the user search. 

*WIKIEngine* categorizes search results into **most relevant** and **other relevant** results, based on the relevance of the result page or image with respect to the user search. 

*WIKIEngine*'s web crawler scrapes the pages for the most relevant data and then indexes them into its database. Creating union pages under the same key, noting page references for keys, and using NLP to optimize the key indexing corresponding to the pages are some features of the crawler.

Web app for *WIKIEngine* is developed using flask and deployed on heroku.

Visit appropriate files to understand the functionality in detail, I have tried to add a brief comment for functions.

## Deployed WIKIEngine -

> The WIKIEngine is publicly deployed on Heroku Server [here](https://wikiengine.herokuapp.com/) or at https://wikiengine.herokuapp.com. 

![image](https://drive.google.com/uc?export=view&id=1AlOrTbZ3rM3IuBuAZ9KiOqoq4x1X_UtH)

> Spell check/ Search suggestion functionality -

![image](https://drive.google.com/uc?export=view&id=12BDkz_0hhTetSMChJ-nAViiuEBjYDqI1)

## Code overview -

**_static[Folder]_-** css and image resource for web app

**_templates[Folder]_-** HTML template for web app

**_Procfile_-** specifies commands that are executed by the web app on startup

**_apps.py_-** defines app object instance of Flask object, also from here application is started and requests are handled

**_Networking.py_-** request the page and handles the response

**_Parser.py_-** parse page to extract data for indexing 

**_Pre-process-for-search.py_-** pre-process the indexing created by crawler

**_Update_index.py_-** extend and update the indexing after crawl

**_index.json_-** json based page index

**_imgind.txt_-** cpickle based image index (space efficient and faster loading)

**_ind.txt_-** cpickle based page index (space efficient and faster loading)

**_main_spider.py_-** base web crawler handler

**_wikiSearch.py_-** base search handler



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

