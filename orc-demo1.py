import requests
from bs4 import BeautifulSoup

# 发送请求并获取网页内容
url = "https://it.ithome.com/"
response = requests.get(url)
content = response.content

# 解析HTML内容，如下.strip() 用于去除 article.text 字符串开头和结尾的空格，使得提取出来的文本内容更加干净。
soup = BeautifulSoup(content, features="html.parser")
articles = soup.find_all('a', class_='title')

# 输出文章标题和URL地址
for article in articles:
    title = article.text.strip()
    url = article['href']
    print(title, url)