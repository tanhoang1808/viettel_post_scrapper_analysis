from parsing.page_parse import processPage
from utils.page_config import readPageConfig
from parsing.page_parse import Page
import sys
import warnings

def main():

    if len(sys.argv) < 2:
        warnings.warn('You not have indicate the runtime , program will be running on dev envinroment.....',category=RuntimeWarning)


    if len(sys.argv) == 2:
        target_environment = sys.argv[1]
    

    
    base_url,page_max,start_page,end_page = readPageConfig(target_environment)
    
    page = Page([])

    page_range = range(int(start_page),int(end_page))
    
    processPage(page, base_url, page_range)
    
    

if __name__ == '__main__':
    main()