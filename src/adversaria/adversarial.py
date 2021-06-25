import random
import time
import numpy as np
from random import gauss
from random import seed
import os, sys
import fnmatch, re
import cv2
import tensorflow as tf
from tensorflow import keras
from utils import *

DIR = "./frames"
image_label = 'portal'

image_set = []
label_set = []

# populate image/label_set with frames
total_frames = fnmatch.filter(os.listdir(DIR), '*.jpg')
total_frames = len(total_frames)

for i in range(total_frames):
    filename = "frame" + i + ".jpg"
    filepath = DIR + filename
    image_set[i] = cv2.imread()
    label_set[i] = image_label # constant

class FrameData():
    def __init__(self, image):
        self.image = image

    def __getitem__(self):
        img_tensor =  []
        return img_tensor

class FrameDataset():
    def __init__(self, image_set, label_set):
        self.image_set = image_set
        self.label_set = label_set
        self.adversarial_image_ids = []
        self.server_perturbation_keys = []
        self.client_perturbation_keys = []
        self.seed_values = []

image = cv2.imread(image_set[0])
image_shape = image.shape
print(image_shape)
data = FrameData(image)
seed = generate_seed_value()
