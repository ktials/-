
import matplotlib.pyplot as plt

plt.title('Задание 1')
plt.xlabel('значение x1')
plt.ylabel('значение x2')
plt.xlim(0,40)

plt.ylim(0,40)
plt.scatter(x=13,y=19,c='black')
plt.scatter(x=17,y=14,c='black')
plt.plot([17, 17], [0,40], c='green')
plt.plot([0, 40], [19,19], c='orange')
plt.plot([28.2, 0],[0,35.25],c='blue')
plt.plot([12,0],[0,7],c='red')
plt.arrow(x=0,y=0,dx=3,dy=5, width=.2)
plt.text(3, 20, 'x2 <=19',fontsize=10)
plt.text(18, 1, 'x1 <=17',fontsize=10)
plt.text(21, 10, '4x1 + 5x2 <= 141',fontsize=10)
plt.text(2, 1, 'z(3,4)',fontsize=10)
plt.grid()
plt.show()
