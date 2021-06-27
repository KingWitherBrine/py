def solve(x, y, m):
  max_num = 0
  for i in range(m+1):
    for j in range(m+1):
      if (x * i + y * j) <= m:
        if (x * i + y * j) > max_num:
          max_num = (x * i + y * j)
  return max_num

if __name__ == '__main__':
  # with open('pails.in', 'r') as f:
  #   x, y, m = map(int, f.readline().strip().split())
  # with open('pails.out', 'w') as f:
  #   f.write(str(solve(x, y, m)))
  with open(0) as f:
    x, y, m = map(int, f.readline().strip().split())
  print(solve(x, y, m))