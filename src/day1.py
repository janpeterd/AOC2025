def day1(lines):
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


with open("/home/jp/Code/AOC/2025/input/day1_2.txt", "r") as f:
    lines = f.readlines()
    print(day1(lines))
