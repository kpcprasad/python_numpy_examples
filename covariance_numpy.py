# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:02:38 2017

@author: kpcprasad

AIM : Program to find covariance of given two Lists

FORMULA : Covariance(x,y) =             n*∑xy - ∑x*∑y
                            ------------------------------------
                            √[ n∑x^2 - (∑x)^2] [n∑y^2 - (∑y)^2 ]
"""
import numpy as np

a = [1,2,3,4,5,6]
b = [9,8,7,6,5,4]

def covariance(x,y):
    # Creating numpy arrays
    npA = np.array(x)
    npB = np.array(y)
    
    # Defining means of arrays in single line
    meanA, meanB = np.mean(npA), np.mean(npB)
    
    # Applying formula
    numerator = sum((npA - meanA) * (npB - meanB))
    denominator = len(x) - 1
    
    return numerator / denominator

value = covariance(a,b)
print(value)
