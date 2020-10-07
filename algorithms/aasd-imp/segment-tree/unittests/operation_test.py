import unittest
from segment_tree import Operation


class OperationCase(unittest.TestCase):
    def test_init_and_call(self):
        def Sum(a: float, b: float) -> float:
            return a + b

        cases = [(1, 2), (3, 4)]
        good = [3, 7]
        op1 = Operation(Sum, 0)
        for case, good_answer in zip(cases, good):
            with self.subTest(case=case):
                self.assertEqual(op1(*case), good_answer)

    def test_call_and_get_neutral(self):
        op1 = Operation(lambda x, y: x + y, 0)
        op2 = Operation(lambda x, y: x * y, 1)

        self.assertEqual(op1.neutral, 0)
        self.assertEqual(op2.neutral, 1)


if __name__ == '__main__':
    unittest.main()
