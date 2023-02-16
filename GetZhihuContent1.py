import requests
from bs4 import BeautifulSoup
import os
import base64

# 设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# 设置请求 URL
url = 'https://zhuanlan.zhihu.com/p/595050104'

# 发送 GET 请求
response = requests.get(url, headers=headers)

# 解析页面内容
soup = BeautifulSoup(response.content, 'html.parser')

# 创建本地文件夹
if not os.path.exists('images'):
    os.mkdir('images')

# 提取文章标题和内容
title = soup.find('h1', class_='Post-Title').get_text()
content = soup.find('div', class_='Post-RichTextContainer')

# 获取文章中的所有图片
imgs = content.find_all('img')

# 保存图片到本地文件夹
for i, img in enumerate(imgs):
    img_url = img['src']
    img_name = f'{i}.png'
    alt_text = img.get('alt', f'image{i}')
    img_path = os.path.join('images', alt_text + '.png')
    if img_url.startswith('data:'):  # 如果是 data URI，使用 base64 解码并保存为 PNG 文件
        try:
            img_data = base64.b64decode(img_url.split(',')[1], validate=True)
            with open(img_path, 'wb') as f:
                f.write(img_data)
        except (ValueError, TypeError):
            print(f'Error: failed to decode image {i}')
    else:  # 如果不是 data URI，使用 requests 库下载图片
        with open(img_path, 'wb') as f:
            f.write(requests.get(img_url).content)

# 输出结果
print(f'Title: {title}')
print(f'Content: {content.get_text()}')
