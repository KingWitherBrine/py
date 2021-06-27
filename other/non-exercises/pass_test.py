letters = "abcdefghijklmnopqrstuvwxyz"
import random
import sys
# sys.setExecutionLimit(60000) # 60 seconds
my_password = "abcd"
guess_num = 0
done = False
while not done:

    guessed_pw = ""
    guessed_pw = "aaaa"
    for _ in range(3):
        if guessed_pw[- 1] == "a":
            