from itertools import permutations as perms

def area(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    if x3 == x1 and y3 == y2 or x3 == x2 and y3 == y1:
        return abs(x1-x2) * abs(y1-y2)
    if x2 == x1 and y2 == y3 or x2 == x3 and y2 == y1:
        return abs(x1-x3) * abs(y1-y3)
    if x1 == x2 and y1 == y3 or x1 == x3 and y1 == y2:
        return abs(x2-x3) * abs(y2-y3)
    return 0

def solve(points):
    max_area = 0
    for a, b, c in perms(points, 3):
        temp_area = area(a, b, c)
        if temp_area > max_area:
            max_area = temp_area
    return max_area

if __name__ == '__main__':
    with open('triangles.in', 'r') as f:
        n = int(f.readline())
        points = [tuple(map(int, line.split())) for line in f]
    with open('triangles.out', 'w') as f:
        print(solve(points), file=f)