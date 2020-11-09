# -*- coding: utf-8 -*-
# @Time : 2020/9/4 21:15
# @Author : Jiyudong
# @FileName: Demo.py
# @Software: PyCharm

# dir = {'爱情片': 6, '动作片': 3, '喜剧片': 10, '恐怖片': 9}
# dir1 = sorted(dir.items(),key=lambda x:x[1],reverse=True)
# print(dir1)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import tensorflow as tf

if __name__ == "__main__":

    print('GPU', tf.test.is_gpu_available())

    a = tf.constant(2.)
    b = tf.constant(4.)
    
    print(a * b)
