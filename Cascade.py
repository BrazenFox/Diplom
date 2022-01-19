import math
from math import log
from random import randint, random, choice, shuffle, gauss, normalvariate
import numpy as np
from functools import reduce
import scipy.special
from scipy.stats import binom
import seaborn as sb
import matplotlib.pyplot as plt
import os


class Cascade:
    def __init__(self, a, b, p, count_of_rounds):
        self.a = a
        self.b = b
        self.n = len(a)
        self.p = p
        self.count_of_rounds = count_of_rounds
        self.w = self.select_w(p)
        self.cascade_blocks = self.fill_cascade_blocks()
        self.iter = 0

    def start(self):
        for i in range(self.count_of_rounds):
            self.pass_i(i)
        return self.number_bit_error()

    def pass_i(self, raund):
        for i in self.cascade_blocks[raund]:
            block_A, block_B = self.fill_blocks(i)
            if self.equals_parity(block_A, block_B):
                bit_error = self.binary_search(block_A, block_B)
                self.b[bit_error] ^= 1
                if raund > 0:
                    self.BK(bit_error, raund)

    def BK(self, bit_error, raund):
        K = self.find_blocks_with_l(raund + 1, bit_error)
        K_min = self.min_K(K)
        bit_error1 = self.binary_search(K_min[0], K_min[1])
        self.b[bit_error1] ^= 1
        B = self.find_blocks_with_l(raund + 1, bit_error1)
        if B != []:
            self.BK(bit_error1, raund)

    def find_blocks_with_l(self, round, l):
        blocks = []
        for i in range(round):
            for j in self.cascade_blocks[i]:
                if j.__contains__(l):
                    Block_A, Block_B = self.fill_blocks(j)
                    if self.equals_parity_on_Bob(Block_A, Block_B):
                        blocks.append(self.fill_blocks(j))
        return blocks

    def min_K(self, K):
        k = K[0]
        for i in K:
            k = i if len(i[1]) < len(k[1]) else k
        return k

    def fill_blocks(self, block):
        block_A = []
        block_B = []
        for i in block:
            block_A.append([self.a[i], i])
            block_B.append([self.b[i], i])
        return block_A, block_B

    def select_w(self, p):
        w = 2
        while ((1 - 2 * p) ** w + 2 * w * p <= log(2) + 1):
            w += 1
        w = max(w - 1, 2)
        return w

    def fill_cascade_blocks(self):
        K = [0] * self.count_of_rounds
        w = self.w
        for raund in range(self.count_of_rounds):
            count_of_blocks = math.ceil(self.n / w)

            blocks = [[] for j in range(count_of_blocks)]
            numbers = [j for j in range(self.n)]
            if raund == 0:
                for j in range(self.n):
                    blocks[int(j // w)].append(j)
            else:
                shuffle(numbers)
                ww = math.ceil(self.n / count_of_blocks)
                delimetr=[]
                for i in range(1, count_of_blocks):
                    num = i * ww + randint(-ww // 4, ww // 4)
                    num = i * ww if num >= self.n - ww // 4 else num
                    delimetr.append(num)
                delimetr = [0] + delimetr + [self.n]
                for i in range(count_of_blocks):
                    blocks[i] = numbers[delimetr[i]:delimetr[i + 1]]
            K[raund] = blocks
            w = 2 * w
        return K

    def parity(self, block):
        return reduce(lambda x, y: x ^ y, [j[0] for j in block])

    def equals_parity(self, a, b):
        # print(a, b)
        self.iter += 1
        return self.parity(a) != self.parity(b)

    def equals_parity_on_Bob(self, a, b):
        return self.parity(a) != self.parity(b)

    def binary_search(self, a, b):
        if (len(b) == 1):
            return b[0][1]
        l = math.ceil(len(a) / 2)
        if self.equals_parity(a[:l], b[:l]):
            return self.binary_search(a[:l], b[:l])
        else:
            return self.binary_search(a[l:], b[l:])

    def number_bit_error(self):
        biterror = 0
        for i in range(self.n):
            biterror += self.a[i] ^ self.b[i]
        return biterror
