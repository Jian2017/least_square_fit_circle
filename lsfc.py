
from scipy import optimize
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


class lsfc(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.center_estimate = 0,0

    def calc_R(self, xc, yc):
        return np.sqrt((self.x-xc)**2 + (self.y-yc)**2)

    def f_2(self,c):
        Ri = self.calc_R(*c)
        return Ri - Ri.mean()
    
    def findit(self):
        center_2, ier = optimize.leastsq(self.f_2, self.center_estimate)
        Ri_2       = self.calc_R(*center_2)
        R_2        = Ri_2.mean()
        #xc_2, yc_2 = center_2
        residu_2   = sum((Ri_2 - R_2)**2)
        return center_2, R_2, np.sqrt(residu_2)
    
    def showit(self):
        
        plt.close('all')
        fig = plt.figure(figsize=(6,6))
        ax = fig.add_subplot(111)
        ax.axis('equal')
        ax.plot(x, y, 'ro', label='test data', zorder=1)
        
        center_2,R_2,sigma=self.findit()
        
        ellipse = Ellipse(xy= center_2, width=2*R_2, height=2*R_2, angle=np.rad2deg(0),edgecolor='b', fc='None', lw=2, label='Fit', zorder = 2)
        ax.add_patch(ellipse)

        plt.legend()
        plt.show()
