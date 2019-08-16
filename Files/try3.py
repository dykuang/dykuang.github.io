# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 18:41:57 2019

@author: dykuang

A test for solving Laplace equation with NN

"""


from keras.layers import Layer, Dense, Input, concatenate, add, multiply
from keras.models import Model
from keras.optimizers import Adam

import numpy as np
import keras.backend as K


## data preparation


## set parameters
params = {
        'input dim': 2,
        'output dim': 1,
        'batchsize': 8,
        'epochs': 1000}


## Model preparation
class Get_gradient(Layer):
    '''
    Be careful about tf.gradients
    * unconnected_gradients='none' is default
    * aggrogate_method is add_n. Watch out if _out's second dimension > 1.
    '''

    def __init__(self, **kwargs):
        super(Get_gradient, self).__init__(**kwargs)

    def build(self, input_shape):
        assert isinstance(input_shape, list)

        super(Get_gradient, self).build(input_shape)  # Be sure to call this at the end

    def call(self, x):
        assert isinstance(x, list)
        _out, _in = x
        return K.gradients(_out, _in) # Be aware that unconnected_gradients='none' is the default, this operation is element-wise

    def compute_output_shape(self, input_shape):
        assert isinstance(input_shape, list)
        shape_out, shape_in = input_shape
        return shape_in

import tensorflow as tf
class sol_form(Layer):
    '''
    Construct the form of solution that satisfies the boundary/initial condtion
    something wrong with the output shape...
    '''
    def __init__(self, **kwargs):
        super(sol_form, self).__init__(**kwargs)
        
    def build(self, input_shape):
        assert isinstance(input_shape, list)
        super(sol_form, self).build(input_shape)
    
    def call(self, x):
        '''
        all variables are splited into size: (batch, 1)
        '''
        assert isinstance(x, list)
        X, nn = x
        X1 = X[:,:1]  # ! shape (1,) != shape (1,1) !
        X2 = X[:,1:2]
        
#        print(X1.shape)
        
        sol = tf.multiply(X2, tf.sin(3.1415926*X1)) + X1*(X1-1.)*X2*(X2-1.)*nn
        
#        print(sol.shape)
        
        return sol
    
    def compute_output_shape(self, input_shape):
        assert isinstance(input_shape, list)
        a, b = input_shape

        return b
    
    
def NN_solver(dim_in=2, dim_out=1, order = 2):
    '''
    dim_in: spatial dimension
    dim_out: value dimension
    order: order of diff-eq
    '''
    
    x_s = [Input(shape=(1, )) for _ in range(dim_in)] # spatial, use a list for better maniputlate higher order derivatives with tensorflow

    x_concat = concatenate(x_s)
#    print(x_concat.shape)
    
    x = Dense(16, activation='tanh')(x_concat)

    nn = Dense(dim_out, activation='linear')(x)  # same reason for better obtaining higher order derivatives
#    print(nn.shape)
    
    x_sol = sol_form()([x_concat, nn])
    
    u1 = Get_gradient()([x_sol, x_s[0]])
    u2 = Get_gradient()([x_sol, x_s[1]])
    
    u11 = Get_gradient()([u1, x_s[0]]) # (batchsize, 1)
    u22 = Get_gradient()([u2, x_s[1]]) # (batchsize, 1)
    
    
    eqn_res = add([u11, u22])
    
    model = Model(x_s, [x_sol, eqn_res]) # return x(t) and left-side value of diff-eq    

    model.compile(loss = ['mse', 'mse'], 
                  loss_weights = [0.0, 1.0], 
                  optimizer=Adam(lr=1e-3))    
    return model

Mymodel = NN_solver()

## Train with batches
def make_grid(x_span = np.linspace(0,1,10), y_span=np.linspace(0,1,10)):
    X , Y = np.meshgrid(x_span, y_span)
    grid = np.stack([X, Y], axis=-1)
    grid = np.reshape(grid, (-1, 2))
    
    return grid
    
def Get_batch(grid, batchsize):
    ind = np.random.choice(len(grid), batchsize, replace=False)
    pts_batch = grid[ind]
    x = pts_batch[:,0]
    y = pts_batch[:,1] 
        
    return [x, y]

def summarize_performance(model, step):
    filename = 'weights_at_step_{}_try3.h5'.format(step)
    model.save_weights(filename)
    print("Weights saved at step {}.".format(step))
    
## Train with fit_generator
def generator(grid, batchsize):
    '''
    randoml sample [x, t] domain. [0, 5] * [0, 6]
    '''
    x = np.zeros((batchsize, 1))
    y = np.zeros((batchsize, 1))
    Ze = np.zeros_like(x)
    
    while True:
        ind = np.random.choice(len(grid), batchsize, replace=False)
#        pts_batch = grid[ind]
        x = grid[ind,0]
        y = grid[ind,1]
               
        yield [x, y], [Ze, Ze]

Grid = make_grid()

#Mygen = generator(Grid, params['batchsize'])
#hist = Mymodel.fit_generator(Mygen,steps_per_epoch=len(Grid)//params['batchsize'], 
#                             epochs=params['epochs'], 
#                             verbose=1, callbacks=None, shuffle=True)

Ze = np.zeros((len(Grid),1))
hist = Mymodel.fit(x=[Grid[:,0], Grid[:,1]], y = [Ze, Ze], batch_size=params['batchsize'], epochs=params['epochs'], verbose=0)


## Custom training with train_on_batch  (slow + large memory, do not know why?)
# =============================================================================
# def train(model, num_steps, batchsize, check_point=100):
#     summary_eqn=[]
# #    summary_res=[]
#     Grid = make_grid()
#     Ydata = [np.zeros((batchsize, 1)), np.zeros((batchsize, 1))]
#     for step in range(num_steps): # put Get_batch as a generator here?
#         print("on step {} ===========>".format(step))
#         Xdata = Get_batch(Grid, batchsize)
#         loss =  model.train_on_batch(Xdata, Ydata)     
#         summary_eqn.append(loss[0]) # train with eqn-loss
#                
#         if (step +1) % check_point == 0:
#             print("step {}: Total loss: {};".format(step, summary_eqn[step]))
#             summarize_performance(model, step)
#             
#     return summary_eqn    
#     
# summary = train(Mymodel, num_steps = 500, batchsize=params['batchsize'], check_point=500) # may need more iterations
# =============================================================================

## Visualization
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def plot_sol_scatter(model,x_span = np.linspace(0,1,10), y_span = np.linspace(0,1,10)):
    grid = make_grid(x_span, y_span)
    U,_ = model.predict([grid[:,0], grid[:,1]])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(grid[:,0], grid[:,1], U, c='r', marker='o')
    

def plot_sol_surface(model,x_span = np.linspace(0,1,10), y_span = np.linspace(0,1,10)):
    grid = make_grid(x_span, y_span)
    U,err = model.predict([grid[:,0], grid[:,1]])
    XX, YY = np.meshgrid(x_span, y_span)
    U = U.reshape((len(x_span), len(y_span)))
    err = err.reshape((len(x_span), len(y_span)))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(XX, YY, U, cmap=cm.coolwarm)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(XX, YY, err, cmap=cm.coolwarm)    

