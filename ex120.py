#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과", "겨울" : "귤"}
answer = input("좋아하는 과일은? ----> ")
if answer in fruit.values():
    print("(⊙o⊙) 정답입니다.")
else:
    print("－_－b 오답입니다.")
# 딕셔너리.valuse()를 이용하여 딕셔너리 안에 value를 확인 할 수 있다.

