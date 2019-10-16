#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:20:11 2019

@author: misiak
"""

import sys

sys.path.append('/home/misiak/projects/package_red_magic')

import red_magic as rmc

import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

# Fixing random state for reproducibility
np.random.seed(19680801)

data = np.random.rand(100, 2)

subplot_kw = dict(xlim=(0, 1), ylim=(0, 1), autoscale_on=False)
fig, ax = plt.subplots(subplot_kw=subplot_kw)

pts, = ax.plot(data[:, 0], data[:, 1], ls='none', marker='+')
selector = rmc.Data_Selector(ax, pts, proceed_func=lambda x: print('hello'))

plt.show()
