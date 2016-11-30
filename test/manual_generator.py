# -*- coding: utf-8 -*-
# Created by Lex.Lei on 2016/11/29

import random


def minus_in_20_a():
    a = int(random.uniform(0, 20))
    b = int(random.uniform(0,a))
    print a, "- (  ) = ", b


def minus_in_20_b():
    a = int(random.uniform(0, 20))
    b = int(random.uniform(0, 20 - a))
    print "(  ) - ", a, "=", b


def plus_in_20_b():
    a = int(random.uniform(0, 20))
    b = int(random.uniform(0, a))
    print "(   ) +", b, " = ", a


def plus_in_20_c():
    a = int(random.uniform(0, 20))
    b = int(random.uniform(0, a))
    print b, "+(   )", " = ", a


def plus_in_20_a():
    a = int(random.uniform(0, 20))
    b = int(random.uniform(0, 20 - a))
    print a, "+ ", b, " = (   )"


def continue_plus_in_20_a():
    a = int(random.uniform(0, 20))
    b = int(random.uniform(0, 20-a))
    c = int(random.uniform(0, 20-a-b))
    print a, "+", b, "+", c, "=(  )"


def continue_plus_in_20_b():
    a = int(random.uniform(0, 20))
    b = int(random.uniform(0, 20-a))
    c = int(random.uniform(20-a-b, 20))
    print a, "+", b, "+", "(  )=",  c


def continue_plus_in_20_c():
    a = int(random.uniform(0, 20))
    b = int(random.uniform(0, 20-a))
    c = int(random.uniform(20-a-b, 20))
    print "(  )+", a, "+", b, "=",  c


def continue_plus_in_20_d():
    a = int(random.uniform(0, 20))
    b = int(random.uniform(0, 20-a))
    c = int(random.uniform(20-a-b, 20))
    print a, "+", "(  )+", b, "=",  c


def continue_minus_in_20_a():
    a = int(random.uniform(0, 20))
    b = int(random.uniform(0, a))
    c = int(random.uniform(0, a-b))
    print a, "-", b, "-", c, "=(  )"


if __name__ == '__main__':
    l = [(minus_in_20_b, 10),
         (minus_in_20_a, 5),
         (plus_in_20_b, 5),
         (plus_in_20_c, 5),
         (continue_plus_in_20_a, 15),
         (continue_plus_in_20_b, 15),
         (continue_plus_in_20_c, 15),
         (continue_plus_in_20_d, 15),
         (continue_minus_in_20_a, 15)]
    for t, n in l:
        for x in xrange(1, n):
            t()

