def solve(n, nums):
    for i in range(1, nums[0]):
        possible_sol = [i]
        check_duplicates = {i}
        for num in nums:
            next_num = num - possible_sol[-1]
            possible_sol.append(next_num)
            if next_num in check_duplicates or next_num not in range(1, n+1):
                break
            check_duplicates.add(next_num)
        if len(possible_sol) == n:
            return possible_sol

if __name__ == "__main__":
    with open('photo.in', 'r') as f:
        num = int(f.readline())
        nums = list(map(int, f.readline().strip().split()))
    with open('photo.out', 'w') as f:
        print(*solve(num, nums), file=f)