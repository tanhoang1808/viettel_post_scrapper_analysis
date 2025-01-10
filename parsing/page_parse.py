from utils.driver_config import chromeDriver
from utils.thread_workers import Threads
from bs4 import BeautifulSoup

class Page:
    def __init__(self,links:list):
        self.links = links
        self.chrome_driver = chromeDriver().initDriver()
        

    def InitDriver(self):
        return self.chrome_driver

    def CloseDriver(self):
        if self.chrome_driver:
            self.chrome_driver.quit()

    def countPage(self):
        return len( self.links)


   

    def GetPageLinks(self,base_website_path,index):
        driver = self.InitDriver()
        
        
        request_url = base_website_path +'/tin-tuc/'+"?page="+str(index)  # 'https://www.viettelidc.com.vn/tin-tuc?Page=2'
        driver.get(request_url)
        
        html = driver.page_source

        bs = BeautifulSoup(html, 'html.parser')

        items = bs.find_all('div',class_='news-wrapper')
        for item in items:
        
            link = base_website_path + str(item.find('a').get('href'))
            self.links.append(link)
        
        
    def AccessPageItem(self, item, posts,base_url):
        print("called AccccessPageItem")
        driver = self.InitDriver()
        
        try:
            index = self.links.index(item)
            print("index : ",index)
            driver.get(self.links[index])
            html = driver.page_source
            bs = BeautifulSoup(html, 'html.parser')
            if bs:
                title = str( bs.find('div', class_='news-detail-head').find('h1').get_text()).strip().replace('\n','')
                content = str(bs.find('div', class_='news-detail-body').find('div', class_='news-content').get_text()).strip().replace('\n','')
                thumbnail = bs.find('img', class_='img-responsive')
                print("thumbnail : ",thumbnail)
                thumbnail_full_path = base_url + thumbnail['src']
                post = PostInfo(title, content, self.links[index],thumbnail_full_path)
                posts.append(post)
            else:
                print("BeautifulSoup found no content.")
        finally:
            # self.CloseDriver()
            pass    
            
        
        
        
def ProcessPage(page:Page,config):
    print("config : ",config)
    base_website_path = config['base_url']
    max_thread = config['max_thread']
    start_page = config['start_page']
    end_page = config['end_page']

    for index in range(int(start_page), int(end_page)):
        page.GetPageLinks(base_website_path, index)
    

    

def ProcessPageWithThreads(page:Page,config):
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
    base_url = config['base_url']
    
    posts = []
    list_of_posts = page.links
    
    for item in page.links:
        page.AccessPageItem(item, posts, base_url)
    return posts



def TransformToPageInfoWithThreads(page:Page,config) -> list:
    max_thread = config['max_thread']
    base_url = config['base_url']
    thread = Threads(max_thread)
    
    posts = []
    list_of_posts = page.links
    
    def fetch_post(item):
        page.AccessPageItem(item,posts,base_url)

    thread.ExecWithThreadWorkerWithList(fetch_post,list_of_posts) 

    print(f'there are total : ${len(posts)} posts')
    return posts




    
        

class PostInfo(Page):
    def __init__(self,title,content,link,thumbnail):
        self.title = title
        self.content = content
        self.link = link
        self.thumbnail = thumbnail


