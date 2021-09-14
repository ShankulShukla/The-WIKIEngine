# The WIKIEngine

## INTRODUCTION -

- WIKIEngine is a Wikipedia-based search engine built on top of a multi-threaded and efficient web crawler. 
- The WIKIEngine is capable of querying relevant Wikipedia pages as well as images associated with the user search. 
- Currently, WIKIEngine queries over 100,000 pages and over 50,000 images indexed by the web crawler. 
- In addition to searching, the WIKIEngine is also able to provide search suggestions (do you mean functionality), if the WIKIEngine is not able to find any relevant results under the user search. 
- WIKIEngine categorizes search results into "most relevant" and "other relevant" results, based on the relevance of the result page or image with respect to the user search. 
- WIKIEngine's web crawler scrapes the pages for the most relevant data and then indexes them into its database. Creating union pages under the same key, noting page references for keys, and using NLP to optimize the key indexing corresponding to the pages are some features of the crawler.
- Visit appropriate files to understand the functionality in detail, I have tried to add a brief comment for each function.

**WIKIEngine** is a simple, multi-threaded and efficient web crawler which mimic's the functionalities of usual web spider but it is also having additional feature of a search engine for surfing over the internet a.k.a providing useful results for searched keyword.


Beginners can understand what crawler is ... by looking over the [Wikipedia](https://en.wikipedia.org/wiki/Web_crawler) page on the topic which for refrence states..

> '*A Web crawler, sometimes called a spider, is an Internet bot that systematically browses the World Wide Web, typically for the purpose of Web indexing (web spidering).
Web search engines and some other sites use Web crawling or spidering software to update their web content or indices of others sites' web content. Web crawlers copy pages for processing by a search engine which indexes the downloaded pages so users can search more efficiently.*'


- **WIKIEngine** is good way for beginners trying to understand the working of crawler a.k.a spiders in a very easy and implemented manner.
- One can also understand that how *multithreading* can be used to achive maximum efficency in API related operation by the CPU.
- It also serve as a good example of how we can scrape data from websites and process it to obtain uesful data , which lead onto the formation of data mining intellect.
- **WIKIEngine** can also be used to interpret the basics of how search engines make use of the web index created by crawler to provide best results for the varied inputs by users.
- Best results are being formulated by the use of the *stemming* and *stopwords* tools available in nltk(natural language tool kit) library.

## INTERNAL OVERVIEW -

The **WIKIEngine** starts with a URL to visit taken from the user as input known as the *seed page*. As the crawler visits the seed page, it gets bunch of hyperlinks in the page and adds them to the list of URL's to be visited, also different title keywords found while scraping the page act as the keys for the index dictionary and url associated with that word is used in the value list of the dictionary.

These task are being operated in the guidance of *threader* which divides the task of visiting the pages into threads, for concurrent execution leading to *maximum utilization of CPU*. This process is then repeated in accordance to the number of pages to be crawled and the size of index to be built as the user want. 

At last user can make use of the index dictionary created via crawler stored in a json file to search for words and can find the most relevant webpages in accordance to the criteria provided in the WIKI-search.

### For more undersatnding refer to following illustration- 
> Process start at main_spider.py (for crawling) and WIKIsearch.py (for searching)

![project](https://user-images.githubusercontent.com/30331393/38129174-7fa1bf22-341b-11e8-98a9-0ee809ca1144.png)


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

