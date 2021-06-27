def friday(value, b1, b2, barn1_value):
  for b in b2:
    barn1_value.add(value + b)

def thursday(value, b1, b2, barn1_value):
  for i in range(len(b1)):
    friday(value - b1[i], b1[:i] + b1[i+1:], b2 + [b1[i]], barn1_value)

def wednesday(value, b1, b2, barn1_value):
  for i in range(len(b2)):
    thursday(value + b2[i], b1 + [b2[i]], b2[:i] + b2[i+1:], barn1_value)
    
def tuesday(value, b1, b2, barn1_value):
  for i in range(len(b1)):
    wednesday(value - b1[i], b1[:i] + b1[i+1:], b2 + [b1[i]], barn1_value)

def back_and_forth(b1, b2):
  barn1_value = set()
  tuesday(1000, b1, b2, barn1_value)
  return len(barn1_value)

if __name__ == "__main__":
  with open(0) as f:
    b1 = list(map(int, f.readline().strip().split()))
    b2 = list(map(int, f.readline().strip().split()))
  print(back_and_forth(b1, b2))



# if __name__ == "__main__":
  # with open(0) as f:
  #   b1_c = list(map(int, f.readline().strip().strip().split()))
  #   b2_c = list(map(int, f.readline().strip().strip().split()))
  #   truck_c = f.readline().strip().split()
  #   lst1 = []
  #   lst2 = []
  #   for i in range(0, (len(b1_c)), 2):
  #     lst1.append((b1_c[i], b1_c[i+1]))
  #   for i in range(0, (len(b2_c)), 2):
  #     lst2.append((b2_c[i], b2_c[i+1]))
  #   print(lst1, lst2)