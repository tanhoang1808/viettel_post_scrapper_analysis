from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class chromeDriver:
    
    def __init__(self,arguments:list=None,default_argument = ['--headless','--no-sandbox']):
        """
        Initialize custom ChromeDriver 

        """
        
        self.chrome_options = Options()

        if arguments is None:
            for arg in default_argument:
                self.chrome_options.add_argument(arg)


        list_arguments = ['--headless','--disable-gpu','--no-sandbox','--disable-dev-shm-sage']

        if isinstance(arguments,list) and arguments is not None:
            for arg in arguments:
                if arg in list_arguments:
                    self.chrome_options.add_argument(arg)
    
        
    def initDriver(self):
        self.driver = webdriver.Chrome(options=self.chrome_options)
        return self.driver

