#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np
from PIL import Image
import os


# In[88]:


def BCC_test():
    BCC_test_tmp=[]
    for file in os.listdir("Images/BCC_test"):
        img = Image.open("Images/BCC_test"+"/"+file)
        image_file = img.convert('L')
        img_convert_ndarray = np.array(image_file)
        BCC_test_tmp.append(img_convert_ndarray)
    return BCC_test_tmp
    


# In[89]:


def FCC_test():
    FCC_test_tmp=[]
    for file in os.listdir("Images/FCC_test"):
        img = Image.open("Images/FCC_test"+"/"+file)
        image_file = img.convert('L')
        img_convert_ndarray = np.array(image_file)
        FCC_test_tmp.append(img_convert_ndarray)
    return FCC_test_tmp


# In[90]:


def BCC_train():
    BCC_train_tmp=[]
    for file in os.listdir("Images/BCC_train"):
        if file == ".DS_Store":
            pass
        else:
            img = Image.open("Images/BCC_train"+"/"+file)
            image_file = img.convert('L')
            img_convert_ndarray = np.array(image_file)
            BCC_train_tmp.append(img_convert_ndarray)
    return BCC_train_tmp


# In[91]:


def FCC_train():
    FCC_train_tmp=[]
    for file in os.listdir("Images/FCC_train"):
        if file == ".DS_Store":
            pass
        else:
            img = Image.open("Images/FCC_train"+"/"+file)
            image_file = img.convert('L')
            img_convert_ndarray = np.array(image_file)
            FCC_train_tmp.append(img_convert_ndarray)
    return FCC_train_tmp


# In[ ]:




