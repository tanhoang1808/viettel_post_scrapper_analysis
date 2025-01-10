from concurrent.futures import ThreadPoolExecutor, as_completed


class Threads:
    def __init__(self,threads):
        """
        params : threads -> max thread use to generate workers
        """
        self.max_threads = threads
        self.executor = ThreadPoolExecutor(max_workers=self.max_threads)


    def ExecWithThreadWorkerWithIndex(self,fn,indexes):
        print(f"ExecWithThreadWorkerWithIndex are working on ${self.max_threads} worker")

        future_to_index = {self.executor.submit(fn, index): index for index in indexes}

            # Duyệt qua từng thread và kiểm tra trạng thái hoàn thành
        for future in as_completed(future_to_index):
            index = future_to_index[future]
            try:
                future.result()  # Lấy kết quả để bắt lỗi (nếu có)
                print(f"Page {index} processed successfully.")
            except Exception as e:
                print(f"Error processing page {index}: {e}")

    def ShowMaxWorkers(self):
        return self.max_threads

    def ExecWithThreadWorkerWithList(self,fn,list:list):
        print(f"ExecWithThreadWorkerWithList are working on ${self.max_threads} worker")
         
         
        future_to_item = {self.executor.submit(fn, item): item for item in list}
            
            # Duyệt qua từng thread và kiểm tra trạng thái hoàn thành
        for future in as_completed(future_to_item):
            item = future_to_item[future]
            print("item : ",item)
            try:
                future.result()  # Lấy kết quả để bắt lỗi (nếu có)
                print(f"{item} processed successfully.")
            except Exception as e:
                print(f"Error processing page {item}: {e}")
