import math
from math import log
from random import randint, random
import numpy as np
from functools import reduce
import scipy.special
from scipy.stats import binom
from Cascade import Cascade
from Analizer import Analizer
import seaborn as sb
import matplotlib.pyplot as plt




class RunAnalizer():
    def __init__(self, confidence_level, averaging, count_of_raunds_for_cascade, e, p, n_array):
        if len(e) != len(p) != len(n_array):
            RuntimeError("not equals len")
        self.confidence_level = confidence_level
        self.averaging = averaging
        self.count_of_raunds_for_cascade = count_of_raunds_for_cascade
        self.e = e
        self.p = p
        self.n_array = n_array
        self.count = len(e)

    def RunForConfidenceLevel(self, fix_count_of_raunds_for_cascade):
        array_e_p = [[[] for i in range(self.count)] for j in range(len(self.confidence_level))]
        array_E_p = [[[] for i in range(self.count)] for j in range(len(self.confidence_level))]
        array_e_P = [[[] for i in range(self.count)] for j in range(len(self.confidence_level))]
        for level in range(len(self.confidence_level)):
            for i in range(self.count):
                for n in self.n_array[i]:
                    print("fix_count_of_raunds_for_cascade", n)
                    analizer = Analizer(n, self.p[i], self.e[i], self.confidence_level[level], self.averaging, fix_count_of_raunds_for_cascade)
                    array_e_p[level][i].append(analizer.RunCascade())
            for i in range(self.count):
                for n in self.n_array[i]:
                    print("fix_count_of_raunds_for_cascade", n)
                    analizer = Analizer(n, self.p[i], self.e[0], self.confidence_level[level], self.averaging, fix_count_of_raunds_for_cascade)
                    array_E_p[level][i].append(analizer.RunCascade())
            for i in range(self.count):
                for n in self.n_array[i]:
                    print("fix_count_of_raunds_for_cascade", n)
                    analizer = Analizer(n, self.p[0], self.e[i], self.confidence_level[level], self.averaging, fix_count_of_raunds_for_cascade)
                    array_e_P[level][i].append(analizer.RunCascade())
        return array_e_p, array_E_p, array_e_P

    def RunForCountOfRaundsForCascade(self, fix_confidence_level):
        array_e_p = [[[] for i in range(self.count)] for j in range(len(self.count_of_raunds_for_cascade))]
        array_E_p = [[[] for i in range(self.count)] for j in range(len(self.count_of_raunds_for_cascade))]
        array_e_P = [[[] for i in range(self.count)] for j in range(len(self.count_of_raunds_for_cascade))]
        for raund in range(len(self.count_of_raunds_for_cascade)):
            for i in range(self.count):
                for n in self.n_array[i]:
                    print("fix_confidence_level", n)
                    analizer = Analizer(n, self.p[i], self.e[i], fix_confidence_level, self.averaging, self.count_of_raunds_for_cascade[raund])
                    array_e_p[raund][i].append(analizer.RunCascade())
            for i in range(self.count):
                for n in self.n_array[i]:
                    print("fix_confidence_level", n)
                    analizer = Analizer(n, self.p[i], self.e[0], fix_confidence_level, self.averaging, self.count_of_raunds_for_cascade[raund])
                    array_E_p[raund][i].append(analizer.RunCascade())
            for i in range(self.count):
                for n in self.n_array[i]:
                    print("fix_confidence_level", n)
                    analizer = Analizer(n, self.p[0], self.e[i], fix_confidence_level, self.averaging, self.count_of_raunds_for_cascade[raund])
                    array_e_P[raund][i].append(analizer.RunCascade())
        return array_e_p, array_E_p, array_e_P