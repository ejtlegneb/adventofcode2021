
# fix the being double
def loop_over_bits(data, pos, y, z):
    for i, bits in enumerate(data):
        pos[bits[y]].append(bits)
    if z == 0:
        x = pos["1"] if len(pos["1"]) < len(pos["0"]) else pos["0"]
    else:
        x = pos["1"] if len(pos["1"]) >= len(pos["0"]) else pos["0"]
    return x


def bin_diagnostics():
    with open("input.txt") as f:
        data = f.read().splitlines()
    filtered_bytes = data
    values = []
    for z in range(2):
        if z == 1:
            filtered_bytes = data
            y = 0
        for y in range(len(data[0])):
            pos = {"0": [], "1": []}
            filtered_bytes = loop_over_bits(filtered_bytes, pos, y, z)
            if len(filtered_bytes) == 1:
                break
            y += 1
        values.append(int(filtered_bytes[0], 2))
    print(values[0] * values[1])


if __name__ == "__main__":
    bin_diagnostics()
