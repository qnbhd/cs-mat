from typing import Callable, List
from enum import Enum


class Operation:

    def __init__(self, bin_op: Callable[[float, float], float], neutral):
        self.op = bin_op
        self.neutral = neutral

    def __call__(self, *args, **kwargs):
        return self.op(args[0], args[1])

    def get_neutral(self) -> float:
        return self.neutral


class HalfInterval:
    class Intersection(Enum):
        NONE = 0,
        FULLINTERSECT = 1,
        INTERSECT = 2

        def __str__(self):
            return self.name

        def __repr__(self):
            return self.__str__()

    def __init__(self, left_bound, right_bound):
        self.L = left_bound
        self.R = right_bound

    def __str__(self):
        return f'[{self.L}, {self.R})'

    def __repr__(self):
        return self.__str__()

    def intersection(self, half_interval) -> Intersection:
        """
        :param half_interval: get self and half_interval intersection
        :return: 0 if not intersection, 1 if self full in half_interval, 2 if exist intersection
        """
        if self.L >= half_interval.L and self.R <= half_interval.R:
            return HalfInterval.Intersection.FULLINTERSECT
        if half_interval.L >= self.R or half_interval.R <= self.L:
            return HalfInterval.Intersection.NONE
        return HalfInterval.Intersection.INTERSECT


# recursive
class SegmentTree:

    def __init__(self, array: List[float], operation: Operation):
        self.tree = [0.0] * 2 * len(array)
        self.length = len(array)
        self.operation = operation
        self.__build(array, 0, 0, self.length)
        print(self.tree)

    def __build(self, input_array, idx, temp_left_bound, temp_right_bound):
        if temp_right_bound - temp_left_bound == 1:
            self.tree[idx] = input_array[temp_left_bound]
        else:
            middle = (temp_left_bound + temp_right_bound) // 2
            self.__build(input_array, 2 * idx + 1, temp_left_bound, middle)
            self.__build(input_array, 2 * idx + 2, middle, temp_right_bound)
            result = self.operation(self.tree[2 * idx + 1], self.tree[2 * idx + 2])
            self.tree[idx] = result

    def __calculate(self, idx: int, temp_left_bound: int, temp_right_bound: int,
                    left_bound: int, right_bound: int) -> float:

        tempHI = HalfInterval(temp_left_bound, temp_right_bound)
        HI = HalfInterval(left_bound, right_bound)

        if tempHI.intersection(HI) == HalfInterval.Intersection.NONE:
            return self.operation.neutral
        if tempHI.intersection(HI) == HalfInterval.Intersection.FULLINTERSECT:
            return self.tree[idx]

        middle = (temp_left_bound + temp_right_bound) // 2
        left_res = self.__calculate(2 * idx + 1, temp_left_bound, middle, left_bound, right_bound)
        right_res = self.__calculate(2 * idx + 2, middle, temp_right_bound, left_bound, right_bound)

        return self.operation(left_res, right_res)

    def calculate(self, left: int, right: int) -> float:
        return self.__calculate(0, 0, self.length, left, right)

    def __update(self, idx, temp_left_bound, temp_right_bound, pos, new_val):
        if temp_right_bound - temp_left_bound == 1:
            self.tree[idx] = new_val
        else:
            middle = (temp_left_bound + temp_right_bound) // 2
            if pos <= middle:
                self.__update(2 * idx + 1, temp_left_bound, middle, pos, new_val)
            else:
                self.__update(2 * idx + 2, middle, temp_right_bound, pos, new_val)
            self.tree[idx] = self.operation(self.tree[2 * idx + 1], self.tree[2 * idx + 2])

    def update(self, pos, new_val):
        self.__update(0, 0, self.length, pos, new_val)
