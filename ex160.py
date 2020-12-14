#!/usr/bin/env python
# coding: utf-8

# In[9]:


# 160
list = ['ex160.ipynb', 'ex170.c', 'ex180.py', 'ex190.py']
for i in list:
    이름, 확장자 = i.split('.')
    if 확장자 == 'py' or 확장자 == 'ipynb':
        print(i)
# split()로 '.'을 기준으로 나누고 확장자가 'py'나 'ipynb'이면 출력한다.

