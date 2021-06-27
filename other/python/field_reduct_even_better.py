def count_area(x, y, matrix):
  m = matrix[:]
  m.remove((x, y))
  min_x, min_y = min(m)[0], min(m, key=lambda p: p[1])[1]
  max_x, max_y = max(m)[0], max(m, key=lambda p: p[1])[1]
  return (max_x - min_x) * (max_y - min_y)

def solve(matrix):
  points = [min(matrix), min(matrix, key=lambda p: p[1]), max(matrix), max(matrix, key=lambda p: p[1])]  
  areas = [count_area(x, y, matrix) for x, y in points]
  return min(areas)

if __name__ == '__main__':
  with open('reduce.in') as f:
    n = int(f.readline())
    matrix = [tuple(map(int, line.split())) for line in f]
  result = solve(matrix)
  with open('reduce.out', 'w') as f:
    print(result, file=f)