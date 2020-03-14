import numpy as np
from PIL import Image
import os

def is_img(ext):
    ext = ext.lower()
    if ext == '.jpg':
        return True
    elif ext == '.png':
        return True
    elif ext == '.jpeg':
        return True
    elif ext == '.bmp':
        return True
    else:
        return False


def BCC_test():
    BCC_test_tmp=[]
    for file in os.listdir("Images/BCC_test"):
        
        if is_img(os.path.splitext(file)[1]):
        
            img = Image.open("Images/BCC_test"+"/"+file)
            image_file = img.convert('L')
            img_convert_ndarray = np.array(image_file)
            BCC_test_tmp.append(img_convert_ndarray)
    BCC_test_tmp=np.array(BCC_test_tmp)
    return BCC_test_tmp

def FCC_test():
    FCC_test_tmp=[]
    for file in os.listdir("Images/FCC_test"):
        
        if is_img(os.path.splitext(file)[1]):
        
            img = Image.open("Images/FCC_test"+"/"+file)
            image_file = img.convert('L')
            img_convert_ndarray = np.array(image_file)
            FCC_test_tmp.append(img_convert_ndarray)
    FCC_test_tmp=np.array(FCC_test_tmp)
    return FCC_test_tmp

def BCC_train():
    BCC_train_tmp=[]
    for file in os.listdir("Images/BCC_train"):
        
        if is_img(os.path.splitext(file)[1]):
        
            img = Image.open("Images/BCC_train"+"/"+file)
            image_file = img.convert('L')
            img_convert_ndarray = np.array(image_file)
            BCC_train_tmp.append(img_convert_ndarray)
    BCC_train_tmp=np.array(BCC_train_tmp)
    return BCC_train_tmp

def FCC_train():
    FCC_train_tmp=[]
    for file in os.listdir("Images/FCC_train"):
        
        if is_img(os.path.splitext(file)[1]):
        
            img = Image.open("Images/FCC_train"+"/"+file)
            image_file = img.convert('L')
            img_convert_ndarray = np.array(image_file)
            BCC_test_tmp.append(img_convert_ndarray)
    FCC_train_tmp=np.array(FCC_train_tmp)
    return FCC_train_tmp
