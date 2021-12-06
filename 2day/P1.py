def dive():
    with open('input.txt') as f:
        data = f.read().splitlines()
    legal_moves = {"down": 0, "forward": 0, "up": 0}
    for move in data:
        for key in legal_moves.keys():
            if key == move.split(" ")[0]:
                legal_moves[key] += int(move.split(" ")[1])
    depth = legal_moves['down'] - legal_moves['up']
    print(depth * legal_moves['forward'])


if __name__ == "__main__":
    dive()
