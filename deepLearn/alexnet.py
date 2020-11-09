#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   alexnet.py    
@Contact :   yudong.j@icloud.com


@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/26 上午8:56   yudong      1.0         None
'''
import tensorflow as tf
import numpy as np
from tensorflow.keras import Model
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.datasets.cifar import load_batch
from tensorflow.keras.layers import Dense, Conv2D, BatchNormalization, Activation, MaxPool2D, Dropout, Flatten
import os
import matplotlib.pyplot as plt


class alexnet(Model):

    def __init__(self, *args, **kwargs):
        super(alexnet, self).__init__()
        self.c1 = Conv2D(filters=96, kernel_size=(3, 3), strides=1, padding='valid')
        self.b1 = BatchNormalization()
        self.a1 = Activation('relu')
        self.p1 = MaxPool2D(pool_size=(3, 3), strides=2, padding='valid')

        self.c2 = Conv2D(filters=256, kernel_size=(3, 3), strides=1, padding='valid')
        self.b2 = BatchNormalization()
        self.a2 = Activation('relu')
        self.p2 = MaxPool2D(pool_size=(3, 3), strides=2, padding='valid')

        self.c3 = Conv2D(filters=384, kernel_size=(3, 3), strides=1, padding='same')
        self.a3 = Activation('relu')

        self.c4 = Conv2D(filters=384, kernel_size=(3, 3), strides=1, padding='same')
        self.a4 = Activation('relu')

        self.c5 = Conv2D(filters=256, kernel_size=(3, 3), strides=1, padding='same')
        self.a5 = Activation('relu')
        self.p3 = MaxPool2D(pool_size=(3, 3), strides=2, padding='valid')

        self.flatten = Flatten()
        self.f1 = Dense(2048, activation='relu')
        self.d1 = Dropout(0.5)
        self.f2 = Dense(2048, activation='relu')
        self.d2 = Dropout(0.5)
        self.f3 = Dense(10, activation='softmax')

    def call(self, inputs, training=None, mask=None):
        x = self.c1(inputs)
        x = self.b1(x)
        x = self.a1(x)
        x = self.p1(x)

        x = self.c2(x)
        x = self.b2(x)
        x = self.a2(x)
        x = self.p2(x)

        x = self.c3(x)
        x = self.a3(x)

        x = self.c4(x)
        x = self.a4(x)

        x = self.c5(x)
        x = self.a5(x)
        x = self.p3(x)

        x = self.flatten(x)

        x = self.f1(x)
        x = self.d1(x)
        x = self.f2(x)
        x = self.d2(x)
        y = self.f3(x)

        return y


def load_data(path):
    num_train_samples = 50000

    x_train = np.empty((num_train_samples, 3, 32, 32), dtype='uint8')
    y_train = np.empty((num_train_samples,), dtype='uint8')

    for i in range(1, 6):
        fpath = os.path.join(path, 'data_batch_' + str(i))
        (x_train[(i - 1) * 10000:i * 10000, :, :, :],
         y_train[(i - 1) * 10000:i * 10000]) = load_batch(fpath)

    fpath = os.path.join(path, 'test_batch')
    x_test, y_test = load_batch(fpath)

    y_train = np.reshape(y_train, (len(y_train), 1))
    y_test = np.reshape(y_test, (len(y_test), 1))

    if K.image_data_format() == 'channels_last':
        x_train = x_train.transpose(0, 2, 3, 1)
        x_test = x_test.transpose(0, 2, 3, 1)

    x_test = x_test.astype(x_train.dtype)
    y_test = y_test.astype(y_train.dtype)

    return (x_train, y_train), (x_test, y_test)


if __name__ == '__main__':
    np.set_printoptions(threshold=np.inf)

    dirname = 'cifar-10-batches-py'
    (x_train, y_train), (x_test, y_test) = load_data(dirname)
    x_train, x_test = x_train / 255.0, x_test / 255.0
    model = alexnet()
    # 配置优化器,损失函数和准确率
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
                  metrics=['sparse_categorical_accuracy'])
    checkpoint_save_path = "./checkpoint/alexnetmodel.ckpt"

    # 读取模型
    if os.path.exists(checkpoint_save_path + '.index'):
        print('-------------load the model-----------------')
        model.load_weights(checkpoint_save_path)
    # 断点回调，只保存参数，只保存最优模型
    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_save_path,
                                                     save_weights_only=True,
                                                     save_best_only=True)
    # 数据训练
    history = model.fit(x_train, y_train, batch_size=32, epochs=5, validation_data=(x_test, y_test),
                        validation_freq=1, callbacks=[cp_callback])
    # 将参数储存
    with open('./weights.txt', 'w') as file:
        for v in model.trainable_variables:
            file.write(str(v.name) + '\n')
            file.write(str(v.shape) + '\n')
            file.write(str(v.numpy()) + '\n')
    # 显示训练集和验证集的acc和loss曲线
    acc = history.history['sparse_categorical_accuracy']
    val_acc = history.history['val_sparse_categorical_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.plot(acc, label='Training Accuracy')
    plt.plot(val_acc, label='Validation Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(loss, label='Training Loss')
    plt.plot(val_loss, label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.legend()
    plt.show()
