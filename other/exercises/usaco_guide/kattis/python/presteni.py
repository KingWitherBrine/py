from math import gcd

def solve(radii):
    lst = []
    for i in range(len(radii)):
        lst.append(gcd(f"{radii[0]}/{radii[i]}"))
    return lst
                

if __name__ == "__main__":
    with open(0) as f:
        n = int(f.readline().strip())
        radii = list(map(int, f.readline().strip().split()))
    print(solve(radii))