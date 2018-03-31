import numpy as np
import sys
import os
import tensorflow as tf

#################################################################################
# Keras configs.                                                                #
# Please refer to https://keras.io/backend .                                    #
#################################################################################

import keras
from keras import backend as K

#K.set_floatx('float32')
#String: 'float16', 'float32', or 'float64'.

#K.set_epsilon(1e-05)
#float. Sets the value of the fuzz factor used in numeric expressions.

#K.set_image_data_format('channels_first')
#data_format: string. 'channels_first' or 'channels_last'.

###################################################################
# Variables                                                       #
# When launching project or scripts from Visual Studio,           #
# input_dir and output_dir are passed as arguments automatically. #
# Users could set them from the project setting page.             #
###################################################################

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string("input_dir", "./data", "Input directory where training dataset and meta data are saved")
tf.app.flags.DEFINE_string("output_dir", "./output", "Output directory where output such as logs are saved.")
tf.app.flags.DEFINE_string("log_dir", "./log", "Model directory where final model files are saved.")

def main(_):
    # TODO: add your code here
    with tf.Session() as sess:
        welcome = sess.run(tf.constant("Hello, TensorFlow!"))
        print(welcome)
    exit(0)


if __name__ == "__main__":
    tf.app.run()
