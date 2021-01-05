# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 11:37:16 2020

@author: pc
"""

import os
import fnmatch

path = 'C:/Users/pc/Documents/biopsy2006_1'
for filename in os.listdir(path):
    if fnmatch.fnmatch(filename, '*.jpg'):
        image_num = int(filename.split('(')[1].split(')')[0])
        os.system("tesseract %s/%s %s/%s --psm 6" % (path, filename, path, filename.split('.')[0]))
        #print("tesseract %s/%s %s/%s" % (path, filename, path, filename.rsplit('.jpg')[0]+".txt"))


#os.system("tesseract C:/Users/pc/Documents/tesseract/test.jpg C:/Users/pc/Documents/tesseract/test.txt")


