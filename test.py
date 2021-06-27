def solve(l, w, h, num_cuts, cut_width):
    if (num_cuts*cut_width) >= (l + w + h):
        return 0
    d = {"l":l, "w": w, "h":h}
    for i in range(num_cuts):
        max_m = "".join([k for k, v in d.items() if v == max(d.values())][0])
        d[max_m] -= cut_width
    return d["l"] * d["w"] * d["h"]
print(solve(10, 13, 14, 8, 1))