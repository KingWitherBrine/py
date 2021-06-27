from itertools import permutations as perms

def valid_area(a, b, c):
  x1, y1 = a
  x2, y2 = b
  x3, y3 = c
  if x1 == x2 and y1 == y3 or x1 == x3 and y1 == y2:
    return abs(x2 - x3) * abs(y2 - y3)
  if x2 == x1 and y2 == y3 or x2 == x3 and y2 == y1:
    return abs(x1 - x3) * abs(y1 - y3)
  if x3 == x1 and y3 == y2 or x3 == x2 and y3 == y1:
    return abs(x1 - x2) * abs(y1 - y2)
  return 0

def solve(points):
  max_area = 0
  for a, b, c in perms(points, 3):
    max_area = max(valid_area(a, b, c), max_area)
  return max_area

if __name__ == '__main__':
  with open(0) as f:
    n = int(f.readline())
    points = [tuple(map(int, line.split())) for line in f]
  print(solve(points))