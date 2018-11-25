import random


def generate_array(m, n):
    s = ""
    for i in range(m):
        for j in range(n):
            s += str(random.choice((0, 1))) + " "
        s += "\n"

    return s


def largest_at(i, j, m, n, array, seen):
    seen.add((i, j))
    current = array[i][j]
    adjacent = []
    if i > 0:
        adjacent.append((i - 1, j))
    if i < m - 1:
        adjacent.append((i + 1, j))
    if j > 0:
        adjacent.append((i, j - 1))
    if j < n - 1:
        adjacent.append((i, j + 1))
    connected = []
    coordinates = {(i, j)}
    for i, j in adjacent:
        if (i, j) not in seen and array[i][j] == current:
            size, coords = largest_at(i, j, m, n, array, seen)
            connected.append(size)
            coordinates.update(coords)
    return sum(connected) + 1, coordinates


def largest(array_string):
    array = []
    for row in array_string.strip().split("\n"):
        array.append(row.split())
    m = len(array)
    n = len(array[0])
    max_size = 0
    seen = set()
    for i in range(m):
        for j in range(n):
            if (i, j) not in seen:
                size, connected = largest_at(i, j, m, n, array, seen)
                if size > max_size:
                    max_size = size
                    max_connected = connected
    return array, max_size, max_connected


def print_connected(array, coords):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if (i, j) in coords:
                print(f"\x1b[31m{ array[i][j] }\x1b[0m", end=" ")
            else:
                print(array[i][j], end=" ")
        print()


s = generate_array(10, 10)
print(s)
array, size, coordinates = largest(s)


print_connected(array, coordinates)
