"""

ID: noahche1
LANG: PYTHON3
TASK: ride

"""
t = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, 
"J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, 
"S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

with open("ride.in", "r") as input:
    y = input.readlines()
    comet_name = y[0].strip()
    group_name = y[1].strip()
    comet_int = 1
    group_int = 1
for i in comet_name:
    comet_int *= t[i]
for j in group_name:
    group_int *= t[j]
with open("ride.out", "w") as output:
    if comet_int % 47 == group_int % 47:
        output.write("GO\n")
    else:
         output.write("STAY\n")

