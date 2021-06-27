def solve(rectangles):
    count = 0
    rectangles = list(map(sorted, rectangles))
    for i in range(len(rectangles)):
        if min(rectangles[i]) == max(rectangles)[0]:
            count += 1
    return count
if __name__ == "__main__":
    print(solve([[2,3],[3,7],[4,3],[3,7]]))