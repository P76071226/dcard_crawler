from bs4 import BeautifulSoup
import re
import requests
import json

# To get article ID lists
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
# save 100 articles id in post_id_list
post_result = requests.get('http://dcard.tw/_api/forums/trending/posts?limit=100', headers = header)
post = json.loads(post_result.text)
#print(post)
post_id_list=  []
for dict in (post):
    post_id_list.append(dict['id'])
print(post_id_list)

#print(post_id_list)
prefix_url_article = 'http://dcard.tw/_api/posts/'
article_content = []

for i in range(10):
    # combine url with article id
    article_id = str(post_id_list[i])  # int into str
    url = prefix_url_article + article_id
    # get article content by id
    req = requests.get(url)
    req_json = json.loads(req.text)
    str1 = (req_json['content'])
    article_content.append(str1)

print(article_content)
