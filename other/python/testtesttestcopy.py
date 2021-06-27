from itertools import permutations
def winners(name_matrix):
  result = []
  for names in name_matrix:
    result.append(list(permutations(names, 3)))
  return result
# if __name__ == "__main__":
#   with open(0) as f:
#     m, n = map(int, f.readline().strip().split())
#     names = [line.strip().split() for line in f]   # [[str, str, str...], [str, str, str...], []]
#     result = winners(names) # [(), (), ...]
#     for i in result:
#       for j in range(len(i)):
#         if j == (n*(n-1))/2:
#           print("==========")
#       print(*result[i])
# # print(winners([["a", "b", "c", "d"], ["e", "f", "g", "h"]]))