import numpy as np
import matplotlib.pyplot as plt 

n=np.arange(0 ,70)
sigma=float(input("Enter the value of sigma: "))
A=float(input("Enter the amplitude of the signal: "))
f=float(input("Enter the frequency of the signal: "))
fs=float(input("Enter the sampling frequency: "))
x_n=A*np.exp(sigma*n)*np.exp(1j*2*np.pi*f*n/fs)

ax = plt.subplot2grid((2,3),(0,0),rowspan=2, projection='3d')
ax.plot(n, np.real(x_n), np.imag(x_n),marker='o', markersize=3, color='b', label='x[n]')
ax.set_title(rf'Complex Exponential Signal $\sigma={sigma}$')
ax.set_xlabel('n')
ax.set_ylabel('Real Part')
ax.set_zlabel('Imaginary Part')
ax.plot([0, 70], [0, 0], [0, 0], 'r--')
ax.plot([0, 0], [-20, 20], [0, 0], 'g--')
ax.plot([0, 0], [0, 0], [-20, 20], 'b--')


plt.subplot2grid((2,3),(0,1),colspan=2)
plt.grid(True)
plt.stem(n,np.real(x_n))
plt.title('Real Part')
plt.xlabel('n')
plt.ylabel('Amplitude')


plt.subplot2grid((2,3),(1,1),colspan=2)
plt.grid(True)
plt.stem(n,np.imag(x_n))
plt.title('Imaginary Part')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()  

