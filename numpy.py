import numpy as np
# initialize arrays
a= np.array([1,2,3],dtype='int16')
print(a);
b=np.array([[1.0,2.0,3.0],[2.0,4.5,6.7]])
print(b);


#getting dimension ans shape
print(a.ndim)
print (b.ndim)
print(a.shape)
print(b.shape)


# Get type
print(a.dtype)

#get size
print(a.size)
#get itemsize
print(a.itemsize)
#total size
print(b.nbytes)
