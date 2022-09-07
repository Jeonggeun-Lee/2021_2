import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy import fft

in_image_lena = cv2.imread('lena_gray.png', 0)
f_lena = fft.fft2(in_image_lena)

fshift_lena = fft.fftshift(f_lena)
magnitude_input_lena = 20*np.log(np.abs(fshift_lena)+1e-10)

plt.subplot(111), plt.imshow(magnitude_input_lena, cmap='gray')
plt.title('magnitude of spectrum of lena')
plt.show()

h_lp = 1/25*np.array([[1,3,1], [3,9,3], [1,3,1]])
h_hp = np.array([[0,1,0], [1,-4,1], [0,1,0]])

height, width = in_image_lena.shape
h_lp = np.pad(h_lp, ((height//2-1, height//2-2),(width//2-1, width//2-2)), 'constant')
h_hp = np.pad(h_hp, ((height//2-1, height//2-2),(width//2-1, width//2-2)), 'constant')

f_h_lp = fft.fft2(h_lp)
f_h_hp = fft.fft2(h_hp)

f_lena_lp = fft.fftshift(np.multiply(f_lena, f_h_lp))
f_lena_hp = fft.fftshift(np.multiply(f_lena, f_h_hp))

magnitude_lp_output_lena = 20*np.log(np.abs(f_lena_lp)+1e-10)
magnitude_hp_output_lena = 20*np.log(np.abs(f_lena_hp)+1e-10)

plt.subplot(111), plt.imshow(magnitude_lp_output_lena, cmap='gray')
plt.title('magnitude of spectrum of low pass filtered lena')
plt.show()
plt.subplot(111), plt.imshow(magnitude_hp_output_lena, cmap='gray')
plt.title('magnitude of spectrum of high pass filtered lena')
plt.show()

lena_lp = np.real(fft.fftshift(fft.ifft2(fft.fftshift(f_lena_lp))))
lena_hp = np.real(fft.fftshift(fft.ifft2(fft.fftshift(f_lena_hp))))

plt.subplot(111), plt.imshow(lena_lp, cmap='gray')
plt.title('image of low pass filtered lena')
plt.show()
plt.subplot(111), plt.imshow(lena_hp, cmap='gray')
plt.title('image of high pass filtered lena')
plt.show()

####################################################

in_image_night = cv2.imread('dgu_night.png', 0)
f_night = fft.fft2(in_image_night)

fshift_night = fft.fftshift(f_night)
magnitude_input_night = 20*np.log(np.abs(fshift_night)+1e-10)

plt.subplot(111), plt.imshow(magnitude_input_night, cmap='gray')
plt.title('magnitude of spectrum of dgu night')
plt.show()

h_lp = 1/25*np.array([[1,3,1], [3,9,3], [1,3,1]])
h_hp = np.array([[0,1,0], [1,-4,1], [0,1,0]])

height, width = in_image_night.shape

h_lp = np.pad(h_lp, ((height//2-1, height//2-2),(width//2-1, width//2-2)), 'constant')
h_hp = np.pad(h_hp, ((height//2-1, height//2-2),(width//2-1, width//2-2)), 'constant')

f_h_lp = fft.fft2(h_lp)
f_h_hp = fft.fft2(h_hp)

f_night_lp = fft.fftshift(np.multiply(f_night, f_h_lp))
f_night_hp = fft.fftshift(np.multiply(f_night, f_h_hp))

magnitude_lp_output_night = 20*np.log(np.abs(f_night_lp)+1e-10)
magnitude_hp_output_night = 20*np.log(np.abs(f_night_hp)+1e-10)

plt.subplot(111), plt.imshow(magnitude_lp_output_night, cmap='gray')
plt.title('magnitude of spectrum of low pass filtered dgu night')
plt.show()
plt.subplot(111), plt.imshow(magnitude_hp_output_night, cmap='gray')
plt.title('magnitude of spectrum of high pass filtered dgu night')
plt.show()

night_lp = np.real(fft.fftshift(fft.ifft2(fft.fftshift(f_night_lp))))
night_hp = np.real(fft.fftshift(fft.ifft2(fft.fftshift(f_night_hp))))

plt.subplot(111), plt.imshow(night_lp, cmap='gray')
plt.title('image of low pass filtered dgu night')
plt.show()
plt.subplot(111), plt.imshow(night_hp, cmap='gray')
plt.title('image of high pass filtered dgu night')
plt.show()