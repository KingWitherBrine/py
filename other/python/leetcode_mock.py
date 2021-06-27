def area(nums):
  x1, y1, x2, y2 = nums
  return (x2 - x1) * (y2 - y1)

def intersect(num1, num2):
    x1, y1, x2, y2 = num1
    x3, y3, x4, y4 = num2
    a1, b1 = max(x1, x3), max(y1, y3)
    a2, b2 = min(x2, x4), min(y2, y4)
    return 0 if a2 < a1 or b2 < b1 else area([a1, b1, a2, b2])

def solve(num1, num2):
    if intersect(num1, num2) != 0:
        return "true"
    return "false"

if __name__ == "__main__":
    print(solve([0,0,1,1], [1,0,2,1]))