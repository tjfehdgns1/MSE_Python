#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 130
import requests
비트코인 = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(비트코인['max_price']) - float(비트코인['min_price'])
시가 = float(비트코인['opening_price'])
최고가 = float(비트코인['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")
# request.get()을 이용하여 데이터를 가져올 수 있다.

