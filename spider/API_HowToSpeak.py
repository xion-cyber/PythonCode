#!/user/bin/env python
# -*- coding:utf-8 -*-

"""
This program is to call the API of HowToSpeak
author: YeYiqi
date: 2021-5-25
"""

import json
import requests

word = input('请输入中文')
url = 'http://howtospeak.org:443/api/e2c?user_key=dfcab6404295f9ed9e430f67b641a8e &notrans=0&text{}'.format(word)
res = requests.get(url)
json_data = json.load(res.text)
english_word = json_data['english']
print(english_word)