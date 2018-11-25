import random
import statistics
from median import median


def test_median():
    for size_a in range(1, 11):
        for size_b in range(1, 11):
            for _ in range(10):
                a = sorted(
                    [random.randint(-size_a // 2, size_a // 2) for _ in range(size_a)]
                )
                b = sorted(
                    [random.randint(-size_b // 2, size_b // 2) for _ in range(size_b)]
                )

                assert statistics.median(a + b) == median(a, b)

                a = sorted([random.random() for _ in range(size_a)])
                b = sorted([random.random() for _ in range(size_b)])
                assert statistics.median(a + b) == median(a, b)
