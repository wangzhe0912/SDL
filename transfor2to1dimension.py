#-*- coding: utf-8 -*-
"""
author: shidongli
time: 2016/10/27
description: transfor a matrix to a list.
"""
import numpy as np

def transfor2to1(matrix):
	return matrix.reshape(1,len(matrix)*len(matrix[0]))[0]

if __name__ == '__main__':
	def func1(i, j):
		return i * 9 + j + 1
	test_array = np.fromfunction(func1, (9,9))
	print test_array
	print transfor2to1(test_array)
