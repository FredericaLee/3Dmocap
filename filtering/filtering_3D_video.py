import numpy as np
from scipy import signal
import math
from filtering import moving_average
from scipy import signal
import math


filepath = 'C:/Users/qingh/Desktop/USC/mocap/3Dvideo.npy'
data = np.load(filepath)
print(data)
data = np.moveaxis(data, 0, -1)
print(data.shape)
output = np.zeros(((data.shape)))
for i in range(data.shape[0]):
    for j in range(data.shape[1]): 
        cur = data[i][j]
        #cur = signal.savgol_filter(cur,5,2)
        #cur = signal.medfilt(cur,3)
        #cur = signal.wiener(cur)
        cur = moving_average(cur,3)
        output[i][j] = cur
output = np.moveaxis(data,2,0)

with open('test.npy', 'wb') as f:
    np.save(f, output)

'''
with open('test.npy', 'rb') as f:
    a = np.load(f)
print(a.shape)
'''