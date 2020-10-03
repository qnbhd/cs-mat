import unittest
from segment_tree import HalfInterval


class HalfIntervalTestCase(unittest.TestCase):
    def test_intersections(self):
        cases = [(HalfInterval(1, 2), HalfInterval(2, 3)),
                 (HalfInterval(1, 5), HalfInterval(1, 5)),
                 (HalfInterval(2, 5), HalfInterval(3, 7))]
        good = [HalfInterval.Intersection.NONE, HalfInterval.Intersection.FULLINTERSECT, HalfInterval.Intersection.INTERSECT]

        for case, good_answer in zip(cases, good):
            with self.subTest(case=case):
                self.assertEqual(case[0].intersection(case[1]), good_answer)


if __name__ == '__main__':
    unittest.main()
