def solve(a, b):
  x1, y1, x2, y2 = a
  x3, y3, x4, y4 = b
  a1, b1 = min(x1, x3), min(y1, y3)
  a2, b2 = max(x2, x4), max(y2, y4)
  max_side = max(max(a1, a2) - min(a1, a2), max(b1, b2) - min(b1, b2))
  return max_side ** 2

if __name__ == "__main__":
  with open(0) as f:
    a = list(map(int, f.readline().strip().split()))
    b = list(map(int, f.readline().strip().split()))
  print(solve(a, b))