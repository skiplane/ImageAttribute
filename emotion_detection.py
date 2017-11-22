
from model.conv_net import conv_net_model
from model.trainer import neural_net_trainer, train
from utils.image_handler import load_datasets

kwargs = { }

X, Yobj, Yemt = load_datasets(img_dir='Images')

# Object labeller - man, woman or child
net_obj = conv_net_model(input_shape= X[0].shape)
model_obj = neural_net_trainer(net_obj, best_checkpoint_path='best_obj_model')
train(model_obj, X, Yobj, save_path='obj_model.tfl')

# Emotion labeller - happy, sad etc
net_emt = conv_net_model(input_shape= X.shape)
model_emt = neural_net_trainer(net_emt, best_checkpoint_path='best_emotion_model')
train(model_emt, X, Yemt, save_path='emt_model.tfl')
