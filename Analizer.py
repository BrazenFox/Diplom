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
        self.count_errors = int(self.binomialBob(n, p))
        self.averaging = averaging
        self.count_of_raunds_for_cascade = count_of_raunds_for_cascade

    def binomialBob(self, n, p):
        data_binom = binom(n, p)
        x = [j for j in range(n)]
        y = [data_binom.pmf(j) for j in x]
        for i in range(n):
            if sum(y[0: i]) >= self.accuracy:
                return i

    def binomialEva(self, n, p):
        data_binom = binom(n, p)
        x = [j for j in range(n)]
        y = [data_binom.pmf(j) for j in x]
        for i in range(n):
            if sum(y[n - i: n]) >= self.accuracy:
                return n - i
        return 0

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
            """if count_non_fixed_error > 0:
                print("error", count_non_fixed_error)
                break"""
            result += self.binomialEva(int(self.n - cascade.iter), self.e)
        result //= self.averaging
        return result






