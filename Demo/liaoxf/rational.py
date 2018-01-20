#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 有理数的四则运算


class Rational:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.gys = Rational.gcb(p, q)

    @classmethod
    def gcb(cls, a, b):
        while b:
            a, b = b, a % b

        return a

    def __str__(self):
        a, b = self.p, self.q
        while b:
            a, b = b, a % b
        return "%s/%s" % (self.p / a, self.q / a)

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __truediv__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

r1 = Rational(1, 2)
r2 = Rational(1, 4)

print(Rational.gcb(49, 35))

print(r1 + r2)
print(r1 - r2)
print(r1 * r2)
print(r1 / r2)
