#usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
data = np.load('ll_top.npy')
print(data)
plt.plot(data)
plt.xlabel('Generation')
plt.ylabel('Top Score')
plt.show()
