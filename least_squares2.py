import numpy
from matplotlib import pyplot as plt

#solve m=(A^T A)^-1 A^T x
def fit_params(x,A):
    if isinstance(A,numpy.matrixlib.defmatrix.matrix)==False:
        A=numpy.matrix(A)

    if isinstance(x,numpy.matrixlib.defmatrix.matrix)==False:
        x=numpy.matrix(x)
        x=x.transpose()
    
    lhs=A.transpose()*A
    rhs=A.transpose()*x
    param=numpy.linalg.inv(lhs)*rhs
    expected=A*param
    return param,expected

if __name__=='__main__':
    x=numpy.arange(-1,1,0.01)
    y=numpy.exp(1*x)
    y=y+numpy.random.randn(y.size)*0.001
    plt.ion()
    plt.clf()
    plt.plot(x,y,'*')
    plt.draw()
        
    order=8
    A=numpy.zeros([y.size,order])
    A[:,0]=1.0
    for i in range(1,order):
        A[:,i]=A[:,i-1]*x

    fitp,model=fit_params(y,A)
    print fitp
    plt.plot(x,model)
    plt.draw()
