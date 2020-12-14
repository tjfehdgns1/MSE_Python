#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 220
def print_max(a, b, c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)
print_max(1, 50, 100)
print_max(150, 20, 1)
# def로 함수를 만들고 최대값이 나오게 한다.

