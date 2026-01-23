import matplotlib.pyplot as plt
import random

x = []
y = []
y2 = []
for i in range(10):
    x.append(i)
    y.append(random.randint(1, 6))
    y2.append(random.randint(3, 6))

plt.plot(x, y)
plt.plot(x, y2)
plt.show()
