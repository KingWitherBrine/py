from itertools import permutations
def winners(name_matrix):
  result = []
  for names in name_matrix:
    result.append(list(permutations(names, 3)))
  return result
if __name__ == "__main__":
  with open(0) as f:
    m, n = f.readline().strip().split() # 1 2
    names = [] # []
    for line in f:
      names.append(line) 
    print(names) # [[], [], []]
  result = winners(names) # [(), (), ()]
  for i in range(len(result)):
    if i != 0:
      print("==========")
    for j in result[i]:
      print(*j)