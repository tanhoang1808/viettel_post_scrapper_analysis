from concurrent.futures import ThreadPoolExecutor, as_completed


class Threads:
    def __init__(self,threads):
        """
        params : threads -> max thread use to generate workers
        """
        self.max_threads = threads

    def ExecWithThreadWorkerWithIndex(self,fn,indexes):
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            future_to_index = {executor.submit(fn, index): index for index in indexes}

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
