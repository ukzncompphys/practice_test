import numpy
import math
def get_points(xmin=-10,xmax=10,npt=101):
    dx=(xmax-xmin)/(npt-1.0)
    x=numpy.arange(0,npt)*dx
    return x+xmin
def simpson(y,dx):
    tot=y[0]+y[-1]+4*y[1::2].sum()+2*y[2:-1:2].sum()
    return tot*dx/3.0

def integrate_fun(xmin,xmax,npt):
    x=get_points(xmin,xmax,npt)
    y=1/(1+x**2)
    dx=x[1]-x[0]
    return simpson(y,dx)

if __name__=='__main__':
    a=get_points()
    x0=get_points(xmin=-10,xmax=10,npt=161)
    y0=1/(1+x0**2)
    int0=simpson(y0,x0[1]-x0[0])
    
    int_left=integrate_fun(-10,-2,81)
    int_middle=integrate_fun(-2,2,81)
    int_right=integrate_fun(2,10,81)
    int2=int_left+int_middle+int_right


    print repr(int0-2*math.atan(10)) + ' ' + repr(int2-2*math.atan(10))
    
    

