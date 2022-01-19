import math
from math import log
from random import randint, random
import numpy as np
from functools import reduce
import scipy.special
from scipy.stats import binom
from Cascade import Cascade
from Analizer import Analizer
from RunAnalizer import RunAnalizer
import seaborn as sb
import matplotlib.pyplot as plt



confidence_level = [0.8, 0.9, 0.99, 0.999]
averaging = 3
count_of_raunds_for_cascade = [2, 4, 6, 8]
fix_count_of_raunds_for_cascade=4
fix_confidence_level=0.9
e = [0.15, 0.1, 0.01, 0.001, 0.0001]
p = [0.15, 0.1, 0.01, 0.001, 0.0001]
n_array = [[100, 300, 1000, 3000, 10000, 30000, 100000],
           [100, 300, 1000, 3000, 10000, 30000, 100000],
           [300, 1000, 3000, 10000, 30000, 100000],
           [1000, 3000, 10000, 30000, 100000],
           [3000, 10000, 30000, 100000]]
"""n_array = [[100, 300, 1000, 3000, 10000],
           [300, 1000, 3000, 10000],
           [1000, 3000, 10000, 30000],
           [3000, 10000, 30000, 100000]]"""


r = RunAnalizer(confidence_level,averaging, count_of_raunds_for_cascade, e,p,n_array)
array_e_p, array_E_p, array_e_P = r.RunForConfidenceLevel(fix_count_of_raunds_for_cascade)

iterator = 0
for i in range(len(confidence_level)):
    plt.xlabel('количество бит')
    plt.ylabel('Безопасная скорость передачи')
    plt.xscale('log')
    plt.title(f'Безопасная скорость передачи в зависимости от длины сообщения при различных вероятностях ошибок \n количество раундов={fix_count_of_raunds_for_cascade} \n d={confidence_level[i]}')
    for j in range(len(n_array)):
        plt.plot(n_array[j], [array_e_p[i][j][k] / n_array[j][k] for k in range(len(n_array[j]))], label=f'e={e[j]},p={p[j]}')
    plt.legend()
    plt.grid(True)
    iterator+=1
    plt.savefig(f'results/{iterator} ep number of rounds={fix_count_of_raunds_for_cascade}, confidence level={confidence_level[i]}.png')
    plt.show()

    plt.xlabel('Count of bits')
    plt.ylabel('Safe baud rate')
    plt.xscale('log')
    plt.title(f'Безопасная скорость передачи в зависимости от длины сообщения при различных вероятностях ошибок \n количество раундов={fix_count_of_raunds_for_cascade} \n d={confidence_level[i]}')
    for j in range(len(n_array)):
        plt.plot(n_array[j], [array_E_p[i][j][k] / n_array[j][k] for k in range(len(n_array[j]))], label=f'e={e[0]},p={p[j]}')
    plt.legend()
    plt.grid(True)
    iterator += 1
    plt.savefig(f'results/{iterator} Ep number of rounds={fix_count_of_raunds_for_cascade}, confidence level={confidence_level[i]}.png')
    plt.show()

    plt.xlabel('Count of bits')
    plt.ylabel('Safe baud rate')
    plt.xscale('log')
    plt.title(f'Безопасная скорость передачи в зависимости от длины сообщения при различных вероятностях ошибок \n количество раундов={fix_count_of_raunds_for_cascade} \n d={confidence_level[i]}')
    for j in range(len(n_array)):
        plt.plot(n_array[j], [array_e_P[i][j][k] / n_array[j][k] for k in range(len(n_array[j]))], label=f'e={e[j]},p={p[0]}')
    plt.legend()
    plt.grid(True)
    iterator += 1
    plt.savefig(f'results/{iterator} eP number of rounds={fix_count_of_raunds_for_cascade}, confidence level={confidence_level[i]}.png')
    plt.show()

array_e_p, array_E_p, array_e_P = r.RunForCountOfRaundsForCascade(fix_confidence_level)

for i in range(len(count_of_raunds_for_cascade)):
    plt.xlabel('Count of bits')
    plt.ylabel('Safe baud rate')
    plt.xscale('log')
    plt.title(f'Безопасная скорость передачи в зависимости от длины сообщения при различных вероятностях ошибок \n количество раундов={fix_count_of_raunds_for_cascade} \n d={confidence_level[i]}')
    for j in range(len(n_array)):
        plt.plot(n_array[j], [array_e_p[i][j][k] / n_array[j][k] for k in range(len(n_array[j]))], label=f'e={e[j]},p={p[j]}')
    plt.legend()
    plt.grid(True)
    iterator += 1
    plt.savefig(f'results/{iterator} ep number of rounds={count_of_raunds_for_cascade[i]}, confidence level={fix_confidence_level}.png')
    plt.show()

    plt.xlabel('Count of bits')
    plt.ylabel('Safe baud rate')
    plt.xscale('log')
    plt.title(f'Безопасная скорость передачи в зависимости от длины сообщения при различных вероятностях ошибок \n количество раундов={fix_count_of_raunds_for_cascade} \n d={confidence_level[i]}')
    for j in range(len(n_array)):
        plt.plot(n_array[j], [array_E_p[i][j][k] / n_array[j][k] for k in range(len(n_array[j]))], label=f'e={e[0]},p={p[j]}')
    plt.legend()
    plt.grid(True)
    iterator += 1
    plt.savefig(f'results/{iterator} Ep number of rounds={count_of_raunds_for_cascade[i]}, confidence level={fix_confidence_level}.png')
    plt.show()

    plt.xlabel('Count of bits')
    plt.ylabel('Safe baud rate')
    plt.xscale('log')
    plt.title(f'Безопасная скорость передачи в зависимости от длины сообщения при различных вероятностях ошибок \n количество раундов={fix_count_of_raunds_for_cascade} \n d={confidence_level[i]}')
    for j in range(len(n_array)):
        plt.plot(n_array[j], [array_e_P[i][j][k] / n_array[j][k] for k in range(len(n_array[j]))], label=f'e={e[j]},p={p[0]}')
    plt.legend()
    plt.grid(True)
    iterator += 1
    plt.savefig(f'results/{iterator} eP number of rounds={count_of_raunds_for_cascade[i]}, confidence level={fix_confidence_level}.png')
    plt.show()




"""
array_e_p = [[] for i in range(4)]
array_E_p = [[] for i in range(4)]
array_e_P = [[] for i in range(4)]

for i in range(4):
    for n in n_array[i]:
        print(n)
        analizer = Analizer(n, p[i], e[i], confidence_level, averaging, count_of_raunds_for_cascade)
        array_e_p[i].append(analizer.RunCascade())
for i in range(4):
    for n in n_array[i]:
        print(n)
        analizer = Analizer(n, p[i], 0.1, confidence_level, averaging, count_of_raunds_for_cascade)
        array_E_p[i].append(analizer.RunCascade())
for i in range(4):
    for n in n_array[i]:
        print(n)
        analizer = Analizer(n, 0.1, e[i], confidence_level, averaging, count_of_raunds_for_cascade)
        array_e_P[i].append(analizer.RunCascade())

plt.xlabel('Count of bits')
plt.ylabel('Safe baud rate')
plt.title('Safe transmission rate on the number of bits for different error rates')
plt.xscale('log')

plt.plot(n_array[0], [array_e_p[0][i] / n_array[0][i] for i in range(len(n_array[0]))], label='e=0.1, p=0.1 ')
plt.plot(n_array[1], [array_e_p[1][i] / n_array[1][i] for i in range(len(n_array[1]))], label='e=0.01, p=0.01 ')
plt.plot(n_array[2], [array_e_p[2][i] / n_array[2][i] for i in range(len(n_array[2]))], label='e=0.001, p=0.001 ')
plt.plot(n_array[3], [array_e_p[3][i] / n_array[3][i] for i in range(len(n_array[3]))], label='e=0.0001, p=0.0001 ')
plt.legend()
plt.grid(True)
plt.show()
plt.plot(n_array[0], [array_E_p[0][i] / n_array[0][i] for i in range(len(n_array[0]))], label='e=0.1, p=0.1 ')
plt.plot(n_array[1], [array_E_p[1][i] / n_array[1][i] for i in range(len(n_array[1]))], label='e=0.1, p=0.01 ')
plt.plot(n_array[2], [array_E_p[2][i] / n_array[2][i] for i in range(len(n_array[2]))], label='e=0.1, p=0.001 ')
plt.plot(n_array[3], [array_E_p[3][i] / n_array[3][i] for i in range(len(n_array[3]))], label='e=0.1, p=0.0001 ')
plt.legend()
plt.grid(True)
plt.show()
plt.plot(n_array[0], [array_e_P[0][i] / n_array[0][i] for i in range(len(n_array[0]))], label='e=0.1, p=0.1 ')
plt.plot(n_array[1], [array_e_P[1][i] / n_array[1][i] for i in range(len(n_array[1]))], label='e=0.01, p=0.1 ')
plt.plot(n_array[2], [array_e_P[2][i] / n_array[2][i] for i in range(len(n_array[2]))], label='e=0.001, p=0.1 ')
plt.plot(n_array[3], [array_e_P[3][i] / n_array[3][i] for i in range(len(n_array[3]))], label='e=0.0001, p=0.1 ')
plt.legend()
plt.grid(True)
plt.show()"""

"""ep=np.arange(0.001,0.2, 0.001)
res2=[]
print(ep)
for i in ep:
    er=round(i,4)
    print(i,er)
    analizer1 = Analizer(10000, er, er, accuracy, averaging, count_of_raunds_for_cascade)
    res2.append(analizer1.RunCascade())

plt.xlabel('bit error')
plt.ylabel('Safe baud rate')
plt.title('Safe baud rate of bit error')
plt.plot(ep, [res2[i] / 10000 for i in range(len(res2))])
plt.grid(True)
plt.show()"""
