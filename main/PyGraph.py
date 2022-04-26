import numpy as np
import matplotlib.pyplot as plt
# from matplotlib.pyplot import rc

# rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
# rc('text', usetex=True)

x = np.arange(0, 100, 1)
y1 = np.ones(100)
y2 = np.log(x)
y3 = x
y4 = x * np.log(x)
y5 = x * x

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.plot(x, y5)
plt.ylim(0, 1000)
plt.ylabel('time')
plt.xlabel('number of items')
# plt.yscale('symlog', linthreshy=0.015)
plt.yscale('symlog')

plt.text(90, 1.1, r'$O(1)$', {'color': 'C2', 'fontsize': 12}, va="bottom", ha="left")
plt.text(80, 5, r'$O(log(n))$', {'color': 'C2', 'fontsize': 12}, va="bottom", ha="left")
plt.text(63, 80, r'$O(n)$', {'color': 'C2', 'fontsize': 12}, va="bottom", ha="left")
plt.text(40, 90, r'$O(nlog(n))$', {'color': 'C2', 'fontsize': 12}, va="bottom", ha="left")
plt.text(7, 300, r'$O(n^2)$', {'color': 'C2', 'fontsize': 12}, va="bottom", ha="left")
plt.show()
