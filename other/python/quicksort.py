def qsort(nums, l, r):
    if l >= r:
        return
    pivot = partition(nums, l, r)
    qsort(nums, l, pivot)
    qsort(nums, pivot + 1, r)

def partition(nums, l, r):
    i, j, x = l - 1, r + 1, nums[(l + r) // 2]
    while i < j:
        i += 1
        while nums[i] < x:
            i += 1
        j -= 1
        while nums[j] > x:
            j -= 1
        if i < j:        
            nums[i], nums[j] = nums[j], nums[i]
    return j

a = [4,3,2]
qsort(a, 0, len(a) - 1)
print(a)