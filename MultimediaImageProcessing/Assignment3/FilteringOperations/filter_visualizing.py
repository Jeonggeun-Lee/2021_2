import numpy as np
import matplotlib.pyplot as plt
from numpy import fft
from matplotlib import cm
#h = 1/256*np.array([[21,31,21], [31,48,31], [21,31,21]])#Gaussian Filter
#h = 1/6*np.array([[1,2,1], [2,4,2], [1,2,1]])#Gaussian Filter
#h = 1/25*np.array([[1,3,1], [3,9,3], [1,3,1]])#Gaussian Filter
#h = np.array([[0.077847,0.123317,0.077847], [0.123317,0.195346,0.123317], [0.077847,0.123317,0.077847]])#Gaussian Filter
#h = np.array([[0,1,0], [1,-4,1], [0,1,0]])
h = 1/9*np.array([[1,1,1],[1,1,1],[1,1,1]])

h = np.pad(h, (254, 255), 'constant')

fh = fft.fft2(h)
fshift_fh = fft.fftshift(fh)

X, Y = np.meshgrid(np.arange(0,512), np.arange(0,512))
Z = np.abs(fshift_fh)

#plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.show()