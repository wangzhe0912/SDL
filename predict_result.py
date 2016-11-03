"""
author: shidongli
time: 2016/10/28
description: process the output result and get the result picture.
"""
import scipy.io as sio
import numpy as np
import Image

results = sio.loadmat(u'G:/test/output74.mat')['output'][0]
zero_one_picture = []


for result in results:
    if result < 0.5:
        zero_one_picture.append(255)
    else:
        zero_one_picture.append(0)


result_picture_inner = np.array(zero_one_picture).reshape(212,212)

result_picture = np.zeros((240,240))

result_picture[14:226,14:226] = result_picture_inner

sio.savemat(u'G:/test/result74.mat', {'data': result_picture})

print np.sum(result_picture)/255

image = Image.fromarray(result_picture.astype(np.uint8))




image.save('image53.jpg')
