"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$

# TODO: Implement for Task 0.1.

def mul(x: float, y: float) -> float:
    return x * y

def id(x: float) -> float:
    return x

def add(x: float, y: float) -> float:
    return x + y

def neg(x: float) -> float:
    return -x

def lt(x: float, y: float) -> bool:
    return x < y

def eq(x: float, y: float) -> bool:
    return x == y

def max(x: float, y: float) -> float:
    return x if x > y else y

def is_close(x: float, y: float) -> bool:
    return abs(x - y) < 1e-2

def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x)) if x >= 0 else math.exp(x) / (1.0 + math.exp(x))

def relu(x: float) -> float:
    return max(0, x)

def log(x: float) -> float:
    return math.log(x)

def exp(x: float) -> float:
    return math.exp(x)

def log_back(x: float, b: float) -> float:
    return b / x

def inv(x: float) -> float:
    return 1.0 / x

def inv_back(x: float, b:float) -> float:
    return -b / (x * x)

def relu_back(x: float, b: float) -> float:
    return b if x > 0 else 0.0




# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.

def map(f: Callable[[float], float], xs: Iterable[float]) -> Iterable[float]:
    '''
    将给定的函数应用于给定的可迭代对象的每个元素。
    即对可迭代对象中的每个元素执行相同的操作，返回一个新的可迭代对象。
    '''
    return [f(x) for x in xs]

def zipWith(f: Callable[[float, float], float], xs: Iterable[float], ys: Iterable[float]) -> Iterable[float]:
    '''
    将给定的函数应用于给定的两个可迭代对象的对应元素。
    即对两个可迭代对象中的对应元素执行相同的操作，返回一个新的可迭代对象。
    '''
    return [f(x, y) for x, y in zip(xs, ys)]

def reduce(f: Callable[[float, float], float], xs: Iterable[float], init: float) -> float:
    '''
    将给定的函数应用于给定的可迭代对象的所有元素。
    即对可迭代对象中的所有元素执行相同的操作，返回一个新的值。
    '''
    return init if not xs else reduce(f, xs[1:], f(init, xs[0]))

def negList(xs: Iterable[float]) -> Iterable[float]:
    return map(neg, xs)

def addLists(xs: Iterable[float], ys: Iterable[float]) -> Iterable[float]:
    return zipWith(add, xs, ys)

def sum(xs: Iterable[float]) -> float:
    return reduce(add, xs, 0.0)

def prod(xs: Iterable[float]) -> float:
    return reduce(mul, xs, 1.0)