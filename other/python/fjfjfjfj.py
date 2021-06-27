def b_lst(lst):
  buckets = [0] * 1000
  for i in range(1000):
    for s, t, b in lst:
      if t >= i >= s:
        buckets[i] += b
  return max(buckets)
if __name__ == "__main__":
  with open(0) as f:
    n = int(f.readline())
    lst = [list(map(int, line.strip().split())) for line in f]
    print(b_lst(lst))