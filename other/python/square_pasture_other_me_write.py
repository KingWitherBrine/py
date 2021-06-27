def solve(b1, b2):
  x1, y1, x2, y2 = b1
  x3, y3, x4, y4 = b2
  a1, b1 = min(x1, x3), min(y1, y3)
  a2, b2 = max(x2, x4), max(y2, y4)
  return max(a2-a1, b2-b1) ** 2

if __name__ == '__main__':
  with open('square.in') as f:
    b1, b2 = [list(map(int, line.strip().split())) for line in f]
  with open('square.out', 'w') as f:
    print(solve(b1, b2), file=f)