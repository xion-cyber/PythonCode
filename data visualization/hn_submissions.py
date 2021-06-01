import requests
import os
from operator import itemgetter

# 执行API调用并存储响应
s = requests.session()

s.keep_alive = False
os.environ['NO_PROXY'] = 'stackoverflow.com'
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
requests.adapters.DEFAULT_RETRIES = 5
r = requests.get(url, verify=False)
print("Status code:", r.status_code)

# 处理每篇文章的信息
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    #对于每一篇文章，都采用一个API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' + 
            str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:",submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])
