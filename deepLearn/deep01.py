#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   deep01.py    
@Contact :   yudong.j@icloud.com


@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/24 下午3:58   yudong      1.0         None
'''
import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 加载数据集
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # 数据归一化
    x_train, x_test = x_train / 255.0, x_test / 255.0
    # 搭建神经网络
    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10, activation='softmax')
        ]
    )
    # 配置优化器,损失函数和准确率
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
                  metrics=['sparse_categorical_accuracy'])
    # 模型存储路径
    checkpoint_save_path = "./checkpoint/mnist.ckpt"

    # 读取模型
    if os.path.exists(checkpoint_save_path + '.index'):
        print('-------------load the model-----------------')
        model.load_weights(checkpoint_save_path)
    # 断点回调，只保存参数，只保存最优模型
    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_save_path, save_weights_only=True,
                                                     save_best_only=True)
    # 数据训练
    history = model.fit(x_train, y_train, batch_size=32, epochs=5, validation_data=(x_test, y_test),
                        validation_freq=1, callbacks=[cp_callback])
    # 显示神经网络模型
    model.summary()

    # 显示训练集和验证集的acc和loss曲线

    acc = history.history['sparse_categorical_accuracy']
    val_acc = history.history['val_sparse_categorical_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    plt.figure()
    plt.subplot(121)
    plt.plot(acc, label='Training Accuracy')
    plt.plot(val_acc, label='Validation Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.legend()

    plt.subplot(122)
    plt.plot(loss, label='Training Loss')
    plt.plot(val_loss, label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.legend()
    plt.show()