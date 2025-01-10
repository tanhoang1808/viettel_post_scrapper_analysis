from parsing.page_parse import ProcessPage,TransformToPageInfo
from utils.page_config import readPageConfig
from parsing.page_parse import Page
import sys
import warnings
import json
def main():
   

    if len(sys.argv) < 2:
        warnings.warn('You not have indicate the runtime , program will be running on dev envinroment.....',category=RuntimeWarning)


    if len(sys.argv) == 2:
        target_environment = sys.argv[1]
    
    
    # base_url,page_max,start_page,end_page = readPageConfig('dev' or target_environment )
    config = readPageConfig('dev' or target_environment)
    file_path = config['data_raw_path']
    
    page = Page([])

    
    
    ProcessPage(
        page = page,
        config=config
    )

    posts = TransformToPageInfo(
        page = page,
        config = config
    )


    if posts is not None:
        with open(file_path,encoding='utf-8',mode='a') as file:
            json.dump([post.__dict__ for post in posts],file,ensure_ascii=False,indent=4)

    



     

    
    




if __name__ == '__main__':
    main()