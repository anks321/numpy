import numpy as np
#Mathematics
a=np.array([1,2,3,4])
a+=2
print(a)
b=np.array([1,2,3,4])
print(a+b)
print(np.sin(a))

#Linear Algebra
a=np.ones((2,3))
print(a)
b=np.full((3,2),2)
print(b)



print(np.matmul(a,b))
c=np.identity(5)
print(c)


print(np.linalg.det(c))


#Statisitics

stat=np.array([[1,2,3],[4,5,6]])

print(np.min(stat))
print(np.max(stat))
print(np.sum(stat))

#Reoganize array

before=np.array([[1,2,3,4],[5,6,7,8]])
print(before)


after = before.reshape((4,2))
print(after)


#Vertical stacks

v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
print(np.vstack((v1,v2,v2,v1)))