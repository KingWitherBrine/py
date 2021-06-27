def friday(val, b1, b2, b1_val):
    for bucket in b2:
        b1_val.add(val+bucket)

def thursday(val, b1, b2, b1_val):
    for i in range(len(b1)):
        friday(val-b1[i], b1[:i] + b1[i+1:], b2 + [b1[i]], b1_val)

def wednesday(val, b1, b2, b1_val):
    for i in range(len(b2)):
        thursday(val+b2[i], b1 + [b2[i]], b2[:i] + b2[i+1:], b1_val)

def tuesday(val, b1, b2, b1_val):
    for i in range(len(b1)):
        wednesday(val-b1[i], b1[:i] + b1[i+1:], b2 + [b1[i]], b1_val)

def back_and_forth(b1, b2):
  b1_val = set()
  tuesday(1000, b1, b2, b1_val)
  return len(b1_val)

if __name__ == "__main__":
    with open('backforth.in', 'r') as f:
        b1 = list(map(int, f.readline().strip().split()))
        b2 = list(map(int, f.readline().strip().split()))
    with open('backforth.out', 'w') as f:
        print(back_and_forth(b1, b2), file=f)
