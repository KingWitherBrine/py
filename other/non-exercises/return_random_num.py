import random
nums = input("Please enter some numbers seperated by spaces: \n")
nums = nums.split()
try:
    for i in nums:
        i = int(i)
    index = random.randint(0, len(nums) - 1)
    print("Here is your number!\n", nums[index])
except ValueError:
    if type(nums) != int:
        nums = input("What you entered is not a number, please try again: \n")
    nums = nums.split()
    index = random.randint(0, len(nums) - 1)
    
    print("Here is your number!\n", nums[index])