import csv

def solve(matrix):
    countries = matrix[0]
    matrix = matrix[1:]
    USD_index = countries.index("USD")
    CNY_index = countries.index("CNY")
    USD_values = []
    CNY_values = []
    for i in matrix:
        USD_values.append(i[USD_index])
        CNY_values.append(i[CNY_index])
    ratios = []
    for i in range(30):
        ratios.append(float(CNY_values[i]) / float(USD_values[i]))
    avg = sum(ratios)/len(ratios)
    return avg

if __name__ == "__main__":
    with open("eurofxref-hist 2.csv") as f:
        file = csv.reader(f, delimiter=",", quotechar='"')
        matrix = [line for line in file][:31]
    print(solve(matrix))