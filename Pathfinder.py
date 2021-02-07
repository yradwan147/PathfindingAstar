import math

grid = []
for i in range(16):
    grid.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
MAX = 15

start_x = input("Please input start point x position: ")
start_y = input("Please input start point y position: ")
grid[int(start_y) - 1][int(start_x) - 1] = 1
end_x = input("Please input end point x position: ")
end_y = input("Please input end point y position: ")
grid[int(end_y) - 1][int(end_x) - 1] = 2

def print_grid():
    for x in range(0, len(grid)):
        print(grid[x])

def find_element(element):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == element:
                position = [y, x]
                return position

def distance(x1 , y1):
    ##print(x1,y1)
    return math.sqrt((abs(x1[0] - y1[0]))^2 + abs((x1[1] - y1[0]))^2)

def f_cost(point):
    return distance(point, find_element(1)) + distance(point, find_element(2))

def neighbor_list(i):
    neighbors = [[i[0] - 1, i[1] - 1], [i[0] - 1, i[1]], [i[0] - 1, i[1] + 1],
                 [i[0], i[1] - 1], [i[0], i[1] + 1],
                 [i[0] + 1, i[1] - 1], [i[0] + 1, i[1]], [i[0] + 1, i[1] + 1]]
    invalid = []
    for i in neighbors:
        for j in range(2):
            if i[j] < 0 or i[j] > MAX:
                invalid.append(i)
    for k in invalid:
        if k in neighbors:
            neighbors.remove(k)
    print(neighbors)
    return neighbors

OPEN = []
CLOSED = []
OPEN.append(find_element(1))

while True:
    f_values = []
    for i in OPEN:
        f_values.append(f_cost(i))
        if f_cost(i) == min(f_values):
            current = i
    OPEN.remove(current)
    CLOSED.append(current)

    if current == find_element(2):
        print("\n" + str(CLOSED))
        for i in CLOSED:
            if i == find_element(1) or i == find_element(2):
                continue
            grid[i[0]][i[1]] = 5
        print_grid()
        break

    for l in neighbor_list(current):
        ##print(l)
        if grid[l[0]][l[1]] == 3 or l in CLOSED:
            continue
        elif l not in OPEN:
            OPEN.append(l)