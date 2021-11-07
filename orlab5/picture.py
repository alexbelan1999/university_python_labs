import matplotlib.pyplot as plt
import numpy as np

step = 0.5
fontsize = 9
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x = np.arange(0, 12 + step, step)
x1 = np.arange(0, 9 + step, step)
x2 = np.arange(0, 12 + step, step)
x3 = np.arange(12, 22 + step, step)
x4 = np.arange(9, 13 + step, step)
x5 = 22
x6 = np.arange(22, 30 + step, step)
x7 = np.arange(22, 31 + step, step)
x8 = np.arange(31, 39 + step, step)
x9 = np.arange(31, 36 + step, step)
x10 = np.arange(39, 42 + step, step)

y = 1 + x * 0
y1 = 2 + x1 * 0
y2 = 3 + x2 * 0
y3 = 4 + x3 * 0
y4 = 5 + x4 * 0
y5 = 6 + x5 * 0
y6 = 7 + x6 * 0
y7 = 8 + x7 * 0
y8 = 9 + x8 * 0
y9 = 10 + x9 * 0
y10 = 11 + x10 * 0

plt.text(0, 1.1, '(p(0),p(1) 5', fontsize=fontsize)
ax.plot(x, y, 'k')
plt.text(0, 2.1, '(p(0),p(2) 2', fontsize=fontsize)
ax.plot(x1, y1, 'k')
plt.text(0, 3.1, '(p(0),p(6) 3', fontsize=fontsize)
ax.plot(x2, y2, 'k')
plt.text(12, 4.1, '(p(1),p(3) 9', fontsize=fontsize)
ax.plot(x3, y3, 'k')
plt.text(9, 5.1, '(p(2),p(4) 1', fontsize=fontsize)
ax.plot(x4, y4, 'k')
plt.text(22, 6.1, '(p(3),p(4)', fontsize=fontsize)
ax.plot(x5, y5, 'k.')
plt.text(22, 7.1, '(p(3),p(7) 4', fontsize=fontsize)
ax.plot(x6, y6, 'k')
plt.text(22, 8.1, '(p(4),p(5) 2', fontsize=fontsize)
ax.plot(x7, y7, 'k')
plt.text(31, 9.1, '(p(5),p(6) 5', fontsize=fontsize)
ax.plot(x8, y8, 'k')
plt.text(31, 10.1, '(p(5),p(7) 5', fontsize=fontsize)
ax.plot(x9, y9, 'k')
plt.text(39, 11.1, '(p(6),p(7) 3', fontsize=fontsize)
ax.plot(x10, y10, 'k')
plt.minorticks_on()
plt.title('Рисунок 1')
plt.grid(True)

plt.xticks(np.arange(0, 48, 2), np.arange(0, 48, 2))
plt.yticks(np.arange(0, 13, 1), np.arange(0, 13, 1))
plt.xlabel('Время')
plt.ylabel('Работы')
plt.show()
fig.savefig("рисунок 1.png", dpi=300, qualite=100)

fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
x = np.arange(0, 12 + step, step)
x1 = np.arange(9, 18 + step, step)
x2 = np.arange(27, 39 + step, step)
x3 = np.arange(12, 22 + step, step)
x4 = np.arange(18, 22 + step, step)
x5 = 22
x6 = np.arange(34, 42 + step, step)
x7 = np.arange(22, 31 + step, step)
x8 = np.arange(31, 39 + step, step)
x9 = np.arange(37, 42 + step, step)
x10 = np.arange(39, 42 + step, step)

y = 1 + x * 0
y1 = 2 + x1 * 0
y2 = 3 + x2 * 0
y3 = 4 + x3 * 0
y4 = 5 + x4 * 0
y5 = 6 + x5 * 0
y6 = 7 + x6 * 0
y7 = 8 + x7 * 0
y8 = 9 + x8 * 0
y9 = 10 + x9 * 0
y10 = 11 + x10 * 0

plt.text(0, 1.1, '(p(0),p(1) 5', fontsize=fontsize)
ax1.plot(x, y, 'k')
plt.text(9, 2.1, '(p(0),p(2) 2', fontsize=fontsize)
ax1.plot(x1, y1, 'k')
plt.text(27, 3.1, '(p(0),p(6) 3', fontsize=fontsize)
ax1.plot(x2, y2, 'k')
plt.text(12, 4.1, '(p(1),p(3) 9', fontsize=fontsize)
ax1.plot(x3, y3, 'k')
plt.text(18, 5.1, '(p(2),p(4) 1', fontsize=fontsize)
ax1.plot(x4, y4, 'k')
plt.text(22, 6.1, '(p(3),p(4)', fontsize=fontsize)
ax1.plot(x5, y5, 'k.')
plt.text(34, 7.1, '(p(3),p(7) 4', fontsize=fontsize)
ax1.plot(x6, y6, 'k')
plt.text(22, 8.1, '(p(4),p(5) 2', fontsize=fontsize)
ax1.plot(x7, y7, 'k')
plt.text(31, 9.1, '(p(5),p(6) 5', fontsize=fontsize)
ax1.plot(x8, y8, 'k')
plt.text(37, 10.1, '(p(5),p(7) 5', fontsize=fontsize)
ax1.plot(x9, y9, 'k')
plt.text(39, 11.1, '(p(6),p(7) 3', fontsize=fontsize)
ax1.plot(x10, y10, 'k')
plt.minorticks_on()
plt.title('Рисунок 2')
plt.grid(True)

plt.xticks(np.arange(0, 48, 2), np.arange(0, 48, 2))
plt.yticks(np.arange(0, 13, 1), np.arange(0, 13, 1))
plt.xlabel('Время')
plt.ylabel('Работы')
plt.show()
fig1.savefig("рисунок 2.png", dpi=300, qualite=100)

fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
x = np.arange(0, 9 + step, step)
x1 = np.arange(9, 12 + step, step)
x2 = np.arange(12, 13 + step, step)
x3 = np.arange(13, 22 + step, step)
x4 = np.arange(22, 30 + step, step)
x5 = np.arange(30, 31 + step, step)
x6 = np.arange(31, 36 + step, step)
x7 = np.arange(36, 39 + step, step)
x8 = np.arange(39, 42 + step, step)
x9 = np.arange(0, 44, 1)

y = 10 + x * 0
y1 = 9 + x1 * 0
y2 = 10 + x2 * 0
y3 = 9 + x3 * 0
y4 = 6 + x4 * 0
y5 = 2 + x5 * 0
y6 = 10 + x6 * 0
y7 = 5 + x7 * 0
y8 = 3 + x8 * 0
y9 = 8.9 + x9 * 0

plt.text(0, 10.1, '10', fontsize=fontsize)
ax2.plot(x, y, 'k')
plt.text(9, 9.1, '9', fontsize=fontsize)
ax2.plot(x1, y1, 'k')
plt.text(12, 10.1, '10', fontsize=fontsize)
ax2.plot(x2, y2, 'k')
plt.text(13, 9.1, '9', fontsize=fontsize)
ax2.plot(x3, y3, 'k')
plt.text(22, 6.1, '6', fontsize=fontsize)
ax2.plot(x4, y4, 'k')
plt.text(30, 2.1, '2', fontsize=fontsize)
ax2.plot(x5, y5, 'k')
plt.text(31, 10.1, '10', fontsize=fontsize)
ax2.plot(x6, y6, 'k')
plt.text(36, 5.1, '5', fontsize=fontsize)
ax2.plot(x7, y7, 'k')
plt.text(39, 3.1, '3', fontsize=fontsize)
ax2.plot(x8, y8, 'k')
plt.text(40, 9.1, 'R = 9', fontsize=fontsize)
ax2.plot(x9, y9, 'k--')

plt.minorticks_on()
plt.title('Рисунок 3')
plt.grid(True)

plt.xticks(np.arange(0, 48, 2), np.arange(0, 48, 2))
plt.yticks(np.arange(0, 13, 1), np.arange(0, 13, 1))
plt.xlabel('Время')
plt.ylabel('Суммарное потребление')
plt.show()
fig2.savefig("рисунок 3.png", dpi=300, qualite=100)

x10 = np.arange(9, 21 + step, step)
y10 = 3 + x10 * 0
ax.plot(x10, y10, 'r+')
fig.savefig("рисунок 4.png", dpi=300, qualite=100)

x11 = np.arange(18, 30 + step, step)
y11 = 3 + x11 * 0
ax.plot(x11, y11, 'b+')
x12 = np.arange(18, 22 + step, step)
y12 = 5 + x12 * 0
ax.plot(x12, y12, 'b+')
fig.savefig("рисунок 5.png", dpi=300, qualite=100)

fig3 = plt.figure()
ax3 = fig3.add_subplot(1, 1, 1)

x = np.arange(0, 12 + step, step)  # p01
x1 = np.arange(0, 9 + step, step)  # p02
x2 = np.arange(22, 34 + step, step)  # p06
x3 = np.arange(12, 22 + step, step)  # p13
x4 = np.arange(22, 26 + step, step)  # p24
x5 = 22  # p34
x6 = np.arange(22, 30 + step, step)  # p37
x7 = np.arange(26, 35 + step, step)  # p45
x8 = np.arange(35, 43 + step, step)  # p56
x9 = np.arange(35, 40 + step, step)  # p57
x10 = np.arange(43, 46 + step, step)  # p67

y = 1 + x * 0
y1 = 2 + x1 * 0
y2 = 3 + x2 * 0
y3 = 4 + x3 * 0
y4 = 5 + x4 * 0
y5 = 6 + x5 * 0
y6 = 7 + x6 * 0
y7 = 8 + x7 * 0
y8 = 9 + x8 * 0
y9 = 10 + x9 * 0
y10 = 11 + x10 * 0

plt.text(0, 1.1, '(p(0),p(1) 5', fontsize=fontsize)
ax3.plot(x, y, 'k')
plt.text(0, 2.1, '(p(0),p(2) 2', fontsize=fontsize)
ax3.plot(x1, y1, 'k')
plt.text(22, 3.1, '(p(0),p(6) 3', fontsize=fontsize)
ax3.plot(x2, y2, 'k')
plt.text(12, 4.1, '(p(1),p(3) 9', fontsize=fontsize)
ax3.plot(x3, y3, 'k')
plt.text(22, 5.1, '(p(2),p(4) 1', fontsize=fontsize)
ax3.plot(x4, y4, 'k')
plt.text(22, 6.1, '(p(3),p(4)', fontsize=fontsize)
ax3.plot(x5, y5, 'k.')
plt.text(22, 7.1, '(p(3),p(7) 4', fontsize=fontsize)
ax3.plot(x6, y6, 'k')
plt.text(26, 8.1, '(p(4),p(5) 2', fontsize=fontsize)
ax3.plot(x7, y7, 'k')
plt.text(35, 9.1, '(p(5),p(6) 5', fontsize=fontsize)
ax3.plot(x8, y8, 'k')
plt.text(35, 10.1, '(p(5),p(7) 5', fontsize=fontsize)
ax3.plot(x9, y9, 'k')
plt.text(43, 11.1, '(p(6),p(7) 3', fontsize=fontsize)
ax3.plot(x10, y10, 'k')
plt.minorticks_on()
plt.title('Рисунок 4')
plt.grid(True)

plt.xticks(np.arange(0, 48, 2), np.arange(0, 48, 2))
plt.yticks(np.arange(0, 13, 1), np.arange(0, 13, 1))
plt.xlabel('Время')
plt.ylabel('Работы')
plt.show()
fig3.savefig("рисунок 6.png", dpi=300, qualite=100)

fig4 = plt.figure()
ax4 = fig4.add_subplot(1, 1, 1)
x = np.arange(0, 12 + step, step)  # p01
x1 = np.arange(13, 22 + step, step)  # p02
x2 = np.arange(31, 43 + step, step)  # p06
x3 = np.arange(12, 22 + step, step)  # p13
x4 = np.arange(22, 26 + step, step)  # p24
x5 = 22  # p34
x6 = np.arange(38, 46 + step, step)  # p37
x7 = np.arange(26, 35 + step, step)  # p45
x8 = np.arange(35, 43 + step, step)  # p56
x9 = np.arange(41, 46 + step, step)  # p57
x10 = np.arange(43, 46 + step, step)  # p67

y = 1 + x * 0
y1 = 2 + x1 * 0
y2 = 3 + x2 * 0
y3 = 4 + x3 * 0
y4 = 5 + x4 * 0
y5 = 6 + x5 * 0
y6 = 7 + x6 * 0
y7 = 8 + x7 * 0
y8 = 9 + x8 * 0
y9 = 10 + x9 * 0
y10 = 11 + x10 * 0

plt.text(0, 1.1, '(p(0),p(1) 5', fontsize=fontsize)
ax4.plot(x, y, 'k')
plt.text(13, 2.1, '(p(0),p(2) 2', fontsize=fontsize)
ax4.plot(x1, y1, 'k')
plt.text(31, 3.1, '(p(0),p(6) 3', fontsize=fontsize)
ax4.plot(x2, y2, 'k')
plt.text(12, 4.1, '(p(1),p(3) 9', fontsize=fontsize)
ax4.plot(x3, y3, 'k')
plt.text(22, 5.1, '(p(2),p(4) 1', fontsize=fontsize)
ax4.plot(x4, y4, 'k')
plt.text(22, 6.1, '(p(3),p(4)', fontsize=fontsize)
ax4.plot(x5, y5, 'k.')
plt.text(38, 7.1, '(p(3),p(7) 4', fontsize=fontsize)
ax4.plot(x6, y6, 'k')
plt.text(26, 8.1, '(p(4),p(5) 2', fontsize=fontsize)
ax4.plot(x7, y7, 'k')
plt.text(35, 9.1, '(p(5),p(6) 5', fontsize=fontsize)
ax4.plot(x8, y8, 'k')
plt.text(41, 10.1, '(p(5),p(7) 5', fontsize=fontsize)
ax4.plot(x9, y9, 'k')
plt.text(43, 11.1, '(p(6),p(7) 3', fontsize=fontsize)
ax4.plot(x10, y10, 'k')
plt.minorticks_on()
plt.title('Рисунок 5')
plt.grid(True)

plt.xticks(np.arange(0, 48, 2), np.arange(0, 48, 2))
plt.yticks(np.arange(0, 13, 1), np.arange(0, 13, 1))
plt.xlabel('Время')
plt.ylabel('Работы')
plt.show()
fig4.savefig("рисунок 7.png", dpi=300, qualite=100)

x10 = np.arange(40, 45 + step, step)
y10 = 10 + x10 * 0
ax3.plot(x10, y10, 'r+')
fig3.savefig("рисунок 8.png", dpi=300, qualite=100)

x10 = np.arange(43, 48 + step, step)
y10 = 10 + x10 * 0
ax3.plot(x10, y10, 'b+')
fig3.savefig("рисунок 9.png", dpi=300, qualite=100)

fig5 = plt.figure()
ax5 = fig5.add_subplot(1, 1, 1)

x = np.arange(0, 12 + step, step)  # p01
x1 = np.arange(0, 9 + step, step)  # p02
x2 = np.arange(22, 34 + step, step)  # p06
x3 = np.arange(12, 22 + step, step)  # p13
x4 = np.arange(22, 26 + step, step)  # p24
x5 = 22  # p34
x6 = np.arange(22, 30 + step, step)  # p37
x7 = np.arange(26, 35 + step, step)  # p45
x8 = np.arange(35, 43 + step, step)  # p56
x9 = np.arange(43, 48 + step, step)  # p57
x10 = np.arange(43, 46 + step, step)  # p67

y = 1 + x * 0
y1 = 2 + x1 * 0
y2 = 3 + x2 * 0
y3 = 4 + x3 * 0
y4 = 5 + x4 * 0
y5 = 6 + x5 * 0
y6 = 7 + x6 * 0
y7 = 8 + x7 * 0
y8 = 9 + x8 * 0
y9 = 10 + x9 * 0
y10 = 11 + x10 * 0

plt.text(0, 1.1, '(p(0),p(1) 5', fontsize=fontsize)
ax5.plot(x, y, 'k')
plt.text(0, 2.1, '(p(0),p(2) 2', fontsize=fontsize)
ax5.plot(x1, y1, 'k')
plt.text(22, 3.1, '(p(0),p(6) 3', fontsize=fontsize)
ax5.plot(x2, y2, 'k')
plt.text(12, 4.1, '(p(1),p(3) 9', fontsize=fontsize)
ax5.plot(x3, y3, 'k')
plt.text(22, 5.1, '(p(2),p(4) 1', fontsize=fontsize)
ax5.plot(x4, y4, 'k')
plt.text(22, 6.1, '(p(3),p(4)', fontsize=fontsize)
ax5.plot(x5, y5, 'k.')
plt.text(22, 7.1, '(p(3),p(7) 4', fontsize=fontsize)
ax5.plot(x6, y6, 'k')
plt.text(26, 8.1, '(p(4),p(5) 2', fontsize=fontsize)
ax5.plot(x7, y7, 'k')
plt.text(35, 9.1, '(p(5),p(6) 5', fontsize=fontsize)
ax5.plot(x8, y8, 'k')
plt.text(43, 10.1, '(p(5),p(7) 5', fontsize=fontsize)
ax5.plot(x9, y9, 'k')
plt.text(43, 11.1, '(p(6),p(7) 3', fontsize=fontsize)
ax5.plot(x10, y10, 'k')
plt.minorticks_on()
plt.title('Рисунок 6')
plt.grid(True)

plt.xticks(np.arange(0, 52, 2), np.arange(0, 52, 2))
plt.yticks(np.arange(0, 13, 1), np.arange(0, 13, 1))
plt.xlabel('Время')
plt.ylabel('Работы')
plt.show()
fig5.savefig("рисунок 10.png", dpi=300, qualite=100)

fig6 = plt.figure()
ax6 = fig6.add_subplot(1, 1, 1)
x = np.arange(6, 18 + step, step)  # p01
x1 = np.arange(15, 24 + step, step)  # p02
x2 = np.arange(33, 45 + step, step)  # p06
x3 = np.arange(18, 28 + step, step)  # p13
x4 = np.arange(24, 28 + step, step)  # p24
x5 = 28  # p34
x6 = np.arange(40, 48 + step, step)  # p37
x7 = np.arange(28, 37 + step, step)  # p45
x8 = np.arange(37, 45 + step, step)  # p56
x9 = np.arange(43, 48 + step, step)  # p57
x10 = np.arange(45, 48 + step, step)  # p67

y = 1 + x * 0
y1 = 2 + x1 * 0
y2 = 3 + x2 * 0
y3 = 4 + x3 * 0
y4 = 5 + x4 * 0
y5 = 6 + x5 * 0
y6 = 7 + x6 * 0
y7 = 8 + x7 * 0
y8 = 9 + x8 * 0
y9 = 10 + x9 * 0
y10 = 11 + x10 * 0

plt.text(6, 1.1, '(p(0),p(1) 5', fontsize=fontsize)
ax6.plot(x, y, 'k')
plt.text(15, 2.1, '(p(0),p(2) 2', fontsize=fontsize)
ax6.plot(x1, y1, 'k')
plt.text(33, 3.1, '(p(0),p(6) 3', fontsize=fontsize)
ax6.plot(x2, y2, 'k')
plt.text(18, 4.1, '(p(1),p(3) 9', fontsize=fontsize)
ax6.plot(x3, y3, 'k')
plt.text(24, 5.1, '(p(2),p(4) 1', fontsize=fontsize)
ax6.plot(x4, y4, 'k')
plt.text(28, 6.1, '(p(3),p(4)', fontsize=fontsize)
ax6.plot(x5, y5, 'k.')
plt.text(40, 7.1, '(p(3),p(7) 4', fontsize=fontsize)
ax6.plot(x6, y6, 'k')
plt.text(28, 8.1, '(p(4),p(5) 2', fontsize=fontsize)
ax6.plot(x7, y7, 'k')
plt.text(37, 9.1, '(p(5),p(6) 5', fontsize=fontsize)
ax6.plot(x8, y8, 'k')
plt.text(43, 10.1, '(p(5),p(7) 5', fontsize=fontsize)
ax6.plot(x9, y9, 'k')
plt.text(45, 11.1, '(p(6),p(7) 3', fontsize=fontsize)
ax6.plot(x10, y10, 'k')
plt.minorticks_on()
plt.title('Рисунок 7')
plt.grid(True)

plt.xticks(np.arange(0, 52, 2), np.arange(0, 52, 2))
plt.yticks(np.arange(0, 13, 1), np.arange(0, 13, 1))
plt.xlabel('Время')
plt.ylabel('Работы')
plt.show()
fig6.savefig("рисунок 11.png", dpi=300, qualite=100)

fig7 = plt.figure()
ax7 = fig7.add_subplot(1, 1, 1)
x = np.arange(0, 9 + step, step)
x1 = np.arange(9, 12 + step, step)
x2 = np.arange(12, 22 + step, step)
x3 = np.arange(22, 26 + step, step)
x4 = np.arange(26, 30 + step, step)
x5 = np.arange(30, 34 + step, step)
x6 = np.arange(34, 35 + step, step)
x7 = np.arange(35, 43 + step, step)
x8 = np.arange(43, 46 + step, step)
x9 = np.arange(46, 48 + step, step)
x10 = np.arange(0, 52, 1)

y = 7 + x * 0
y1 = 5 + x1 * 0
y2 = 9 + x2 * 0
y3 = 8 + x3 * 0
y4 = 9 + x4 * 0
y5 = 5 + x5 * 0
y6 = 2 + x6 * 0
y7 = 5 + x7 * 0
y8 = 8 + x8 * 0
y9 = 5 + x9 * 0
y10 = 8.9 + x10 * 0

plt.text(0, 7.1, '7', fontsize=fontsize)
ax7.plot(x, y, 'k')
plt.text(9, 5.1, '5', fontsize=fontsize)
ax7.plot(x1, y1, 'k')
plt.text(12, 9.1, '9', fontsize=fontsize)
ax7.plot(x2, y2, 'k')
plt.text(22, 8.1, '8', fontsize=fontsize)
ax7.plot(x3, y3, 'k')
plt.text(26, 9.1, '9', fontsize=fontsize)
ax7.plot(x4, y4, 'k')
plt.text(30, 5.1, '5', fontsize=fontsize)
ax7.plot(x5, y5, 'k')
plt.text(34, 2.1, '2', fontsize=fontsize)
ax7.plot(x6, y6, 'k')
plt.text(35, 5.1, '5', fontsize=fontsize)
ax7.plot(x7, y7, 'k')
plt.text(43, 8.1, '8', fontsize=fontsize)
ax7.plot(x8, y8, 'k')
plt.text(46, 5.1, '5', fontsize=fontsize)
ax7.plot(x9, y9, 'k')
plt.text(40, 9.1, 'R = 9', fontsize=fontsize)
ax7.plot(x10, y10, 'k--')

plt.minorticks_on()
plt.title('Рисунок 8')
plt.grid(True)

plt.xticks(np.arange(0, 52, 2), np.arange(0, 52, 2))
plt.yticks(np.arange(0, 13, 1), np.arange(0, 13, 1))
plt.xlabel('Время')
plt.ylabel('Суммарное потребление')
plt.show()
fig7.savefig("рисунок 12.png", dpi=300, qualite=100)
