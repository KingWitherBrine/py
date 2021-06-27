def cow_gymnastics(rank, K, N):
  t = 0
  lst = []
  for a in range(len(rank)):
    for i in range(len(rank)):
      for j in range(i+1, len(rank)+1):
        lst.append((rank[a][i], rank[a][j]))
  for i in lst[:len(lst)//len(rank)]:
    if lst.count(i) == K:
      t += 1
  return t
print(cow_gymnastics([[4, 1, 3, 2], [4, 2, 1, 3], [4, 1, 2, 3]], 3, 4))

