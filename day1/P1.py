def sonar_sweep():
    with open('input.txt') as f:
        data = f.read().splitlines()
    nbrs = [int(i) for i in data]
    counter = 0
    for b, a in zip(nbrs, nbrs[1:]):
        if a > b:
            counter += 1
    print(counter)


if __name__ == "__main__":
    sonar_sweep()
