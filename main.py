import os
import time
import tensorflow as tf
from network import DilatedPixelCNN


def configure():
    # training
    flags = tf.app.flags
    flags.DEFINE_integer('max_epoch', 1, '# of step in an epoch')
    flags.DEFINE_integer('test_step', 100, '# of step to test a model')
    flags.DEFINE_integer('save_step', 1000, '# of step to save a model')
    flags.DEFINE_float('learning_rate', 1e-3, 'learning rate')
    # data
    flags.DEFINE_string('data_dir', './dataset', 'Name of data directory')
    flags.DEFINE_string('data_list', './dataset/train.txt', 'Training data list')
    flags.DEFINE_string('sample_dir', 'samples', 'Sample directory')
    flags.DEFINE_integer('batch', 2, 'batch size')
    flags.DEFINE_integer('channel', 3, 'channel size')
    flags.DEFINE_integer('height', 320, 'height size')
    flags.DEFINE_integer('width', 320, 'width size')
    # Debug
    flags.DEFINE_boolean('is_train', True, 'Training or testing')
    flags.DEFINE_string('log_level', 'INFO', 'Log level')
    flags.DEFINE_integer('random_seed', int(time.time()), 'random seed')
    # network
    flags.DEFINE_integer('network_depth', 5, 'network depth for U-Net')
    flags.DEFINE_integer('class_num', 21, 'output class number')
    flags.DEFINE_integer('start_channel_num', 64, 'start number of outputs')
    flags.DEFINE_boolean('use_gpu', False, 'use GPU or not')
    flags.FLAGS.__dict__['__parsed'] = False
    return flags.FLAGS


def main(_):
    conf = configure()
    sess = tf.Session()
    model = DilatedPixelCNN(sess, conf)
    model.train()
    writer = tf.summary.FileWriter('./my_graph', model.sess.graph)


if __name__ == '__main__':
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    tf.app.run()
