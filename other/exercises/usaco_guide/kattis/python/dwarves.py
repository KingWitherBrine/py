from itertools import permutations as perms

def solve(nums):
    for i in perms(nums, 7):
        if sum(i) == 100:
            return i

if __name__ == "__main__":
    with open(0) as f:
        nums = [int(f.readline().strip()) for i in range(9)]
    for i in solve(nums):
        print(i)