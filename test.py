#!/usr/bin/enc python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:11:00 2019

@author: ninad
"""

import os
import cv2
import pandas as pd
import sys
import numpy as np
from progressbar import ProgressBar

from data_augmentation import DataAugmentation
from image_process import ImageProcess

image_process = ImageProcess()
data_aug = DataAugmentation()

csv_fname = '/home/mir-lab/Ninad_Thesis/Test/Test.csv'
csv_header = ['image_fname', 'steering_angle']
df = pd.read_csv(csv_fname, names=csv_header, index_col=False)
num_data = len(df)
text = open('/home/mir-lab/Ninad_Thesis/Test/Shift/Shift.txt','w+')
bar = ProgressBar()
for i in bar(range(num_data)):
    image_name = df.loc[i]['image_fname']
    steering = df.loc[i]['steering_angle']
    image_path = '/home/mir-lab/Ninad_Thesis/Test/' + image_name + '.jpg'
    image = cv2.imread(image_path)
    image = cv2.resize(image, (160, 70))
    image = image_process.process(image)
    shift_image, shift_steering = data_aug.shift(image, steering)
    cv2.imwrite('/home/mir-lab/Ninad_Thesis/Test/Shift/S_' + image_name + '.jpg', shift_image)
    text.write('S_' + str(image_name) + '\t' + str(shift_steering) + '\r''\n')
    



