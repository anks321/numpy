import numpy as np
#Accessing / Chnaging


a=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(a)


#getting specific element (r,c)
print(a[1,5])


#Getting a spcefic row

print(a[0,:])


#Getting a specefi column

print(a[:,3])



# Getting every other element of first row

print(a[0,1:6:2])

#Changing element
a[1,5]=14
a[:,3]=[1,2]
print(a)

#3d element
b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

print(b[:,:,0])