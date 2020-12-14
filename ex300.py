#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 300 try, except, else, finally 구조 사용해보기
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")
# try로 실행하고 except로 예외가 발생했을때 실행한다.
# finally 로 마지막에 항상 수행할 코드를 실행 시킨다.

