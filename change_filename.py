# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:01:04 2020

@author: pc
"""

import os
import fnmatch

path = 'C:/Users/pc/Documents'
max_num = 0
for filename in os.listdir(path):
    if fnmatch.fnmatch(filename, '*.jpg'):
        num = int(filename.split('-')[1].split('.')[0])
        file_path = '%s/%s'%(path, filename.split('-')[0])
        if num > max_num:
            max_num = num
        
print(max_num)
print(file_path)

# start 찾기
paraquat_path = 'C:/Users/pc/Documents/Paraquat'
start = 0
for paraquat in os.listdir(paraquat_path):
    if fnmatch.fnmatch(paraquat, '*.jpg'):
        num = int(paraquat.split('_')[0].replace('C', ''))
        if num > start:
            start = num
start += 1
print(start)

for i in range(1, max_num + 1):
    if i % 2 == 1:
        i = str(i).zfill(2)
        os.rename('%s-%s.jpg' % (file_path, i), '%s/C%d_1.jpg' % (path, start))
    else:
        i = str(i).zfill(2)
        os.rename('%s-%s.jpg' % (file_path, i), '%s/C%d_2.jpg' % (path, start))
        start += 1
    
