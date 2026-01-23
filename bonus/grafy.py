import matplotlib.pyplot as plt

znamky = [5, 5, 3, 2, 1, 1, 3, 2, 1, 1, 1, 1]
znamky2 = [4, 4, 2, 3, 5, 2, 1, 2, 4, 1, 2, 2, 1]
x = []
y = []
y2 = []
s = 0
s2 = 0

for i in range(len(znamky)):
    x.append(i)
    s += znamky[i]
    s2 += znamky2[i]
    y.append(s / (i + 1))
    y2.append(s2 / (i + 1))

#plt.scatter(x, y)
plt.plot(x, y)
plt.plot(x, y2)
plt.show()
