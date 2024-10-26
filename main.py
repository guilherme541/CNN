import cv2
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.neural_network import MLPClassifier #DataSET
from sklearn.model_selection import train_test_split #DataSET
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits
import numpy as np