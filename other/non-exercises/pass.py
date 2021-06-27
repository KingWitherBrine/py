import random
import sys
# sys.setExecutionLimit(60000) # 60 seconds
my_password = "abcd"
guess_num = 0
done = False
while not done:

    guessed_pw = ""
    # your code here
    letters = "abcdefghijklmnopqrstuvwxyz"
    length = len(letters)
    for _ in range(len(my_password)):
        x = letters[random.randrange(length)]
        guessed_pw += x
    guess_num += 1
    if guessed_pw == my_password:
        print("found it after ", guess_num, " tries")
        done = True
