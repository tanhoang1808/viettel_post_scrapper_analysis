from utils.driver_config import chromeDriver
from utils.thread_workers import Threads
from bs4 import BeautifulSoup


class Page:
    def __init__(self,links:list):
        self.links = links
        self.chrome = chromeDriver()
        

    def countPage(self):
        return len( self.links)


   

    def GetPageLinks(self,base_website_path,index):
        driver = self.chrome.initDriver()
        
        
        request_url = base_website_path +'/tin-tuc/'+"?page="+str(index)  # 'https://www.viettelidc.com.vn/tin-tuc?Page=2'
        driver.get(request_url)
        
        html = driver.page_source

        bs = BeautifulSoup(html, 'html.parser')

        items = bs.find_all('div',class_='news-wrapper')
        for item in items:
        
            link = base_website_path + str(item.find('a').get('href'))
            self.links.append(link)
        
        
    def AccessPageItem(self, item, posts):
        print("called AccccessPageItem")
        driver = self.chrome.initDriver()
        
        try:
            index = self.links.index(item)
            print("index : ",index)
            driver.get(self.links[index])
            html = driver.page_source
            bs = BeautifulSoup(html, 'html.parser')
            if bs:
                
                title = bs.find('div', class_='news-detail-head').find('h1').get_text()
                content = bs.find('div', class_='news-detail-body').find('div', class_='news-content').get_text()
                post = PostInfo(title, content, self.links[index])
                posts.append(post)
            else:
                print("BeautifulSoup found no content.")
        finally:
            driver.quit()
            
        
        
        


    

def ProcessPage(page:Page,config):
    print("config : ",config)
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
    

    



def TransformToPageInfo(page:Page,config) -> list:
    max_thread = config['max_thread']
    thread = Threads(max_thread)
    
    posts = []
    list_of_posts = page.links
    
    def fetch_post(item):
        page.AccessPageItem(item,posts)

    thread.ExecWithThreadWorkerWithList(fetch_post,list_of_posts) 

    print(f'there are total : ${len(posts)} posts')
    return posts




    
        

class PostInfo(Page):
    def __init__(self,title,content,link):
        self.title = title
        self.content = content
        self.link = link


