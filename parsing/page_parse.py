from urllib.request import urlopen
from utils.driver_config import chromeDriver
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


   

    def getPageLinks(self,base_website_path,index):
        driver = self.chrome.initDriver()
        
        
        request_url = base_website_path +"?page="+str(index)  # 'https://www.viettelidc.com.vn/tin-tuc?Page=2'
        driver.get(request_url)
        
        html = driver.page_source

        bs = BeautifulSoup(html, 'html.parser')

        items = bs.find_all('div',class_='news-wrapper')
        for item in items:
        
            link = item.find('a').get('href')
            self.links.append(link)
        
        


    def accessPageIndex(self,index):
        driver = self.chrome.initDriver()

        page_count = self.countPage()
        if (index > page_count): 
            raise IndexError('Index is exceed pages , try again')
        
        request_url = self.links[index]
        print(request_url)


def processPage(page:Page,base_website_path,page_range):
    def fetch_links(index):
        page.getPageLinks(base_website_path, index)

    max_threads = 5  # Tùy chỉnh số threads phù hợp với tài nguyên máy
    # Sử dụng ThreadPoolExecutor để chạy song song
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        future_to_index = {executor.submit(fetch_links, index): index for index in page_range}

        # Duyệt qua từng thread và kiểm tra trạng thái hoàn thành
        for future in as_completed(future_to_index):
            index = future_to_index[future]
            try:
                future.result()  # Lấy kết quả để bắt lỗi (nếu có)
                print(f"Page {index} processed successfully.")
            except Exception as e:
                print(f"Error processing page {index}: {e}")



    
        

class PostInfo(Page):
    def __init__(self,title,content,link):
        self.title = title
        self.content = content
        self.link = link