from day1 import day1


def test_day1():
    with open("/home/jp/Code/AOC/2025/input/day1_1.txt", "r") as f:
        lines = f.readlines()
        assert day1(lines) == 3

    with open("/home/jp/Code/AOC/2025/input/day1_2.txt", "r") as f:
        lines = f.readlines()
        print(day1(lines))
        assert 0 == 0
