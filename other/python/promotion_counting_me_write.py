def solve(matrix):
  platinum = matrix[3][1] - matrix[3][0]
  gold = matrix[2][1] - matrix[2][0] + platinum
  silver = matrix[1][1] - matrix[1][0] + gold
  return silver, gold, platinum

if __name__ == '__main__':
  with open('promote.in') as f:
    matrix = [list(map(int, line.strip().split())) for line in f]
  solve(matrix)
  with open('promote.out', 'w') as f:
    print(*solve(matrix), sep='\n', file=f)