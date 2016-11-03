"""
author: shidongli
time: 2016/10/28
description: split a 240*240 flair picture to a group of n*n pictures by a sliding window. x*(N*N)
where n is the size of window which can be used to predict.
"""

import numpy as np
from scipy.io import matlab as mio
from transfor2to1dimension import transfor2to1




def split_by_sliding_window(array_picture, length):
    length = int(length)
    array_picture = array_picture*255.0/np.max(array_picture)
    size = 240
    result_arrays = []
    for x in range(length, size-length):
        for y in range(length, size-length):
            result_arrays.append(array_picture[x-length:x+length,y-length:y+length])
    return result_arrays


def first_step(original_picture, length, route):
    n = int(length) * 2 + 1
    
    picture = mio.loadmat(original_picture)['ab']
    processed_pictures = split_by_sliding_window(picture, length)
    result = []
    for processed_picture in processed_pictures:
        result.append(transfor2to1(processed_picture))
    mio.savemat(route, {'data': result})


if __name__== '__main__':
    #picture = sio.loadmat(u'C:/Users/wangz/Desktop/Git/sdl/prepared/test/flair53.mat')['aa']
    picture = mio.loadmat(u'./picture/1flair61.mat')['ab']
    processed_pictures = split_by_sliding_window(picture, 25)
    result = []
    for processed_picture in processed_pictures:
        result.append(transfor2to1(processed_picture))
    #sio.savemat(u'C:/Users/wangz/Desktop/Git/sdl/prepared/test/pictures53.mat', {'data': result})
    print len(result)
    print len(result[0])
    mio.savemat(u'./picture/multi1flair61.mat', {'data': result})

    # import sys
    # first_step(sys.argv[1], sys.argv[2], sys.argv[3])

