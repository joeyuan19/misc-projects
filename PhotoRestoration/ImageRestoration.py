#!/bin/sh

#  ImageRestoration.py
#  
#
#  Created by Joe Yuan on 11/27/12.
#


from PIL import Image as I
from PIL import ImageChops as IC
import numpy as np
import sys, os


f = open("DSC03123.jpg",'r')
data = []
for i in f:
    data.append(i)

print len(data)
