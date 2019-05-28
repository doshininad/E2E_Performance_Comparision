#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
#
class Config:
    def __init__(self): # model_name):
        self.version = (0, 4) # version 0.4
        self.valid_rate = 0.3
        #self.image_size = (160, 70, 3)
        self.num_outputs = 1  # steering_angle, throttle
        self.fname_ext = '.jpg'
        self.num_epochs = 20
        self.batch_size = 16
        #type of Model = (1)Jkwon-Shobhit,
        #                (2)Nvidia, 
        #                (3)Intermediate_ResNet,
        #                (4)LSTM-fc6,
        #                (5)LSTM-fc8,
        #                (6)SqueezeNet
        self.typeofModel = 3

        #self.raw_scale = 1.0 # Multiply raw input by this scale
        #self.jitter_tolerance = 0.009 # joystick jitter
        #self.capture_area = (0,380,800,800)
        #self.capture_size = (self.capture_area[3]-self.capture_area[1], 
        #                     self.capture_area[2]-self.capture_area[0], 3)

        self.capture_area = (0,370,800,620) #Intermediate_ResNet
        self.image_size = (400,200,3) #Intermediate_ResNet, SqueezeNet
