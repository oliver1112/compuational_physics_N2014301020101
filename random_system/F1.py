import random
import pylab as pl
class rando_system:
    def __init__(self, n_step = 100):
        self.t=[0]
        self.x=[0]
        self.nsteps = n_step 
    def run(self):
        for i in range(1,self.nsteps):
            a=random.random()
            if a<0.5:
                self.x.append(self.x[i-1]+1)
            else:
                self.x.append(self.x[i-1]-1)
            self.t.append(t[i-1]+1)
    def show_result(self):
        pl.plot(self.t, self.x,'ko')
        pl.ylim(-10,10)
        pl.xlabel('step number')
        pl.ylabel('x')
        pl.show()
x=rando_system()
x.run()
x.show_result()
