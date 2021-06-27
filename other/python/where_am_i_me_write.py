def lost(s):
  for i in range(1, len(s)+1):
    if all(s[j:j+i] not in s[j+1:] for j in range(len(s)-i+1)):
      return i

if __name__ == "__main__":
  with open("whereami.in", "r") as f:
    length = f.readline()
    s = f.readline()
  with open("whereami.out", "w") as f:
    print(lost(s), file=f)