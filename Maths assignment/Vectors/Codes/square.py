import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import subprocess
import shlex
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def line_gen(A,B):
    len = 10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
        temp1 = A + lam_1[i]*(B-A)
        x_AB[:,i] = temp1.T
    return x_AB


A = np.array(([-1,2]))
C = np.array(([3,2]))
B = np.array(([(A[0]-A[1]+C[0]+C[1])/2,(A[0]+A[1]-C[0]+C[1])/2]))
#find midpoint
M = (A+C)/2
#coords of Fourth point
D_x = 2*M[0]-B[0] 
D_y = 2*M[1]-B[1]
O = np.array(([(A+C)/2]))

D = np.array(([D_x,D_y]))

#line generation
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)
x_AC = line_gen(A,C)
x_BD = line_gen(B,D)

plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')


sqr_vert = np.vstack((A,B,C,D,O)).T
plt.scatter(sqr_vert[0,:],sqr_vert[1,:])
vert_labels = ['A(-1,2)','B(1,0)','C(3,2)','D(1,4)','O(1,2)']

for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
            (sqr_vert[0,i], sqr_vert[1,i]),
            textcoords = 'offset points',
            xytext = (0,10),
            ha='center')


plt.xlabel('$x$')                    
plt.ylabel('$y$')
#plt.legend(loc='best')
plt.grid()
plt.axis('equal')
#plt.savefig('/home/annu/Parvvv/Latex files/WORK/square.png')
plt.show()