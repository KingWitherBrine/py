def area(a, b, matrix):
  new_matrix = matrix[:]
  new_matrix.remove((a, b))
  min_x, min_y = min(new_matrix)[0], min(new_matrix, key=lambda p: p[1])[1]
  max_x, max_y = max(new_matrix)[0], max(new_matrix, key=lambda p: p[1])[1]
  return (max_x-min_x) * (max_y-min_y)

def solve(matrix):
  points = [min(matrix), min(matrix, key=lambda p: p[1]), max(matrix), max(matrix, key=lambda p: p[1])]
  return min([area(a, b, matrix) for a, b in points])

if __name__ == '__main__':
  with open('reduce.in') as f:
    n = int(f.readline())
    matrix = [tuple(map(int, line.split())) for line in f]
  result = solve(matrix)
  with open('reduce.out', 'w') as f:
    print(result, file=f)