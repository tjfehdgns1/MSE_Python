#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 290 부모클래스 생성자 호출
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()

