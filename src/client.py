import random
import time
import numpy as np
from random import gauss
from random import seed
import cv2
import tensorflow as tf
from tensorflow import keras
import torch

def create_clients():
    # let's manually tag images with their target labels as an example
    # setup n clients/users and generate psuedo-random perturbation-based key to track the id tied to the user,s o there's unique content ids generated to help facilitate its tracking
    perturbation_key = []
    transformed_user_image = []
    user_id = []
    return perturbation_key, user_id, transformed_user_image