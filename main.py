from parsing.page_parse import ProcessPageWithThreads,TransformToPageInfoWithThreads,ProcessPage,TransformToPageInfo
from utils.page_config import readPageConfig
from utils.yaml_config import OverrideConfig
from parsing.page_parse import Page
import sys
import warnings
import json
import yaml
import argparse



def main():
    # Sử dụng argparse để truyền tham số từ terminal
    parser = argparse.ArgumentParser(description="Run Scrapper")
    parser.add_argument('--target', type=str, help="environment ")
    parser.add_argument('--thread', action='store_true', help="Enable thread for performance")
    
    args = parser.parse_args()
   
    print(args)
    config = readPageConfig()
    # Ghi đè cấu hình từ tham số terminal
    config = OverrideConfig(config, args)

    # Hiển thị cấu hình cuối cùng
    print("Final Config:", config)

    
    


    file_path = config['data_raw_path']
    
    page = Page([])

    
    if config['use_thread'] == True:
        print("Use threads")
        ProcessPageWithThreads(
        page = page,
        config=config
    )

        posts = TransformToPageInfoWithThreads(
            page = page,
            config = config
        )
        if posts is not None:
            with open(file_path,encoding='utf-8',mode='a') as file:
                json.dump([post.__dict__ for post in posts],file,ensure_ascii=False,indent=4)

    else:
        print("not use threads")
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