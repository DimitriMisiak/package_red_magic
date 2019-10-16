#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 11:06:16 2018

Test for the function of the chi2 script of the omnitool package.

@author: misiak
"""

import sys

sys.path.append('/home/misiak/projects/package_red_magic')

import numpy as np
import matplotlib.pyplot as plt

from red_magic import Manual_fitting




plt.close('all')


x_data = np.arange(0, 1, 0.05)

funk = lambda p: [p[0] + p[1]*x_data,]

y_data = funk([0.1, 5])[0]


fig, ax = plt.subplots()

ax.plot(x_data, y_data, ls='none', marker='.')

p0 = [1,1]
line, = ax.plot(x_data, funk(p0)[0])


from red_magic import chi2_simple

chi2_aux = lambda p: chi2_simple(y_data, funk(p)[0], 1)

def chi2_print(x):
    chi2 = chi2_aux(x)
    fig.suptitle('$\chi^2 = $' + str(chi2))

manual_fitting = Manual_fitting([line, ], funk, p0, chi2_fun=chi2_aux, 
                                callback=chi2_print)

manual_fitting.bonus_button('Bonus', lambda event: print('Yay'))


plt.show()