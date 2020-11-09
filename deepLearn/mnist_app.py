#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mnist_app.py    
@Contact :   yudong.j@icloud.com


@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/24 下午6:07   yudong      1.0         None
'''

import tensorflow as tf
import numpy as np
import os
from PIL import Image
import matplotlib.pyplot as plt

if __name__ == '__main__':
    model_save_path = "./checkpoint/mnist.ckpt"

    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10, activation='softmax')
        ]
    )
    model.load_weights(model_save_path)
    img_path = '/home/yudong/Downloads/Compressed/class4/MNIST_FC/img/'
    for ph in os.listdir(img_path):
        split = ph.split('.')
        img = Image.open(img_path + ph)
        img = img.resize((28, 28), Image.ANTIALIAS)
        img_arr = np.array(img.convert('L'))
        for i in range(28):
            for j in range(28):
                if img_arr[i][j] < 220:
                    img_arr[i][j] = 255
                else:
                    img_arr[i][j] = 0
        img_arr = img_arr / 255.0

        x_predict = img_arr[tf.newaxis, ...]
        result = model.predict(x_predict)
        pred = tf.argmax(result, axis=1)
        print('真实值:',split[0],'预测值',pred.numpy()[0])
