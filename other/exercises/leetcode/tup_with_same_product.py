from itertools import combinations as combs
from itertools import permutations as perms

def solve(nums):
    count = 0
    for i in set(perms(nums, 4)):
        if i[0] * i[1] == i[2] * i[3]:
            count += 1
    return count
if __name__ == "__main__":
    print(solve([2,3,4,6,8,12]))