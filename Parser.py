from bs4 import BeautifulSoup
from Networking import network
import re

class parser:

    def get_content(url):
        #get content from the page source obtained via BeautifulSoup
        page = network.get_page(url)
        parsed_content = BeautifulSoup(page.content,'html.parser')
        return parsed_content


    def get_links(info,domain_name):
        #Extract all links from the source provided
        page_links = []
        img_links = []
        for link in info.find_all('a',href=True):
            Link = link.get('href')
            # Rule for extracting the web page links
            if Link[0] != '#' and Link.find('/w/index.php') == -1  and Link.find('/wiki/') == 0:
                pos = Link.find('/wiki/')
                # remove internal linking
                if Link[pos:].find(':') == -1:
                    page_links.append(domain_name+Link)
            # Rule for extracting images links
            if link.has_attr('class') and link['class'][0] == 'image' and link.get('href').find('/wiki/') == 0:
                img_links.append(domain_name+link.get('href'))
        return page_links, img_links

    def get_data(info, imgFlag = False):
        #Getting all the headline from the page
        #So that when searching for word in the index only the sites with most useful information are being provided

        # extract image data
        if imgFlag:
            data = info.title.contents[0].lower()
            data = data.replace('file:', '')
            data = data[:data.rfind('.')]
            return re.sub('[\W\d]+', ' ', data)
        data = info.title.contents
        temp = re.sub('[\W]+', ' ', data[0]).lower()
        temp = temp.replace('wikipedia', '')  # remove the keyword Wikipedia with each title
        print('Page parsed - ', temp)
        data[0] = temp
        _info = info.find('body')  # parse only the elements in the body of the page
        for d in _info.find_all('span', {'class': 'mw-headline'}):
            title = re.sub('[\W_]+', ' ', d['id']).lower()
            data.append(temp + " " + title)
        return data
