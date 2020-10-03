import unittest
from segment_tree import SegmentTree, Operation


class SegmentTreeTestCase(unittest.TestCase):
    def test_simple_sums(self):
        targetArray = [1, 2, 3, 4]
        cases = [(0, 1), (0, 2), (0, 3),
                 (1, 2), (1, 3)]
        good = [1, 3, 6, 2, 5]

        sTree = SegmentTree(targetArray, Operation(lambda x, y: x + y, 0))
        for case, good_answer in zip(cases, good):
            with self.subTest(case=case):
                self.assertEqual(sTree.calculate(case[0], case[1]), good_answer)

    def test_sums_with_update(self):
        targetArray = [1, 2, 3, 4]
        cases = [(0, 2), (1, 3)]
        good = [3, 5]

        sTree = SegmentTree(targetArray, Operation(lambda x, y: x + y, 0))
        for case, good_answer in zip(cases, good):
            with self.subTest(case=case):
                self.assertEqual(sTree.calculate(case[0], case[1]), good_answer)

        # updating
        sTree.update(0, 11)  # [1, 2, 3, 4] -> [11, 2, 3, 4]
        good_updated = [13, 5]
        for case, good_answer in zip(cases, good_updated):
            with self.subTest(case=case):
                self.assertEqual(sTree.calculate(case[0], case[1]), good_answer)


if __name__ == '__main__':
    unittest.main()
