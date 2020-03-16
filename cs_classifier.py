from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
from keras.preprocessing import image

import numpy as np
import os

# image size
img_width, img_height = 432,288
# train and test sample sizes
train_samples = 665
test_samples = 98
# set weights
epochs = 75
batch_size = 20
# Directories of train and test data
train_dir = 'XRayDawgz/Images/Train'
test_dir = 'XRayDawgz/Images/Test'
###############################################################################
# data image augmentation to create more variation of XRD patterns
train_data = ImageDataGenerator(rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
# only resize for test data
test_data = ImageDataGenerator(rescale=1. / 255)
# import train data consisting of 'binary' or  2 classifications (BCC or FCC) 
train_gen = train_data.flow_from_directory(train_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='binary')
# import test data consisting of 'binary' or  2 classifications (BCC or FCC) 
test_gen = test_data.flow_from_directory(test_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='binary')
###############################################################################
# build CNN model
model = Sequential()
# extract features by iterating across image
model.add(Conv2D(32, (3, 3), input_shape=(img_width, img_height, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), input_shape=(img_width, img_height, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), input_shape=(img_width, img_height, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(ZeroPadding2D((1,1)))
# convert 3D features to 1D feature vectors
model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))
# model summary
model.summary()
###############################################################################
# compile model
model.compile(loss='binary_crossentropy',
        optimizer='rmsprop',
        metrics=['accuracy'])
###############################################################################
# run the CNN model
model.fit_generator(train_gen,
        steps_per_epoch=train_samples // batch_size,
        epochs=epochs,
        validation_data=test_gen,
        validation_steps=test_samples // batch_size)

