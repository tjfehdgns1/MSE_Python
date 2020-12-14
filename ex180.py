#!/usr/bin/env python
# coding: utf-8

# In[13]:


# 180
저가  = [100, 200, 400, 800, 1000]
고가 = [150, 300, 430, 880, 1000]
volatility = []
for i in range(5):
    차이 = 고가[i] - 저가[i]
    volatility.append(차이)
print(volatility)
# xxx.append()를 이용하여 리스트에 값을 추가한다.

