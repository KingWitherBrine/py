def largest_interior_gap(s):
  max_gap_start, current_start = 0, -1
  gap = 0
  for i in range(len(s)):
    if s[i] == '1':
      if current_start != -1 and i - current_start > gap:
        gap = i - current_start
        max_gap_start = current_start
      current_start = i
  return gap, max_gap_start

def smallest_interior_gap(s):
  current_start = -1
  gap = len(s) - 1  # the max possible interior gap
  for i in range(len(s)):
    if s[i] == '1':
      if current_start != -1:
        gap = min(gap, i - current_start)
      current_start = i
  return gap

def put_cow_in_largest_interior_gap(s):
  gap, gap_start = largest_interior_gap(s)
  if gap >= 2:
    s[gap_start + gap // 2] = '1'
    return smallest_interior_gap(s)
  return 0  # No gap

def solve(s):
  answer = 0
  # case 1: place the two cow in same the interior gap
  gap, gap_start = largest_interior_gap(s)
  if gap >= 3:
    temp_s = list(s)
    temp_s[gap_start + gap // 3] = '1'
    temp_s[gap_start + gap // 3 * 2] = '1'
    answer = max(answer, smallest_interior_gap(temp_s))
  # case 2: 1 cow at left end + 1 cow in the interior largest gap
  if s[0] == '0':
    temp_s = list(s)
    temp_s[0] = '1'
    answer = max(answer, put_cow_in_largest_interior_gap(temp_s))
  # case 3: 1 cow at right end + 1 cow in the interior largest gap
  if s[-1] == '0':
    temp_s = list(s)
    temp_s[-1] = '1'
    answer = max(answer, put_cow_in_largest_interior_gap(temp_s))
  # case 4: 1 cow at left end + 1 cow at right end
  if s[0] == '0' and s[-1] == '0':
    temp_s = list(s)
    temp_s[0] = temp_s[-1] = '1'
    answer = max(answer, smallest_interior_gap(temp_s))
  # case 5: put 1 cow in the largest interior gap; Look for the largest interior gap again
  if gap >= 2:
    temp_s = list(s)
    temp_s[gap_start + gap // 2] = '1'
    gap, gap_start = largest_interior_gap(temp_s)
    answer = max(answer, put_cow_in_largest_interior_gap(temp_s))
  return answer



if __name__ == "__main__":
  with open(0) as f:
    n = int(f.readline())
    s = f.readline().strip()
  print(solve(s))