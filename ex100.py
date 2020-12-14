#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 100 zip과 dict
game = ['컨트롤', '인왕', '다잉라이트', '용과같이']
game_price = [20000, 15000, 12000, 60000]
game_table = dict(zip(game, game_price))
print(game_table)
# 2개의 리스트를 zip()으로 key와 value로 지정해서 딕셔너리로 만들 수 있다.

