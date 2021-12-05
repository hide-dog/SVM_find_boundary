# --------------------------------------
import numpy as np
import matplotlib.pyplot as pyplot
from sklearn import svm
from sklearn.metrics import confusion_matrix
from mlxtend.plotting import plot_decision_regions
# --------------------------------------
pathf     = "d_loadtxt.csv"
pathftest = "d_loadtxt_sam.csv"
path_pic  = "result"
# SVM
kernel    = "rbf"
c         = 1
gamma     = 0.1
# --------------------------------------
data = np.loadtxt(pathf, delimiter=',')
y = data[:,2].astype(int)
x = data[:,0:2]

# clf = svm.SVC(kernel='linear')
# clf = svm.SVC(gamma="auto")
clf = svm.SVC(kernel=kernel, C=c, gamma=gamma)
clf.fit(x, y)

data = np.loadtxt(pathftest, delimiter=',')
ty = data[:,2].astype(int)
tx = data[:,0:2]
# --------------------------------------
pyplot.style.use('ggplot')

x_bind = np.vstack((tx,x))
y_bind = np.hstack((ty,y))

plot_decision_regions(x_bind, y_bind, clf=clf)
path_pic += "_" + kernel + "_c" + str(c) + "_g" + str(gamma) + ".png"
pyplot.savefig(path_pic)
# ------------------------------------
# output_data
with open("output_SVM_param", "w") as f:
    temp = sorted(clf.get_params(True).items())
    temp = '\n'.join(map(str, temp))
    f.write(temp)
#end
with open("output_support_vectors", "w") as f:
    temp = clf.support_vectors_[:,:]
    temp = '\n'.join(map(str, temp))
    f.write(temp)
#end
with open("output_dual_coef_", "w") as f:
    temp = clf.dual_coef_[0]
    temp = '\n'.join(map(str, temp))
    f.write(temp)
#end
with open("output_intercept_", "w") as f:
    temp = clf.intercept_
    temp = '\n'.join(map(str, temp))
    f.write(temp)
#end