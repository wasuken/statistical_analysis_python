import numpy as np
import matplotlib.pyplot as plt


# リスト 3-9

t = np.arange(0., 5., 0.2)

plt.title('drawing example1')
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='square')
plt.plot(t, t**3, 'g^', label='cube')
plt.xlabel('x values')
plt.ylabel('y values')
plt.legend()
plt.show()
