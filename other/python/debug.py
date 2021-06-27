def solve(num):
    for n in num:
        for i in n:
            temp = i ** 2
            print(temp) 

if __name__ == "__main__":
  with open(0) as f:
    nums = [list(map(int, line.strip().split())) for line in f]
  solve(nums)