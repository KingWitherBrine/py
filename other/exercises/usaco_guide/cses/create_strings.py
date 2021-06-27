from itertools import permutations as perms

if __name__ == "__main__":
    with open(0) as f:
        s = f.readline().strip()
    perms_s = sorted(set(list(perms(s))))
    print(len(perms_s))
    for i in perms_s:
        print("".join(i))