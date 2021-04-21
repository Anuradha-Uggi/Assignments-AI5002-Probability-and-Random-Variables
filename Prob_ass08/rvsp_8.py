# -*- coding: utf-8 -*-
"""rvsp_8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XDqkj23EYZzX9r9SRxcSEP8DAXFkNBEb
"""

import numpy as np
import math


## function for probability p(y=0)
def prob_y_0(p_y0_x0,p_y0_x1,p_x0,p_x1):
     p_y0=p_y0_x0*p_x0+p_y0_x1*p_x1;
     return p_y0

## function for probability p(x=1/y=0)
def prob_x1_y0(p_y0_x1,p_x1,x):
     p_x1_y0=p_y0_x1*p_x1/x ;
     return p_x1_y0
     
## given cross over probability
p_c=1/7;
## given non-cross over probability
p_nc=6/7;
## input probabilities
p_x0=0.2;
p_x1=0.8;

## computation
p_x1_y=prob_x1_y0(p_c,p_x1,prob_y_0(p_nc,p_c,p_x0,p_x1))
print('probability that X=1 is transmitted given y=0 is recieved is:',p_x1_y)