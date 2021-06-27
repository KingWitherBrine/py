from itertools import permutations as perms

def solve(matrix):
  areas = []
  for i in perms(matrix, 3):
    results = is_right_triangle(i)
    if results[0] is not None:
      x1, y1 = results[1]
      x2, y2 = results[2]
      areas.append(area([x1, y1, x2, y2]))
    areas.append(0)
  return max(areas)

def area(matrix):
  x1, y1, x2, y2 = matrix
  area = abs(x2-x1) * abs(y2-y1)
  return area

def is_right_triangle(perm):
  p1, p2, p3 = perm
  x1, y1 = p1
  x2, y2 = p2
  x3, y3 = p3
  right_angle_point = []
  if (x1 == x2 and y1 == y3):
    right_angle_point, x_same, y_same = p1, p2, p3
  if (x1 == x3 and y1 == y2):
    right_angle_point, x_same, y_same = p1, p3, p2
  if (x1 == x2 and y2 == y3):
    right_angle_point, x_same, y_same = p2, p1, p3
  if  (x2 == x3 and y1 == y2):
    right_angle_point, x_same, y_same = p2, p3, p1
  if (x1 == x3 and y2 == y3):
    right_angle_point, x_same, y_same = p3, p1, p2
  if (x2 == x3 and y1 == y3):
    right_angle_point, x_same, y_same = p3, p2, p1
  else:
    right_angle_point, x_same, y_same = None, None, None
  return right_angle_point, x_same, y_same
  # if (x1 == x2 and y1 == y3) or (x1 == x2 and y2 == y3) or (x1 == x3 and y1 == y2) or (x1 == x3 and y2 == y3) or (x2 == x3 and y1 == y3) or (x2 == x3 and y1 == y2):

if __name__ == "__main__":
  with open(0) as f:
    num_lines = int(f.readline())
    matrix = [list(map(int,f.readline().strip().split())) for _ in range(num_lines)]
  print(solve(matrix))