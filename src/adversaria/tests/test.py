from cv2 import cv2
import numpy as np
import sys, os
import matplotlib.pyplot as plt
import glob

lp_norm_bounded_perturbations = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
mean = 0
var = 10
sigma = var ** 0.5
img_path = './data/10-17-16.jpg'
img = cv2.imread(img_path)

# gaussian perturbation doesn't translate to generating any key
gauss = np.random.normal(0,1,img.size)
gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
img_gauss = cv2.add(img,gauss)
