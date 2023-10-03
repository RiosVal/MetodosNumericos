import numpy as np

iter = 5
p = 2
tol = 0.001

f1 = lambda x,y,z: (4-y-2*z)/3
f2 = lambda x,y,z: (6-2*x-z)/1
f3 = lambda x,y,z: (2-x-4*y)/6

x0 = 0
y0 = 0
z0 = 0

def forma1():
    for i in range(iter):
        x = f1(x0, y0, z0)
        y = f2(x0, y0, z0)
        z = f3(x0, y0, z0)
        error = np.sqrt(((x-x0)**p + (y-y0)**p + (z-z0)**p))
        if error < tol:
            break
        else:
            x0 = x; y0 = y; z0 = z
    vector = [x,y,z]
    return vector

def forma2():
    v0 = np.array([x0,y0,z0])
    for i in range(iter):

        x1 = f1(x0,y0,z0)
        y1 = f1(x0,y0,z0)
        z1 = f1(x0,y0,z0)

        v1 = np.array([x1,y1,z1])
        error = np.linalg.norm(v1-v0, ord=p)/np.linalg.norm(v1, ord=p)

        if error < tol:
            break
        else:
            x0=x1; y0=y1; z0=z1
    print(v1)

A=np.array([
    [3,1,2],
    [2,1,1],
    [1,4,6]
])
b=np.array([4,6,2])

D = np.diag(np.diag(A))
L = np.tril(A)-D
U = np.triu(A)-D

T = -np.dot(np.linalg.inv(D), (L+U))
c = np.dot(np.linalg.inv(D), b)

V0 = np.array([0,0,0])

for i in range(iter):
    V1 = np.dot(T, V0) + c
    error = np.linalg.norm(V1-V0, ord=p)/np.linalg.norm(V1, ord=p)
    if error < tol:
        break
    else:
        V0=V1
    print(V1)