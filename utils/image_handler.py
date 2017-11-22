
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys

class_of_object = ['man', 'woman', 'boy', 'girl']
emotion = ['happy', 'sad', 'suspicious', 'attractive', 'unattractive', 'smart', 'thin', 'fat',
           'energy', 'lazy', 'tired']

obmap = {'man':0, 'woman':1, 'boy':2, 'girl':3}
emmap = {'happy':0, 'sad':1, 'suspicious':2, 'attractive':3, 'unattractive':4, 'smart':5, 'thin':6, 'fat':7,
           'energy':8, 'lazy':9, 'tired':10}

def resize_all_in_folder(dirpath):
    dirs = os.listdir(dirpath)
    for item in dirs:
        if os.path.isfile(dirpath+item):
            im = Image.open(dirpath+item)
            f, e = os.path.splitext(dirpath+item)
            imResize = im.resize((200,200), Image.ANTIALIAS)
            # imResize = img.thumbnail((64, 64), Image.ANTIALIAS)
            imResize.save(f + '_resized.jpg', 'JPEG', quality=90)


def resize_and_convert_image_to_array(path, newsize=(500,500)):
    im = Image.open(path)
    return plt.imshow(im.resize(newsize, Image.ANTIALIAS)).get_array()

def convert_image_to_array(filepath):
    return mpimg.imread(filepath)

def convert_array_to_image(arr):
    plt.imshow(arr)
    plt.show()

def load_datasets(img_dir):
    X, Yobj, Yemt = [], [], []
    dirs = os.listdir(img_dir)
    for subdir in dirs:
        abspath = os.path.abspath(img_dir+ '/' + subdir)
        if os.path.isdir(abspath):
            ob,emt = subdir.split('+')
            files = os.listdir(abspath)
            i = 1
            for filepath in files:
                try:
                    X.append(resize_and_convert_image_to_array(os.path.abspath(img_dir+'/'+subdir+'/'+filepath)))
                except IOError as e:
                    print "IO Error", e.message
                    continue
                y_obj = np.zeros(len(obmap))
                y_emt = np.zeros(len(emmap))
                y_obj[obmap[ob]] = 1.
                y_emt[emmap[emt]] = 1.
                Yobj.append(y_obj)
                Yemt.append(y_emt)
                progress(i, len(files), status='Processing images in folder: %s' % subdir)
                i += 1
            sys.stdout.write("\n")
            sys.stdout.flush()
    return X, Yobj, Yemt

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()  # As suggested by Rom Ruben (see: http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console/27871113#comment50529068_27871113)
