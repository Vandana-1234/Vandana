import numpy as np
a=np.array(input("enter array"))
b=np.array(input("enter array"))
c=a+b
print"addition of two numbers",c
d=a-b
print"subtraction of two numbers",d
e=a/b
print"division of two numbers",e
f=a*b
print"multiplication of two numbers",f
g=np.max(a)
print"maximum of two numbers",g
h=np.min(a)
print"minimum of two numbers",h
i=np.linalg.eig(a)
print"eigen values of two numbers",i
j=np.zeros((2,2))
print"zero matrix",j
k=np.ones((1,2))
print"ones matrix",k
l=np.eye(3)
print"identity matrix",l
m=np.linalg.det(a)
print"determinant of matrix",m
n=a.transpose()
print"transpose of matrix",n
