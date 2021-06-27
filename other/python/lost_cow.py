def lost_cow(x, y):
    is_add = True
    count = 0
    i = 0
    while True:
        if is_add:
            if x <= y <= x + 2 ** i:
                count += y - x
                return count
        else:
            if x - 2 ** i <= y <= x:
                count += x - y
                return count 
        count += 2 ** (i+1)
        is_add = not is_add
        i += 1

if __name__ == "__main__":
    with open(0) as f:
        x, y = list(map(int, f.readline().strip().split()))
        print(lost_cow(x, y))