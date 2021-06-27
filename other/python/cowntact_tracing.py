def meet_condition(patient_zero, k, matrix, cows_state, N):
    infected = [0] * (N+1)
    infected[patient_zero] = 1
    handshakes = [0] * (N + 1)
    for _, x, y in matrix:
        if infected[x]:
            handshakes[x] += 1
        if infected[y]:
            handshakes[y] += 1
        if infected[x] and handshakes[x] <= k:
            infected[y] = 1
        if infected[y] and handshakes[y] <= k:
            infected[x] = 1
    all_true = True
    for i, cow in enumerate(infected[1:]):
        if str(cow) != cows_state[i]:
            all_true = False
            break
    return all_true
def solve(matrix, cows_state, N, T):
    matrix = sorted(matrix)
    zero_patients = [False] * (N+1)
    lower_k, upper_k = T, 0
    for i in range(1, N+1):
        for k in range(T+1):
            if meet_condition(i, k, matrix, cows_state, N):
                zero_patients[i] = True
                lower_k, upper_k = min(lower_k, k), max(upper_k, k)
    return zero_patients.count(True), lower_k, "Infinity" if upper_k == T else upper_k

if __name__ == "__main__":
  with open("tracing.in") as f:
    N, T = map(int, f.readline().split())
    cows_state = f.readline().strip()
    matrix = [tuple(map(int, line.strip().split())) for line in f]
  with open("tracing.out", "w") as f:
    print(*solve(matrix, cows_state, N, T), file=f)