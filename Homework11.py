#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
from sympy import *
from sympy.plotting import plot


# In[2]:


x = Symbol('x')
fx = -5*x**2 + 10*x - 150
fx


# In[3]:


p = plot(fx, (x,-10,10))


# In[4]:


sqrt_1,sqrt_2 = solve(fx)
print(sqrt_1, sqrt_2)


# In[11]:


pr = diff(fx)
print(pr)


# In[6]:


apex = solve(diff(fx))[0]
print(apex)


# In[7]:


solve(diff(fx) > 0)


# In[8]:


solve(diff(fx) < 0)


# In[17]:


solve(fx < 0)
print(solve (fx < 0))


# In[18]:


solve(fx > 0)
print(solve (fx > 0))


# In[ ]:




