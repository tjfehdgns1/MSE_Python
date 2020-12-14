#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 240
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
# ((2 + 10)+ 2) * 2 = 28

