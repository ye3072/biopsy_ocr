# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:03:24 2020

@author: pc
"""

import os
import fnmatch

path = 'C:/Users/pc/Documents/biopsy2006_1'
for filename in os.listdir(path):
    if fnmatch.fnmatch(filename, '*.jpg'):
        image_num = int(filename.split('(')[1].split(')')[0])
        os.rename('%s/%s' % (path, filename), '%s/%s' % (path, filename.replace(' ', '')))
        