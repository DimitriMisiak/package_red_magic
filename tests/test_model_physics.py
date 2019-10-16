#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:20:11 2019

@author: misiak
"""

import sys

sys.path.append('/home/misiak/projects/package_red_magic')

from red_magic import Model_pulse

import matplotlib.pyplot as plt
plt.close('all')



model = Model_pulse(model='1exp')
model.expo_plot('plot 1exp')

model = Model_pulse(model='2exp')
model.expo_plot('plot 2exp')
    
model = Model_pulse(model='3exp')
model.expo_plot('plot 3exp')

plt.show()
