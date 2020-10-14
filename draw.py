#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
data = np.load('mc_top.npy')
print(data)
plt.plot(data)
plt.xlabel('Generation')
plt.ylabel('Average Score')
plt.show()
