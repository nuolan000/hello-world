import requests

def get_douyin_hot():
    """获取抖音热榜"""
    url = "https://www.douyin.com/hot"
    response = requests.get(url)
    print(f"状态码: {response.status_code}")
    
if __name__ == "__main__":
    get_douyin_hot()
