import json
import csv

def json_to_csv(json_file, csv_file):
    """
    Chuyển đổi file JSON thành file CSV.
    
    Args:
        json_file (str): Đường dẫn đến file JSON đầu vào.
        csv_file (str): Đường dẫn để lưu file CSV đầu ra.
    """
    try:
        # Đọc dữ liệu từ file JSON
        with open(json_file, 'r', encoding='utf-8') as jf:
            data = json.load(jf)

        # Kiểm tra dữ liệu JSON
        if isinstance(data, list) and len(data) > 0:
            # Lấy danh sách các key làm header cho CSV
            headers = data[0].keys()

            # Ghi dữ liệu vào file CSV
            with open(csv_file, 'w', encoding='utf-8', newline='') as cf:
                writer = csv.DictWriter(cf, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data)

            print(f"File CSV đã được tạo tại: {csv_file}")
        else:
            print("Dữ liệu JSON không phải là danh sách hoặc rỗng!")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Sử dụng hàm
json_to_csv('data/raw_post/posts.json', 'data/csv/post.csv')


