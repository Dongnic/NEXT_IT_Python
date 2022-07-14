#!/usr/bin/env python
# coding: utf-8

# # 1일차

# In[1]:


print("hi")


# ## List 동적배열
# > 특징은 수정삭제가 가능하며 인덱스로 접근이 가능함.

# In[2]:


arr = [1, 'hi', True, 100]
print(arr[1])
arr[1]="test"
print(arr[1])


# In[3]:


# 요소추가
arr.append(1000)
print(arr)


# ## SET 중복이 허용되지 않는 자료구조

# In[5]:


arr2 = {1, 1, 2, 2, 3, 4}
print(arr2)


# In[6]:


arr3 = set()
arr4 = {}
#set dictionary 둘 다 중괄호를 사용하기 때문에 set은 set()로 선언
print(type(arr3))
print(type(arr4))


# In[8]:


import random
ran = random.randint(1,10)
# 랜덤 정수 반환 1~10
print(ran)


# ## 오늘의 문제 
# ### input으로 숫자를 입력 받아 그 수량으로 로또번호(6개 숫자)를 출력하시오
# >6개의 숫자는 중복이 허용되지 않으며 1 ~ 45의 수를 가진다.
# 
# ### while, for, set, len, input.. 등 사용

# In[9]:


#length 반환
print(len(arr))


# In[50]:


import random
a = int(input("숫자를 입력해주세요 : "))
print("===============로또 번호 생성기=============")
for i in range(a) :
    lotto = set()
    while len(lotto) <= 5 :
        lotto.add(random.randint(1,45))
    lotto = list(lotto)
    lotto.sort()    
    print(lotto)
print("===============로또 번호 생성기=============")    


# In[ ]:




