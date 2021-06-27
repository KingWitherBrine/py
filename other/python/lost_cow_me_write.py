def lost_cow(x, y):
    min_y, max_y = x, x
    step = 1
    total = 0
    while y not in range(min_y, max_y+1):
        if step > 0:
            max_y = x + step
        else:
            min_y = x + step
        step *= -2
        total += max_y-min_y
    extra = min(max_y-y, y-min_y)
    total -= extra
    return total

if __name__ == "__main__":
    with open("lostcow.in") as f:
        x, y = map(int, f.readline().split())
    with open("lostcow.out", "w") as f:
        print(lost_cow(x, y), file=f)