import matplotlib.pyplot as plt
import numpy as np

# Line Chart
x = [100, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]  # x-coordinates of points
k1 = [737, 11091, 44885, 98065, 177439, 290730, 397956, 530784, 739215, 929991]  # y-coordinates for line 1
k2 = [266, 8966, 39863, 94957, 175453, 282193, 415827, 576884, 765810, 982992]  # y-coordinates for line 2 (theory)
plt.plot(x, k1, 's-', color='firebrick', lw=2.5, label="Experimental Results")  # s-: square marker
plt.plot(x, k2, 'o-', color='royalblue', lw=2.5, label="Theoretical Result")  # o-: circle marker
plt.xlabel("n value")  # x-axis label
plt.ylabel("time")  # y-axis label
plt.xticks(np.arange(0, 5000, 500))  # Customize x-axis tick marks
plt.yticks(np.arange(0, 1100000, 100000))  # Customize y-axis tick marks
plt.ticklabel_format(style='plain')  # Disable scientific notation
plt.grid(axis='y')  # Add y-axis gridlines
plt.legend(loc="best")  # Legend
plt.show()
