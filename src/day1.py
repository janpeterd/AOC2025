def day1_part1(lines):
    start = 50
    result = 0
    rotations = []
    for line in lines:
        rotation = (line.strip()[0:1], int(line.strip()[1:]))
        rotations.append(rotation)
    print(f"{rotations=}")

    for direction, amount in rotations:
        if direction.lower() == "l":
            print("Left")
            start -= amount
        else:
            print("Right")
            start += amount
        start %= 100
        if start == 0:
            result += 1

    print(f"{start=}")
    print(f"{result=}")
    return result


def day1_part2(lines):
    def zeros_hit_right(position, clicks):
        steps_to_zero = (100 - position) % 100 or 100
        if clicks < steps_to_zero:
            return 0
        return 1 + (clicks - steps_to_zero) // 100

    def zeros_hit_left(position, clicks):
        steps_to_zero = position or 100
        if clicks < steps_to_zero:
            return 0
        return 1 + (clicks - steps_to_zero) // 100

    start = 50
    result = 0
    rotations = []
    for line in lines:
        rotation = (line.strip()[0:1], int(line.strip()[1:]))
        rotations.append(rotation)
    print(f"{rotations=}")

    for direction, amount in rotations:
        if direction.lower() == "l":
            print("Left")
            result += zeros_hit_left(start, amount)
            start = (start - amount) % 100
        else:
            print("Right")
            result += zeros_hit_right(start, amount)
            start = (start + amount) % 100

    print(f"{start=}")
    print(f"{result=}")
    return result


with open("/home/jp/Code/AOC2025/input/day1_2.txt", "r") as f:
    lines = f.readlines()
    print(day1_part2(lines))
