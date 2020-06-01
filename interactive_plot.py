import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


X = pd.read_csv("Linear_X_Train.csv").values
Y = pd.read_csv("Linear_Y_Train.csv").values

theta = np.load("ThetaList.npy")
# 100, 2 shape
T0  = theta[:,0]
T1 = theta[:,1]

plt.ion()##on the interactive mode of matplotlib using this command
              #start from 0 till 50 and everytime u will take a jump of 3
for i in range(0,50,3):
    y_ = T1[i]*X + T0
    #points
    plt.scatter(X,Y)
    # line 
    plt.plot(X,y_,'red')
    plt.draw()
    plt.pause(1)#pause the line for one second
    plt.clf()#destroy the graph