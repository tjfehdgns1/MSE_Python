#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 210
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()
# def로 message#n()를 함수로 만들어 준다.
# for문에서 message2()와 print('C')를 3번 반복한다. 그리고 message1()을 출력한다.

