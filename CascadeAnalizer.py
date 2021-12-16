import math
from math import log
from random import randint, random
import numpy as np
from functools import reduce
import scipy.special
from scipy.stats import binom
from Cascade import Cascade
import seaborn as sb
import matplotlib.pyplot as plt


class Analizer:
    def __init__(self, n, p, e, accuracy, averaging, count_of_raunds_for_cascade):
        self.n = n
        self.p = p
        self.e = e
        self.accuracy = accuracy
        self.count_errors = int(self.binomial(n, p)[1])
        self.averaging = averaging
        self.count_of_raunds_for_cascade = count_of_raunds_for_cascade

    def binomial(self, n, p):
        data_binom = binom(n, p)
        x = [j for j in range(n)]
        y = [data_binom.pmf(j) for j in x]

        disp = n * p * (1 - p)
        for j in range(int(min(n * p, n - n * p))):
            if sum(y[int(n * p - j):int(n * p + j)]) >= self.accuracy:
                return n * p - (j - 1), n * p + (j - 1)
        return 0, 1

    def select_a_b(self, n, count_of_error):
        a = [randint(0, 1) for i in range(n)]
        b = [0] * n
        errors = []
        while len(errors) != count_of_error:
            number = randint(0, n - 1)
            if not errors.__contains__(number):
                errors.append(number)
        for i in range(n):
            b[i] = a[i] ^ 1 if errors.__contains__(i) else a[i]
        return a, b

    def RunCascade(self):
        result = 0
        for i in range(self.averaging):
            a, b = self.select_a_b(self.n, self.count_errors)
            cascade = Cascade(a, b, self.p, self.count_of_raunds_for_cascade)
            count_non_fixed_error = cascade.start()
            if count_non_fixed_error > 0:
                print("error", count_non_fixed_error)
                break
            result += self.binomial(int(self.n - cascade.iter), self.e)[0]
        result //= self.averaging
        return result


"""n = 10000
p = 0.1
e = 0.1
accuracy = 0.9
averaging=10
count_of_raunds_for_cascade=4
analizer=Analizer(n, p, e, accuracy, averaging, count_of_raunds_for_cascade)
print(analizer.RunCascade())"""
#######################################################################################################
accuracy = 0.8
averaging = 1
count_of_raunds_for_cascade = 4
n_array = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000,
           10000, 50000, 100000]
array_e_p = [[] for i in range(4)]
array_E_p = [[] for i in range(4)]
array_e_P = [[] for i in range(4)]
e = [0.1, 0.05, 0.01, 0.005]
p = [0.1, 0.05, 0.01, 0.005]
for i in range(4):
    for n in n_array:
        print(n)
        analizer = Analizer(n, p[i], e[i], accuracy, averaging, count_of_raunds_for_cascade)
        array_e_p[i].append(analizer.RunCascade())
for i in range(4):
    for n in n_array:
        print(n)
        analizer = Analizer(n, p[i], 0.1, accuracy, averaging, count_of_raunds_for_cascade)
        array_E_p[i].append(analizer.RunCascade())
for i in range(4):
    for n in n_array:
        print(n)
        analizer = Analizer(n, 0.1, e[i], accuracy, averaging, count_of_raunds_for_cascade)
        array_e_P[i].append(analizer.RunCascade())

fig, ax = plt.subplots(1, 3)
fig.suptitle('Horizontally stacked subplots')
ax[0].set_xscale('log')
ax[1].set_xscale('log')
ax[2].set_xscale('log')
ax[0].plot(n_array, array_e_p[0])
ax[0].plot(n_array, array_e_p[1])
ax[0].plot(n_array, array_e_p[2])
ax[0].plot(n_array, array_e_p[3])
ax[1].plot(n_array, array_E_p[0])
ax[1].plot(n_array, array_E_p[1])
ax[1].plot(n_array, array_E_p[2])
ax[1].plot(n_array, array_E_p[3])
ax[2].plot(n_array, array_e_P[0])
ax[2].plot(n_array, array_e_P[1])
ax[2].plot(n_array, array_e_P[2])
ax[2].plot(n_array, array_e_P[3])

plt.show()
