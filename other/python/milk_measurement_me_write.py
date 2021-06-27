def solve(matrix):
    measures = {"Bessie": 7, "Elsie": 7, "Mildred": 7}
    winner, total = None, 0
    for _, cow, change in matrix:
        measures[cow] += change
        max_output = max(measures.values())
        current_winners = [k for k, v in measures.items() if v == max_output]
        if current_winners != winner:
            total += 1
            winner = current_winners
    return str(total)

if __name__ == "__main__":
  with open("measurement.in") as f:
    N = int(f.readline())
    matrix = []
    for line in f:
      day, name, change = line.strip().split()
      matrix.append([int(day), name, int(change)])
  with open("measurement.out", "w") as f:
    print(solve(sorted(matrix)), file=f)