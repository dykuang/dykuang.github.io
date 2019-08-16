# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 10:42:13 2019

@author: dykuang

A test for solving simple ODE with neural network

"""
from keras.layers import Layer, Dense, Input, concatenate, add, multiply
from keras.models import Model
from keras.optimizers import Adam

import numpy as np
import keras.backend as K


## data preparation


## set parameters
params = {
        'dim': 1,
        'batchsize': 25,
        'epochs': 1000}



f = lambda x,t: x*np.exp(-t) 
## Model preparation
class Get_gradient(Layer):

    def __init__(self, **kwargs):
        super(Get_gradient, self).__init__(**kwargs)

    def build(self, input_shape):
        assert isinstance(input_shape, list)
        # Create a trainable weight variable for this layer.
#        self.kernel = self.add_weight(name='kernel', 
#                                      shape=(input_shape[1], self.output_dim),
#                                      initializer='uniform',
#                                      trainable=True)
        super(Get_gradient, self).build(input_shape)  # Be sure to call this at the end

    def call(self, x):
        assert isinstance(x, list)
        _out, _in = x
        return K.gradients(_out, _in)

    def compute_output_shape(self, input_shape):
        assert isinstance(input_shape, list)
        shape_out, shape_in = input_shape
        return (shape_out[0], shape_in[1])

def NN_solver(dim):
    
    x_s = Input(shape=(dim, )) # spatial
#    
    x_t = Input(shape=(1,)) # time
    x = Dense(16, activation='tanh')(x_t)
#    x = Dense(dim)(x)
#    x = concatenate([x_s, x])
    
#    x = Dense(16)(x)
#    x = Dense(16)(x)
    nn = Dense(dim, activation='linear')(x)
    
    dndt = Get_gradient()([nn, x_t])
    x_sol = add([x_s, multiply([x_t, nn])]) # could be wrapped as a custom layer for more complexed structure
    
    eqn_res = add([x_sol, nn, multiply([x_t, dndt])])
#    eqn_res = add([x_sol, eqn])

    
    model = Model([x_s, x_t], [nn, eqn_res]) # return x(t) and left-side value of diff-eq    
    
    return model

def NN_solver_2(dim):
    
    x_s = Input(shape=(dim, )) # spatial
#    
    x_t = Input(shape=(1,)) # time
    x = Dense(16, activation='tanh')(x_t)
#    x = Dense(dim)(x)
#    x = concatenate([x_s, x])
    
#    x = Dense(16)(x)
#    x = Dense(16)(x)
    nn = Dense(dim, activation='linear')(x)
    
    x_sol = add([x_s, multiply([x_t, nn])]) # could be wrapped as a custom layer for more complexed structure
    
    dxdt = Get_gradient()([x_sol, x_t])
    eqn_res = add([dxdt, x_sol])
    
    model = Model([x_s, x_t], [x_sol, eqn_res]) # return x(t) and left-side value of diff-eq    
    
    model.compile(loss = ['mse', 'mse'], 
                  loss_weights = [0.0, 1.0], 
                  optimizer=Adam(lr=1e-3))
    return model

Mymodel = NN_solver_2(params['dim'])

## Train with fit_generator
# =============================================================================
# def generator(batchsize):
#     '''
#     randoml sample [x, t] domain. [0, 5] * [0, 6]
#     '''
#     half_batch = int(batchsize/2)
#     zeros = np.zeros((half_batch, 1))
# 
#     while True:
#         x = np.random.uniform(0, 5, size=(batchsize, 1))
#         t = np.random.uniform(0.05, 6, size=(half_batch, 1))
#         t = np.vstack([t, zeros])
# #        xt = np.hstack([x,t])
#         
#         yield [x, t], [np.zeros_like(x), np.zeros_like(x)]
# 
# Mygen = generator(params['batchsize'])
# hist = Mymodel.fit_generator(Mygen,steps_per_epoch=10, epochs=params['epochs'], 
#                              verbose=1, callbacks=None, shuffle=True)
# =============================================================================
def make_grid(x_ini = 1., tspan = np.linspace(0, 6, 100)):
    x = x_ini*np.ones_like(tspan)
    
    return [x, tspan]

grid = make_grid()
Ze = [np.zeros((grid[0].shape[0], 1)), np.zeros((grid[0].shape[0],1))]
    
hist = Mymodel.fit(grid, Ze, batch_size=params['batchsize'], epochs=params['epochs'], verbose=0)

## Train with batches
def Get_batch(batchsize):
    x = np.random.uniform(1, 1, size=(batchsize, 1))
    t = np.linspace(0,2,batchsize)
        
    return [x, t], [np.zeros_like(x), np.zeros_like(x)]

def summarize_performance(model, step):
    filename = 'weights_at_step_{}.h5'.format(step)
    model.save_weights(filename)
    print("Weights saved at step {}.".format(step))

# =============================================================================
# def train(model, num_steps, batchsize, check_point=100):
#     summary_eqn=[]
# #    summary_res=[]
#     
#     Xdata, Ydata = Get_batch(batchsize)
#     for step in range(num_steps+1):
#         print("on step {} ===========>".format(step))
# #        Xdata, Ydata = Get_batch(batchsize, t_is_0 = False)
# 
#         summary_eqn.append(model.train_on_batch(Xdata, Ydata)[0]) # train with eqn-loss
#                
#         if (step + 1) % check_point == 0:
#             print("step {}: loss: {}; ".format(step, summary_eqn[step]))
#             summarize_performance(model, step)
#             
#     return summary_eqn    
#     
# summary = train(Mymodel, num_steps = 500, batchsize=params['batchsize'], check_point=100) # may need more iterations
# =============================================================================

## Visualization
import matplotlib.pyplot as plt
def plot_sol(model, num_ini=9, tspan=np.linspace(0, 6, 100)):
    x_ini = np.random.uniform(1.,1., size=(num_ini, ))
    dataX = np.zeros((num_ini*len(tspan),2))
    for i in range(num_ini):
        dataX[i*len(tspan):(i+1)*len(tspan), 0] = x_ini[i]*np.ones(len(tspan))
        dataX[i*len(tspan):(i+1)*len(tspan), 1] = tspan
    
    sol, eqn_err = model.predict([dataX[:,0], dataX[:,1]]) # be aware that predX = xsol - x0
    
#    pred_sol = res[:,0]*tspan + dataX[:,0] 
    plt.figure()
    side_num = int(num_ini**0.5)
    for i in range(num_ini):
        plt.subplot(side_num, side_num, i+1)
        pred_sol = sol[i*len(tspan):(i+1)*len(tspan),0]
        plt.plot(tspan, pred_sol)
        plt.plot(tspan, np.array([f(x_ini[i], t) for t in tspan]), '*')        
    
plot_sol(Mymodel)


def plot_sol_single(model, x_ini = 1.0, tspan = np.linspace(0,6,100)):
    Xdata = make_grid(x_ini, tspan)
    sol, eqn_err = model.predict(Xdata)
    plt.figure()
    plt.plot(tspan, sol)
    plt.figure()
    plt.plot(tspan, eqn_err)
plot_sol_single(Mymodel)   

