from time import*

def zbroj(a):
    zbroj= 0

    for i in range(1, a+1 ):
        zbroj = zbroj + i
    print(zbroj)

brojevi = []
vremena = []

for n in range(100, 1000001, 100000):
    print('n: ', n)
    t1 = time()
    zovi = zbroj(n)
    t2 = time()
    brojevi.append(n)
    vremena.append(t2-t1)
    print('zbroj1:', t2-t1, 'sekundi')

from matplotlib import pyplot as plt


plt.plot(vremena, label = "vremena")
plt.legend()
plt.show()