import numpy as np
#Initialize Different types of arrays
a=np.zeros((2,3,3,3))
print(a)

a=np.ones((2,3))
print(a)
a=np.full((2,3),99)
print(a)

#Random numbers

c=np.random.rand(4,2)
print(c)


d= np.random.randint(7,size=(3,3))
print(d)

e=np.identity(4)
print(e)

f =np.array([[1,2,3]])
r1=np.repeat(f,3,axis=0)
print(r1)


# Problem
q =np.ones((5,5))
z=np.zeros((3,3))
z[1,1]=9;
q[1:4,1:4]=z
print(q)
#careful while copying

a=np.array([1,2,3])
b=a.copy()
b[0]=100
print(b)
print(a)