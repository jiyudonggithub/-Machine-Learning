#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   img_demo.py    
@Contact :   yudong.j@icloud.com


@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/24 下午7:20   yudong      1.0         None
'''
from typing import Optional, Any

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

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
    img_path = '/home/yudong/Downloads/Compressed/class4/MNIST_FC/img/5.png'
    img = Image.open(img_path)
    img = img.resize((28, 28), Image.ANTIALIAS)
    img_arr = np.array(img.convert('L'))

    print(img_arr)
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
    print(result)
    print('预测值', pred.numpy()[0])
    plt.imshow(img_arr, cmap='gray')
    plt.show()
