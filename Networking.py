#all functions related to networking
import requests
import sys
from urllib.parse import urlparse

class network:

    def get_page(url):
        try:
            page = requests.get(url)
            #print("PAGE STATUS-", page)
            """
            Can see status of the pages also being loaded 
            Status in 200's are the best loaded
            """
            return page
        except:
            print('Error loading the page - ',url)
            sys.exit(1)



    def get_domain(url):
        try:
            domain = urlparse(url).netloc # Network location part
            return 'https://' + domain
        except:
            print('Error while getting the domain name!!!')
            sys.exit(1)
