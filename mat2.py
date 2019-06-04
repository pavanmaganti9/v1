from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.plot(x,y,'g',label='LineOne',linewidth=5)
plt.plot(x2,y2,'c',label="LineTwo",linewidth=5)

plt.title("Info")
plt.ylabel("Y-axis")
plt.xlabel("X-axis")

plt.grid(True,color='K')

plt.show()