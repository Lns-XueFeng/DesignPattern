"""
Create time: 2023.08.17
Author: Lns-XueFeng
Goal: To master the common design pattern
"""


# 修饰器模式
# 该模式虽名为修饰器，但这并不意味着它应该只用于让产品看起来更漂亮。修饰器模式通常用于扩展一个对象的功能
import functools


def memoize(fn):
    known = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]

    return memoizer


@memoize
def nsum(n):
    '''返回前n个数字的和'''
    assert (n >= 0), 'n must be >= 0'
    return 0 if n == 0 else n + nsum(n - 1)


@memoize
def fibonacci(n):
    '''返回斐波那契数列的第n个数'''
    assert (n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)


from timeit import Timer

measure = [{'exec': 'fibonacci(100)', 'import': 'fibonacci',
            'func': fibonacci}, {'exec': 'nsum(200)', 'import': 'nsum',
                                 'func': nsum}]
for m in measure:
    t = Timer('{}'.format(m['exec']), 'from __main__ import{}'.format(m['import']))
    print('name: {}, doc: {}, executing: {}, time:{}'.format(m['func'].__name__, m['func'].__doc__, m['exec'],
                                                             t.timeit()))
