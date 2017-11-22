
from tflearn import regression, DNN

def neural_net_trainer(net, learning_rate=0.001, best_checkpoint_path='model_best'):
    net = regression(net, optimizer='adam', learning_rate= learning_rate, loss='categorical_crossentropy', shuffle_batches=True)
    return DNN(network=net, clip_gradients=0., tensorboard_verbose=3, best_checkpoint_path=best_checkpoint_path, best_val_accuracy=0.999)

def train(model, X, Y, overall_iters=60, num_epochs=20, save_path='model.tfl'):
    for overalliter in xrange(overall_iters):
        model.fit(X, Y, validation_set=0.1, show_metric=True, batch_size=None, shuffle = True, n_epoch=num_epochs) # 100% of data being used for validation
        model.save(save_path)