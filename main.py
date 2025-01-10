from parsing.page_parse import ProcessPageWithThreads,TransformToPageInfoWithThreads
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
    parser.add_argument('--thread', type=bool, help="Enable thread for performance")
    
    args = parser.parse_args()
   
    
    config = readPageConfig()
    # Ghi đè cấu hình từ tham số terminal
    config = OverrideConfig(config, args)

    # Hiển thị cấu hình cuối cùng
    print("Final Config:", config)

    return


    file_path = config['data_raw_path']
    
    page = Page([])

    print("config in main : ",config)
    
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

    

if __name__ == '__main__':
    main()