#Data input output from file
import numpy as np
filedata = np.genfromtxt('data',delimiter=",")
filedata =filedata.astype('int32')
print(filedata)


#advanced indexing and boolean masking
print(filedata[filedata>50])

print(np.any(filedata>50,axis=1))


print(filedata>50)