# The WIKICrawler
## INTRODUCTION -

**WIKICrawler** is a simple, multithreaded and efficient web crawler which mimic's the functionalities of usual web spider but it is also having additional functionality of a search engine for surfing over the internet a.k.a providing useful results for searched keyword.


Beginners can understand what crawler is ... by looking over the [Wikipedia](https://en.wikipedia.org/wiki/Web_crawler) page on the topic which for refrence states..

'*A Web crawler, sometimes called a spider, is an Internet bot that systematically browses the World Wide Web, typically for the purpose of Web indexing (web spidering).
Web search engines and some other sites use Web crawling or spidering software to update their web content or indices of others sites' web content. Web crawlers copy pages for processing by a search engine which indexes the downloaded pages so users can search more efficiently.*'


- **WIKICrawler** is good way of beginners trying to understand the working of crawler a.k.a spiders in a very easy and implemented manner.
- One can also understand that how *multithreading* can be used to achive maximum efficency in API related operation by the CPU.
- It also serve as a good example of how we can scrape data from websites and process it to obtain uesful data , which lead onto the formation of data mining intellect.
- **WIKICrawler** can also be used to interpret the basics of how search engines make use of the web index created by crawler to provide best results for the varied inputs by users. 

## INTERNAL OVERVIEW -

The **WIKICrawler** starts with a URL to visit taken from the user as input known as the *seed page*. As the crawler visits the seed page, it gets bunch of hyperlinks in the page and adds them to the list of URL's to be visited, also different title keywords found while scraping the page act as the keys for the index dictionary and url associated with that word is used in the value list of the dictionary.
These task are being operated in the guidance of *threader* which divides the task of visiting the pages into threads, for concurrent execution leading to *maximum utilization of CPU*. This process is then repeated in accordance to the number of pages to be crawled and the size of index to be built as the user want. 

## FUTURE GOALS

To implement page ranking algorithm to display best and most relevant websites with each search of keywords in the index.

