#! /usr/bin/py3

import numpy as np

## 创建一个ndarray对象
a = np.array([1,2,3]) # 1,2,3的一维数组
a = np.array((1,2,3)) # 1,2,3的一维数组
a = np.array(((1,2),(3,4))) # 1,2;3,4的二维数组
a = np.array([[1,2],[3,4]]) # 1,2;3,4的二维数组
a = np.array(((1,2),(3,4)),dtype=complex) # 指定数据类型为复数


a = np.arange(15)   #  0,1,...,14的一维数组
a = np.arange(2,10) #  2,3,...,9的一维数组
a = np.arange(2,15,3) # 2,5,8,11,14的一维数组


a = np.zeros((3,4)) # 初始化一个3*4的全为0.0的矩阵,默认为float64
a = np.zeros((3,4), dtype=np.int16) # 指定为int16
a = np.ones(...) # 生成全为1.0的矩阵,参数可以参照zeros(...)方法
a = np.empty(...) # 生成未经初始化的矩阵,参数可以参照zeros(...)方法


a = np.linspace(0,2,11) # 生成0~2之间均布的11个元素的一维数组


# ndarray对象的属性
ndarray.ndim  # 维度 int
ndarray.shape # 形状 tuple[int],如(2,3)表示2*3矩阵
ndarray.size  # 数据量,int,等于ndarray.shape元素的累乘
ndarray.dtype # 数据类型 numpy.dtype类型
ndarray.dtype.name # 具体类型的名称,str，如int64
ndarray.itemsize # 元素占的内存大小,如int64占8个字节
ndarray.data  # 原始数据,内存片段


## ndarray对象的方法
a = np.arange(15).reshape(3,5) # reshape方法重新调整矩阵形状







