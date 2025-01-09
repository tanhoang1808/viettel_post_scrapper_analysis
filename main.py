from parsing.page_parse import ProcessPage,TransformToPageInfo
from utils.page_config import readPageConfig
from parsing.page_parse import Page
import sys
import warnings

def main():
   

    if len(sys.argv) < 2:
        warnings.warn('You not have indicate the runtime , program will be running on dev envinroment.....',category=RuntimeWarning)


    if len(sys.argv) == 2:
        target_environment = sys.argv[1]
    
    
    # base_url,page_max,start_page,end_page = readPageConfig('dev' or target_environment )
    config = readPageConfig('dev' or target_environment)
    
    
    page = Page([])

    
    
    ProcessPage(
        page = page,
        config=config
    )
     

    
    




if __name__ == '__main__':
    main()