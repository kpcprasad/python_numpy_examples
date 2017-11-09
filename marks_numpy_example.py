
# coding: utf-8

# In[109]:

import numpy as np
file = open("F:/eda_dataset/python_numpy_transformations.txt")
header = file.readline()
#print(header)
data = file.readlines()

sname = []


for i in data:
    w = i.split(',')
    sname = [w[1]]
    print(sname)
    m1,m2,m3,m4,m5,m6,m7,m8,m9,m10 = int(w[2]), int(w[3]), int(w[4]), int(w[5]), int(w[6]), int(w[7]), int(w[8]),int(w[9]), int(w[10]),int(w[11])
    r1 = 1 if m1>=35 else 0
    r2 = 1 if m2>=35 else 0
    r3 = 1 if m3>=35 else 0
    r4 = 1 if m4>=50 else 0
    r5 = 1 if m5>=50 else 0
    r6 = 1 if m6>=50 else 0
    r7 = 1 if m7>=60 else 0
    r8 = 1 if m8>=60 else 0
    r9 = 1 if m9>=60 else 0
    r10= 1 if m10>=60 else 0
    
    g1 = r1+r2+r3
    g2 = r4+r5+r6
    g3 = r7+r8+r9+r10
    
    
    if (g1>=2 and g2>=2 and g3>=2 and g1+g2+g3>=7):
        print ("Pass")
    else: print("Fail")
    

