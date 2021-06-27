def solve(n, nums):
    for i in range(1, n + 1):
        possible_list = [i]
        for num in nums:
            possible_list.append(num - possible_list[-1])
            if sorted(possible_list) == list(range(1, n + 1)):
                return possible_list

if __name__ == "__main__":
    with open(0) as f:
        num = int(f.readline())
        nums = list(map(int, f.readline().strip().split()))
    print(*solve(num, nums))