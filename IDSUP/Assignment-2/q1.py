from typing import List
import math
vector = List[float]

def vector_add(v: vector, w: vector) -> vector:
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v, w)]
print(vector_add([1,2,3], [4,5,6]))

def vector_sub(v: vector, w: vector) -> vector:
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]
print(vector_sub([5,6,7], [2,3,4]))


def scalar_multiply(c: float, v: vector) -> vector:
    return [c * v_i for v_i in v]
print(scalar_multiply(3, [2,3,4]))

def dot_product(v: vector, w: vector) -> vector:
    return sum(i*j for i, j in zip(v, w))
print(dot_product([1,2,3], [2,3,4]))

def length_of_vector(v: vector) -> vector:
    return math.sqrt(sum(i*i for i in v))
print(length_of_vector([2,2]))