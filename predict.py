# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 19:30:54 2020

@author: cagda
"""

import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from sklearn.metrics import classification_report, confusion_matrix
import cv2

def predict(path,weight,img):
    
    b=0
    model = load_model(path)
    model.load_weights(weight)
    
    from keras.preprocessing import image
    #test_image = image.load_img(img, target_size = (112,112))
    
    predic_list=[]
    for i in img:
        i=cv2.resize(i, (112,112))
        i = image.img_to_array(i)
        i = np.expand_dims(i, axis = 0)
        result = model.predict(i)
        b=b+1
        if result[0][0] == 1:
            prediction = 'angry'
        
        elif result[0][1]:
            prediction = 'happy'
        elif result[0][2]:
            prediction = 'neutral'
        elif result[0][3]:
            prediction = 'sad'
        elif result[0][4]:
            prediction = 'surprise'
        
        predic_list.append(prediction)
            
    return predic_list