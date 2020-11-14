import numpy as np
from scipy import signal
import math

filepath = 'C:/Users/qingh/Desktop/USC/mocap/refine3d_1.txt' ## change to your own root of file
cnt = 0
data = []
print(float('3'))

def moving_average(input, window_size): 
    output = np.zeros(input.shape)
    for i in range(input.shape[0]): 
        left =  i - math.floor(window_size/2)
        right = i + math.floor(window_size/2)
        if left>=0 and right<input.shape[0]:
            output[i] = np.average(input[left:right+1]) 
        else: 
            output[i] = input[i]

    return output 


if __name__=='__main__':
    with open(filepath, 'r') as file_read:
        line = file_read.readline()
        while line and cnt<273:
            row_data = line.split(',')
            row_out = []
            for single_data in row_data:
                row_out.append(float(single_data))
            data.append(row_out)
            line = file_read.readline()
            cnt += 1
    #data = np.asarray(data)
    data = np.moveaxis(data, 0, -1)
    print(data.shape)

    index = 0
    #print(data[0][:10])
    for row in data:
        row = signal.savgol_filter(row,5,2)
        #row = signal.medfilt(row,3)
        #row = signal.wiener(row)
        #row = moving_average(row,3)
        data[index] = row
        index = index + 1
    #print(data[0][:10])
    data = np.moveaxis(data, 0, -1)
    print(data.shape)

    file_write = open('C:/Users/qingh/Desktop/USC/mocap/out.txt','w')
    index = 0 
    for row in data:
        file_write.write(str(row[0]))
        for i in range(1,row.shape[0]):
            file_write.write(',' + str(row[i]))    
        file_write.write('\n')