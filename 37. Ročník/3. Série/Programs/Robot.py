output = open("../Solution", "w")
lines = open("../Inputs/05.in").read().split("\n", 1)
height, width = tuple(map(int, lines[0].split()))
start_index = lines[1].index("V")
start_pos = (start_index % (width+1), start_index//(width+1))
warehouse = list(map(list, lines[1].splitlines()))


def find(pos, p_pos):
    global warehouse, end
    if warehouse[pos[1]][pos[0]] == "V" and p_pos != (-1, -1):
        return
    elif warehouse[pos[1]][pos[0]] == "P":
        warehouse[pos[1]][pos[0]] = "A"
    neighbours = []
    dx, dy = 1, 0
    for _ in range(4):
        x, y = pos[0]+dx, pos[1]+dy
        if 0 <= x < width and 0 <= y < height and warehouse[y][x] != "#":
            neighbours.append((x, y))
        temp = dy
        dy = -1*dx
        dx = temp
    if len(neighbours) <= 2:
        for neighbour in neighbours:
            if neighbour != p_pos:
                find(neighbour, pos)
    else:
        print(pos)
        end = None
        if p_pos != (-1, -1) and all([split(neighbour, pos) for neighbour in neighbours if neighbour != p_pos]):
            warehouse[end[1]][end[0]] = "A"
        elif [split(neighbour, pos) for neighbour in neighbours if neighbour != p_pos].count(False) <= 1:
            warehouse[end[1]][end[0]] = "A"


def split(pos, p_pos):
    global end
    neighbours = []
    dx, dy = 1, 0
    for _ in range(4):
        x, y = pos[0] + dx, pos[1] + dy
        if 0 <= x < width and 0 <= y < height and warehouse[y][x] != "#":
            neighbours.append((x, y))
        temp = dy
        dy = -1 * dx
        dx = temp
    if len(neighbours) == 2:
        for neighbour in neighbours:
            if neighbour != p_pos and split(neighbour, pos):
                return True
    elif end is None and warehouse[pos[1]][pos[0]] == "P":
        end = pos
        return True
    elif pos == end:
        return True
    return False


end = None
find(start_pos, (-1, -1))
for line in warehouse:
    for tile in line:
        if tile == "P":
            print("N", end="", file=output)
        elif tile == "A":
            print("A", end="", file=output)
print()
