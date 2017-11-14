# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:11:46 2017

@author: kpcprasad
"""

import numpy as np
import math

a = [1,2,3,4,5,6]
b = [9,8,7,6,5,4]

def correlation(x,y):
    # Creating numpy arrays and required constants
    npA = np.array(x)
    npB = np.array(y)
    n = len(x)
    # Applying formula 
    numerator = n * (sum(npA * npB)) - (sum(npA) * sum(npB))
    denominator = math.sqrt((   n * sum(npA**2) - (sum(npA))**2   ) * (   n * sum(npB**2) - (sum(npB))**2) )
    
    #return numerator
    return numerator / denominator

value = correlation(a,b)
print(value)