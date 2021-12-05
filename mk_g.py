#----------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#----------------------------------------
n = 20
delta = 40
m = 100
path_pic = "sample"
pathf = "d"

#----------------------------------------
x = np.ones([n])
y = np.ones([n])
z = np.ones([n,n])
#----------------------------------------
for i in range(n):
    x[i] = m * i / n
    y[i] = m * i / n
#end
for i in range(n):
    for j in range(n):
        if (x[i]-80)**2 + (y[j]-40)**2 < 50**2:
            z[i,j] = 0
        #end
    #end
#end
#----------------------------------------
# with open(pathf + "_pandas.csv", "w") as f:
#     temp = ","

#     for i in range(n):
#         temp += str(x[i])
#         temp += ","
#     #end
#     temp += "\n"
#     f.write(temp)

#     for i in range(n):
#         temp = str(y[i]) 
#         temp += ","
#         for j in range(n):
#             temp += str(z[i,j]) 
#             temp += ","
#         #end
#         temp += "\n"
#         f.write(temp)
#     #end
# #end
#--------------------------------------------
with open(pathf + "_loadtxt.csv", "w") as f:
    for i in range(n):
        for j in range(n):
            temp = ""
            temp += str(x[i])
            temp += ","
            temp += str(y[j])
            temp += ","
            temp += str(z[i,j]) 
    
            temp += "\n"
            f.write(temp)
        #end
    #end
#end
with open(pathf + "_loadtxt_sam.csv", "w") as f:
    ite = 0
    for i in range(n):
        for j in range(n):
            if ite == delta:
                temp = ""
                temp += str(x[i])
                temp += ","
                temp += str(y[j])
                temp += ","
                temp += str(z[i,j]) 
        
                temp += "\n"
                f.write(temp)
                ite = 0
            else:
                ite += 1
            #end
        #end
    #end
#end
#----------------------------------------
# xx, yy = np.meshgrid(y,x)
# plt.contourf(xx, yy, np.transpose(z))
# plt.savefig(path_pic)
#----------------------------------------
# mk grids
xx = np.ones([n+1])
yy = np.ones([n+1])
xx[n-1] = x[n-2] - 0.5*(x[n-3] - x[n-2])
yy[n-1] = y[n-2] - 0.5*(y[n-3] - y[n-2])
xx[n] = x[n-1] - 0.5*(x[n-2] - x[n-1])
yy[n] = y[n-1] - 0.5*(y[n-2] - y[n-1])
for i in range(n-1):
    xx[i] = x[i] - 0.5*(x[i+1] - x[i])
    yy[i] = y[i] - 0.5*(y[i+1] - y[i])
#end
xx, yy = np.meshgrid(yy,xx)
plt.pcolormesh(xx, yy, np.transpose(z))
plt.savefig(path_pic)
#----------------------------------------