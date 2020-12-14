#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 200
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
profit = 0
for row in ohlc[1:]:
    profit += (row[3] - row[0])
print(profit)
# ohlc 행렬의 2~4행의 4번째-1번째렬을 뺀 값을 다 더한다.

