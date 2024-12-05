#import matplotlib as matplotlib
import matplotlib.pyplot as plt
import numpy as np
#import matplotlib.patches as mpatches
from matplotlib.patches import Ellipse
#from math import pi

import plotly as ply
import plotly.express as px
import plotly.graph_objects as go

x = np.linspace(1,1000,100)

#plot fields
y= 0.001*x** -1.0
y1= 0.00001*x** -1.0
plt.axvline(x=1000, ymin= 0, ymax= 0.425, color='cornflowerblue')

#plt.plot(a,b)
plt.plot(x, y, 'cornflowerblue')
plt.plot(x, y1, 'cornflowerblue')
plt.title('F-N diagram for societal risk')


#plt.scatter( 3000 , 0.000001 , s = 100, facecolors = 'red')
#plt.axvline(x=3000, ymin= 0.285, ymax= 0.57, color='red')
#plt.axhline(y=0.000001, xmin= 0.75, xmax= 0.98, color='red')

##Asset 1, no risk reduction metric
#plt.scatter( 300 , 0.00000012 , s = 100, facecolors = 'red')
##Asset 1 with risk reduction measure: one order of magnitude PT:S reduction
#plt.scatter( 300 , 0.000000012 , s = 100, facecolors = 'red')

#plt.text(3500, 0.0000015, 'a')
#plt.text(350, 0.00000009, 'b')
#plt.text(350, 0.00000001, 'c')


plt.text(15, 0.001, 'Unacceptable')
plt.text(20, 0.000005, 'ALARP')
plt.text(5, 0.00000001, 'Broadly acceptable')

plt.xlim([1,10000])
plt.ylim([0.000000001,0.01])

plt.xscale("log")
plt.yscale("log")
plt.xlabel('Number of fatalities (N)', color='#1C2833')
plt.ylabel('Probability of N or more fatalities per year (F)', color='#1C2833')
#plt.legend(loc='upper left')
plt.grid(True,)
plt.show()
