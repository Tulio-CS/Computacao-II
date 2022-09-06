from random import randint
import matplotlib.pyplot as plt
x = []

for i in range(10):
    x.append(randint(0,100))

plt.plot(x)


