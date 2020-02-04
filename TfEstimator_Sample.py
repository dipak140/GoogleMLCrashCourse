# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:31:31 2020

@author: DIPAK
Description : TensorFlow Estimator sample code

"""

import tensorflow as tf

classifier = tf.estimator.LinearClassifier(feature_column)
classifier.train(input_fn = train_input_fn ,  steps = 2000)
predictions = classifier.predict(input_fn = predict_input_fn)

