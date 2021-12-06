def dive():
    with open('input.txt') as f:
        data = f.read().splitlines()
    pos = {"hor": 0, "depth": 0}
    aim = 0
    for move in data:
        if move.split(" ")[0] == "down":
            aim += int(move.split(" ")[1])
        elif move.split(" ")[0] == "up":
            aim -= int(move.split(" ")[1])
        elif move.split(" ")[0] == "forward":
            pos["hor"] += int(move.split(" ")[1])
            pos["depth"] += int(move.split(" ")[1]) * aim

    print(pos["hor"] * pos["depth"])


if __name__ == "__main__":
    dive()
