import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.subplot(2,2,1)
plt.plot(x, np.sin(x),'-')
plt.subplot(4,4,15)
plt.plot(x, np.cos(x),'--')
# plt.show()

x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.plot(x, y, 'o', color='red');
plt.show()