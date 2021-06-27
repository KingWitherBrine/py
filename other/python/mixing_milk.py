def mixing_milk(lst):
    for i in range(100):
        milk_to_be_poured = min(lst[i%3][1], lst[(i+1)%3][0] - lst[(i+1)%3][1])
        lst[i%3][1] -= milk_to_be_poured
        lst[(i+1)%3][1] += milk_to_be_poured
    return lst[0][1], lst[1][1], lst[2][1]

if __name__ == "__main__":
    with open('mixmilk.in') as f:
        lst = [list(map(int, line.strip().split())) for line in f]
    with open('mixmilk.out', 'w') as f:
        print(*mixing_milk(lst), sep="\n", file=f)