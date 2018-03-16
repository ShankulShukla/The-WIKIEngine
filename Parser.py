from bs4 import BeautifulSoup
from Networking import network
class parser:

    def get_content(url):
        #get content from the page source obtained via BeautifulSoup
        page=network.get_page(url)
        parsed_content=BeautifulSoup(page.content,'html.parser')
        return parsed_content


    def get_links(info,domain_name):
        #Extract all links from the source provided
        links=[]
        for link in info.find_all('a',href=True):
            Link=link.get('href')
            if Link[0] != '#' and Link.find('/w/index.php') == -1  and Link.find('/wiki/') == 0: #extacting the most useful links from the page
                pos=Link.find('/wiki/')
                if Link[pos:].find(':')==-1:
                    links.append(domain_name+Link)
        return links

    def get_data(info):
        #Getting all the headline from the page
        #So that when searching for word in the index only the sites with most useful information are being provided
        data = info.title.contents
        print(data)#printing out the title of pages being crawl
        temp = str(data[0])
        temp = temp.replace(' - Wikipedia','')#remove the keyword Wikipedia with each title
        data[0] = temp
        info=info.find('body') #parse only the elements in the body of the page
        for d in info.find_all('span',{'class' : 'mw-headline'}):
            data.append(temp+" "+d['id']) #add all the headlines
        return data
