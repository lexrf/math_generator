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

if __name__ == '__main__':
    l = [(plus_in_20_a, 20), (plus_in_20_b, 20), (plus_in_20_c, 20), (minus_in_20_a, 20), (minus_in_20_b, 20)]
    for t, n in l:
        for x in xrange(1, n):
            t()

