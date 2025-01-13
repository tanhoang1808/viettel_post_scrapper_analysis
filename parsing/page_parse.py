from utils.driver_config import chromeDriver
from utils.thread_workers import Threads
from bs4 import BeautifulSoup
import re
import time
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
            print("link processed : ",link)
            self.links.append(link)
        
        
    def AccessPageItem(self, item, posts,base_url,limit_posts_to):
        print("called AccccessPageItem")
        driver = self.InitDriver()
        index = self.links.index(item)
        index = self.links.index(item)
        limit_posts = limit_posts_to
        print("index : ",index)
        if index > limit_posts:
            print("Access Limit of posts , returningg....!")
            return
        else:
            driver.get(self.links[index])
            time.sleep(30)
            html = driver.page_source
            bs = BeautifulSoup(html, 'html.parser')
            self.ParsePostObject(bs,index,posts,base_url)
            
        
    def ParsePostObject(self,soup,index,posts,base_url):
        
        if soup:
                title = soup.find('div', class_='news-detail-head')
                if title is not None:
                    title = title.find('h1').get_text().strip().replace('\n','')
                
                content = soup.find('div', class_='news-detail-body')
                if content is not None:
                    content = content.get_text().strip().replace('\n','')
                    
                date_post = soup.find('div',class_='news-detail-head')

                if date_post is not None:
                    date_post = soup.find('span').get_text().strip().replace('\n','')

                thumbnail = soup.find('img', class_='img-responsive')
                thumbnail_full_path = ''
                if thumbnail:
                    thumbnail_full_path = base_url + thumbnail['src']
                
                #Phân tích content
                # char_count = len(content) 
                # word_count = len(content.split()) 
                # sentence_count = len(re.split(r'[.!?]', content)) 
                # paragraph_count = len(content.split('\n\n')) 



                post = PostInfo(title, content, self.links[index],thumbnail_full_path,date_post)
                print(post.__dict__)
                posts.append(post)
        else:
                print("BeautifulSoup found no content.")

    # def AnalyzePostInfo(content):
    #     char_count = len(content) 
    #     word_count = len(content.split()) 
    #     sentence_count = len(re.split(r'[.!?]', content)) 
    #     paragraph_count = len(content.split('\n\n')) 
    #     return char_count,word_count,sentence_count,paragraph_count  
        
        
def ProcessPage(page:Page,config):
    
    base_website_path = config['base_url']
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
    base_url = config['base_url']
    limit_posts_to = config['limit_post']
    posts = []
    print(f"Scrapper crawl total ${len(page.links)} posts ")
    for item in page.links:
        page.AccessPageItem(item, posts, base_url,limit_posts_to)
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
    def __init__(self,title,content,link,thumbnail,date_post):
        self.date_post = date_post
        self.title = title
        self.content = content
        self.link = link
        self.thumbnail = thumbnail
        # self.char_count = char_count
        # self.word_count = word_count
        # self.sentence_count = sentence_count
        # self.paragraph_count = paragraph_count


