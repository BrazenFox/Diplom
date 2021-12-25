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


def binomialBob(n, p, d):
    data_binom = binom(n, p)
    x = [j for j in range(n)]
    y = [data_binom.pmf(j) for j in x]
    print(y[0: 15])
    for i in range(n):
        if sum(y[0: i]) >= d:
            return i


def binomialEva(n, p, d):
    data_binom = binom(n, p)
    x = [j for j in range(n)]
    y = [data_binom.pmf(j) for j in x]
    for i in range(n):
        if sum(y[n - i: n]) >= d:
            return n - i


def gr(n, p):
    data_binom = binom(n, p)
    x = [j for j in range(n)]
    y = [data_binom.pmf(j) for j in x]
    return x, y


"""n = 60
p = 0.1
d = 0.9
data_binom = binom(100, 0.0001)
print(binomialBob(n, p, d), binomialEva(n, p, d), data_binom.pmf(0.1))
x, y = gr(n, p)
plt.xlabel('Count of errors')
plt.ylabel('Probability')
#plt.title('Binomial distribution')
plt.plot(x, y)
plt.scatter(3, 0.08, label = 'y=3')
plt.vlines(x[3:n], 0, y[3:n])
#plt.scatter(15, 0.031, label = 'x=15')
#plt.vlines(x[0:16], 0, y[0:16])
plt.legend()
plt.grid(True)
plt.show()

"""

plt.xlabel('Probability')
plt.ylabel('Safe baud rate')
plt.plot([0.01, 0.03, 0.05, 0.07, 0.1, 0.125, 0.15], [0.0075, 0.0225, 0.03, 0.037, 0.04, 0.037, 0.03])
# plt.scatter(15, 0.031, label = 'x=15')
# plt.vlines(x[0:16], 0, y[0:16])
plt.legend()
plt.grid(True)
plt.show()
