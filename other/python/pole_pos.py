def solve(num_cars, car_data): # num_cars: 4 data: [[1, 0], [2, -1], [3, 1], [4, -1]]
    lst = [0]*num_cars
    for i, (car_num, change_pos) in enumerate(car_data):
        previous_index = i + change_pos
        if previous_index < 0 or previous_index > num_cars or lst[previous_index] > 0:
            return [-1]
        lst[previous_index] = car_num
    return lst
if __name__ == "__main__":
    # print(*solve(4, [[1, 0], [3, 1], [2, -1], [4, 0]]))
    # print(*solve(4, [[22, 1], [9, 1], [13, 0], [21, -2]]))
    # print(*solve(2, [[1, 24], [2, 0]]))
    with open(0) as f:
        while True:
            num_cars = int(f.readline().strip())
            if num_cars == 0:
                break
            cars = [list(map(int, f.readline().strip().split())) for i in range(num_cars)]
            print(*solve(num_cars, cars))