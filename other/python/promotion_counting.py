def solve(bronze, silver, gold, platinum):
  a, b = bronze
  c, d = silver
  e, f = gold
  g, h = platinum
  platinum_result = h - g
  gold_result = (f - e) + platinum_result
  silver_result = (d - c) + gold_result
  return([platinum_result, gold_result, silver_result])

if __name__ == "__main__":
  with open(0) as f:
    bronze = list(map(int, f.readline().strip().split()))
    silver = list(map(int, f.readline().strip().split()))
    gold = list(map(int, f.readline().strip().split()))
    platinum = list(map(int, f.readline().strip().split()))
  print(*solve(bronze, silver, gold, platinum), sep="\n")
  # print(bronze, silver, gold, platinum)