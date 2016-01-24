from matplotlib import pyplot as plt
import numpy as np

# plot function can draw multi plot
plt.plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
plt.plot([1,2,3], [1,4,9], 'rs',  label='line 2')
plt.plot([1,2,3], [4,6,8], color='g', linestyle='--', label='line 3',
	marker='o', markersize=6)

plt.grid()
plt.legend()


plt.show()

plt.scatter([1,3,4,5,5,4,1],[65,23,15,65,61,51,13])
plt.show()