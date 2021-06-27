def solve(x, y, m):
  lst = []
  for i in range(m+1):
    for j in range(m+1):
      if (x * i + y * j) <= m:
        lst.append(x * i + y * j)
  return max(lst)

if __name__ == '__main__':
  with open('pails.in', 'r') as f:
    x, y, m = map(int, f.readline().strip().split())
  with open('pails.out', 'w') as f:
    f.write(str(solve(x, y, m)))