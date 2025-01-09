from urllib.request import urlopen
from utils.driver_config import chromeDriver
from utils.thread_workers import Threads
from bs4 import BeautifulSoup
import re
import urllib
import ssl
from concurrent.futures import ThreadPoolExecutor, as_completed

import sys


class Page:
    def __init__(self,links:list):
        self.links = links
        self.chrome = chromeDriver()
        

    def countPage(self):
        return len( self.links)


   

    def GetPageLinks(self,base_website_path,index):
        driver = self.chrome.initDriver()
        
        
        request_url = base_website_path +"?page="+str(index)  # 'https://www.viettelidc.com.vn/tin-tuc?Page=2'
        driver.get(request_url)
        
        html = driver.page_source

        bs = BeautifulSoup(html, 'html.parser')

        items = bs.find_all('div',class_='news-wrapper')
        for item in items:
        
            link = item.find('a').get('href')
            self.links.append(link)
        
        


    def AccessPageIndex(self,index):
        driver = self.chrome.initDriver()

        page_count = self.countPage()
        if (index > page_count): 
            raise IndexError('Index is exceed pages , try again')
        
        request_url = self.links[index]
        print(request_url)

    

def ProcessPage(page:Page,config):
    print(config)
    base_website_path = config['base_url']
    max_thread = config['max_thread']
    start_page = config['start_page']
    end_page = config['end_page']
    page_range = range(int(start_page),int(end_page))

    def fetch_page_links(index):
        page.GetPageLinks(base_website_path, index)

    # Sử dụng ThreadPoolExecutor để chạy song song
    thread = Threads(max_thread)
    thread.ExecWithThreadWorkerWithIndex(fetch_page_links,page_range)
    


def TransformToPageInfo(page_range):
    thread = Threads(5)




    
        

class PostInfo(Page):
    def __init__(self,title,content,link):
        self.title = title
        self.content = content
        self.link = link