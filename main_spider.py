from Parser import parser
from Networking import network
import time
import threading
from Update_index import update
from signal import signal, SIGINT

class webcrawler:
    """"
    The dictionary 'index' use to store the dictionary having words as keys and the website where it was found to be its values in a appended list format.
    The list 'tocrawl' is used to store the websites which are there to be crawled by the scraper as a appended list format.
    The list 'crawled' is used to store the websites which are already being crawled , to avoid the redundancy of scraping that website again.
    The thread is keep the record the list of thread initiated.
    Domain_name is class string which is used by functions to generate urls for scraping.
    """
    index = {}
    imgIndex = {}
    tocrawl = []
    crawled = []
    imagecrawled = []
    thread = []
    domain_name = ''

    def add_to_index(data,url):
        # building up the index of word and website
        for word in data:
            if word in webcrawler.index.keys():
                webcrawler.index[word].add(url)
            else:
                webcrawler.index[word]={url}

    def add_to_imageIndex(data, url):
        # building up the index of images in the website
        if data in webcrawler.imgIndex.keys():
            webcrawler.imgIndex[data].add(url)
        else:
            webcrawler.imgIndex[data]={url}

    def union(a,b):
        #union function so that no website are repeatedly crawled
        for i in b:
            if i not in a:
                a.append(i)


    def main(self,link,status):
        #dividing the links from input site into separate threads of sites for crawling
        i = 0
        division = 100 #Division parameter for dividing the sites from the link into different threads ...this can be played on with
        while i<len(link):
            j = i+division
            if j>len(link):
                j = len(link)
            t = threading.Thread(target=self.sender,args=(link[i:j],status,),daemon=True) #daemon thread
            webcrawler.thread.append(t)
            t.start()
            i = j
        for i in webcrawler.thread:
            i.join()

    def sender(self,urls,status):
        #generater function for the crawler ..sending out url's to the crawler
        if status == 1:
            for i in urls:
                self.crawl(i)
        else:
            for i in urls:
                self.crawl(i, status)

    def check_tocrawl(self):
        #to crawl the left over url's in the tocrawl
        status = 0
        webcrawler.scrape(status)

    def crawl(self,url, status = 1):
        webcrawler.tocrawl.append(url)
        webcrawler.scrape(status)

    def scrape(status,count=3):
        # Main scraper function
        # can play around with the count according to size of index of words with sites
        if status == 0:
            # crawling the left over url in the tocrawl list
            count = len(webcrawler.tocrawl)
        while webcrawler.tocrawl and count > 0:
            page = webcrawler.tocrawl.pop(0)  # pop from the beginning
            if page not in webcrawler.crawled:
                info = parser.get_content(page)
                links, imagelinks = parser.get_links(info, webcrawler.domain_name)
                data = parser.get_data(info)
                webcrawler.imageCrawl(imagelinks)
                webcrawler.add_to_index(data, page)
                if status == 1:
                    webcrawler.union(webcrawler.tocrawl, links)
                webcrawler.crawled.append(page)
                # print(webcrawler.crawled)  #can uncomment to see the list of sites already being crawled
                count = count - 1

    def imageCrawl(img_links):
        for page in img_links:
            if page not in webcrawler.imagecrawled:
                info = parser.get_content(page)
                data = parser.get_data(info, imgFlag = True)
                webcrawler.add_to_imageIndex(data, page)
                webcrawler.imagecrawled.append(page)


if __name__ == '__main__':

    print("Initiate spider with a url (from wikipedia) - ")
    url = input()  # input url from user
    print("Parsing the web ..... ")
    start = time.time()  # help in visualizing the time taken according to the threads taken with respect to the sites crawled
    content_first = parser.get_content(url)
    webcrawler.domain_name = network.get_domain(url)#extracting domain name
    page_links, img_links = parser.get_links(content_first,webcrawler.domain_name) #getting links from the input url page
    print(len(page_links))
    # link = parser.get_links(content_first,webcrawler.domain_name)
    crawler = webcrawler()#defining our crawler
    status = 1 #it signifies that at this moment we are not scraping the left over pages in tocrawllist
    page_links.append(url) # add first page for scraping
    crawler.main(page_links, status)
    #crawler.imageCrawl(img_links)
    """"
    One can just play around with crawling the pages left over in the tocrawl list ...but there is a caution over here, 
    The amount pages left in tocrawl list would be gigantic in number and would take very large amount of time for crawling 
    But one can have lot much much of data from them because at that time whole information found at each page crawled is collected and would be present at your index
    So implement it, as it's also threaded so it will decrease some of the overhead time for computation ..... just uncomment the next line
    """
    #crawler.check_tocrawl()
    #storing the index created in the json file for further usage
    update(webcrawler.index, webcrawler.imgIndex)

    print('TOTAL TIME TAKEN - ', time.time() - start)
    seen = []
    counter = 0
    for key in webcrawler.index.keys():
        for page in webcrawler.index[key]:
            if page not in seen:
                counter = counter + 1
                seen.append(page)
    #can print out the seen pages list
    print('TOTAL {} PAGES CRAWLED !! '.format(counter))
    print('WORD INDEX SIZE - ',len(webcrawler.index))
    print("You can now play with WIKI-search")
