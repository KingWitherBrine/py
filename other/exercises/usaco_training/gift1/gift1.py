"""

ID: noahche1
LANG: PYTHON3
TASK: gift1

"""
with open("gift1.in", "r") as input:
    input2 = input.readlines()
num_people = int(input2[0])
input2.pop(0)
money = {}
for i in range(num_people):
    money[input2[0].strip()] = 0
    input2.pop(0)

for i in range(num_people): 
    giver = input2[0]
    input2.pop(0)
    receiver = int(input2[0].split()[1])
    if receiver != 0:
        remainder = int(input2[0].split()[0]) % receiver
        money_to_receiver = int(int(input2[0].split()[0]) / receiver)
    else:
        remainder = int(input2[0].split()[0])
        money_to_receiver = 0
    input2.pop(0)
    for i in range(receiver):
        money[input2[0].strip()] += money_to_receiver
        input2.pop(0)

    money[giver.strip()] -= (money_to_receiver * receiver)

with open("gift1.out", "w") as output:
    for i in money:
        output.write(f"{i} {money[i]}\n")