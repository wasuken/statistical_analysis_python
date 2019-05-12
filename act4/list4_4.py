import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

def seiki(x):
    y = (1 / np.sqrt(2*np.pi * i[0])) * np.exp(-(x - i[1]) ** 2 / (2 * i[0]))
    return y
