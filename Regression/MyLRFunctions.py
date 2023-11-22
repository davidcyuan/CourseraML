import numpy as np
import matplotlib.pyplot as plt
import math

def print_scatter(X_train, y_train, feature_names, y_predict):
    feature_num = len(feature_names)
    cols = 4
    rows = math.ceil(feature_num / cols)
    fig,ax = plt.subplots(rows, cols, figsize = (12,5), sharey = True)
    for i in range(feature_num):
        row = math.floor(i/cols)
        col = i%cols
        ax[row][col].scatter(X_train[:,i], y_train, label = "target")
        ax[row][col].set_xlabel(feature_names[i])
    
        ax[row][col].scatter(X_train[:,i], y_predict, label = "prediction")
                      
    ax[0][0].set_ylabel("Value")
    ax[0][0].legend()
    fig.suptitle('Target vs Prediction')
    plt.show()