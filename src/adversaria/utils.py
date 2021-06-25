import random
import time
import numpy as np
from random import gauss
from random import seed
import cv2
import tensorflow as tf
from tensorflow import keras
import torch
# import torchsprng

# image frames to perturb
dir = "./frames"

def generate_secure_pseudorandom_key():
    key = []
    return key

def generate_gaussian_distribution(norm_type, norm_value):
    # generate a unique pseudorandom key based on the norm-bounded perturbations. The larger the epsilon norm-value, the more unique the key that is generated. We will perturb the image on a unique distribution and translate the pattern into a key string, then store the key string with the image frame, e.g. store a JSON file with the frames and the respective partial keys
    return []

def create_image_mask(image : np.ndarray):
    # precondition: norm-bounded gaussian distribution applied
    # creating imperceptible adversarial perturbation to the image, return the original image and the perturbed image in order to reference the original for any reason
    # generate unique seed value and do this: dot_product(image) * seed_value * pseudorandom_generated_key_value
    return image, {}

def generate_seed_value():
    # use a seed value with a base transformation layer (constant applied perturbation norm) to generate unique perturbation_keys. Store the seed values along with the perturbation key in order to transform and de-transform the image.
    seed_value = np.random.seed(seed=None)
    max = 1000
    min = 1
    max = seed_value * (max-min) + min
    seed_multiplier = torch.manual_seed(seed_value)
    for min in range(max):
        seed_value * seed_multiplier 
    
    return seed_value 


def detransform(image):
    # precondition: we have image and its metadata that links the user and the source (transformed) content
    image = tf.cast(image, tf.float32)

