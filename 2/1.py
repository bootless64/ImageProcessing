import numpy as np
from numpy import array

print ("matrix Spiliting")
matrix=array([[12,3,3,2],
             [6,3,8,9],
             [9,0,9,0]]
)
print (matrix)
sub=matrix[0:2,1:3]
print (sub)
sub=matrix[::2,::3]
print (sub)
sub=matrix[::-1,1:4:]
print (sub)
sub=matrix[::-1,::-1]
print (sub)
sub=matrix[::2,::2]
print (sub)

print ("------------------------")
print ("Concatenation")

a = np.arange(1, 13).reshape((4, 3))
print(a)

print("****")

x = np.array([4, 6,8])
y = np.array([9, 8,4])
q=np.concatenate([x, y,x])
print (q)

print("****")

print (np.vstack([x,y]))

print("****")

print(np.vstack([x, a]))

print ("------------------------")
print ("Spilitig")


q1,q2,q3,q4=np.split(q,[3,5,7])
print (q1,q2,q3,q4)

print("****")

upper, lower = np.vsplit(a, [3])

print("upper:")
print(upper)

print("lower:")
print(lower)

print("****")

left, right = np.hsplit(a, [1])

print("left:")
print(left)

print("right:")
print(right)