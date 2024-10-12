# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.patches import Polygon
# Fixing random state for reproducibility
np.random.seed(5)
# fake up some data
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))
# don't show outlier points
fig, ax = plt.subplots()
ax.boxplot(data, 0, '', vert=False)
ax.set_title("don't show\noutlier points")

plt.show()