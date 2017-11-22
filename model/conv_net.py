
import tensorflow as tf
from tflearn import DNN, conv_2d, max_pool_2d, batch_normalization
from tflearn import input_data, dropout, fully_connected
from tflearn import local_response_normalization

def conv_net_model(input_shape, **kwargs):
    net = input_data(shape=input_shape)
    net = conv_2d(net, 32, 3, activation='relu', regularizer="L2") # filter_size=32, nb_filter=3
    net = max_pool_2d(net, 2)
    net = local_response_normalization(net)
    net = conv_2d(net, 64, 3, activation='relu', regularizer="L2")
    net = max_pool_2d(net, 2)
    net = local_response_normalization(net)
    net = fully_connected(net, 128, activation='tanh')
    net = dropout(net, 0.8)
    net = fully_connected(net, 256, activation='tanh')
    net = dropout(net, 0.8)
    net = fully_connected(net, 10, activation='softmax')
    return net

