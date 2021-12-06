def bin_diagnostics():
    with open("input.txt") as f:
        data = f.read().splitlines()
    gamma = 0
    total = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0}
    length = len(data)
    for bits in data:
        for x in range(len(bits)):
            total[str(x)] += int(bits[x])

    gamma = 0
    for count in total.values():
        if count > length / 2:
            gamma = gamma << 1 | 1
        else:
            gamma = gamma << 1

    epsilon = (~gamma & 0xFFF)

    print(epsilon * gamma)


if __name__ == "__main__":
    bin_diagnostics()
