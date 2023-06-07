#!/usr/bin/env python
# coding: utf-8

# In[3]:


def my_function(arg1, arg2):   # Defines a new function
    return arg1 + arg2           # Function body (code to execute)


# In[4]:


my_function(4, 10)


# In[ ]:

def sum_3_items(x, y, z, print_args = False): 
    if print_args:                        
        print(x,y,z)
    return x + y + z


sum_3_items(5,10,20)        # By default the 

