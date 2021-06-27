import random
from math import sqrt

print("Hello I am Alexa")
menu = """Here are a list of things you can do:
Games:
'1: Roll a dice', '2: Guess number game', '3: Give me a random number', '4: Pokemon adventure (Under Construction)', '5: Magic eight ball', '6: Coinflip, 7: Gambling (WARNING: For 18+ players only)'
Questions:
'1 + 1', '24 * 3', '100 / 20', '2 ** 12', '124 - 56', '2 ** 10', 'sqrt 25'
And please say 'question' before asking your question:
e.g: 
question
1 + 1
"""
print(menu)
while True:
    answer = input("What would you like to do?\n")

    if answer in ["Options", "What are the options", "What are the options again", "options"]:
        print(menu)
    if answer == 'Roll a dice' or answer == "1":
        print("Your dice number is:\n ", random.randint(1, 6))
    """Guess Number Game"""
    if answer == 'Guess number game' or answer == '2':
        guess = int(input('Please enter a number 0 through 1000: '))
        tries = 1
        actual = random.randint(0, 1000)

        while guess != actual:
            tries += 1
            if guess < actual:
                print("Too small. Please enter another number: ")
            else:
                print("Too big. Please enter another number: ")
            guess = int(input())

        print("Found it after", tries, "tries")
    """Random Number"""
    if answer == 'Give me a random number' or answer == '3':
        num1 = int(input("What is smaller number?\n"))
        num2 = int(input("What is bigger number?\n"))
        number = random.randint(num1, num2)
        print("here is your number: \n", number)
    """Pokemon aventure"""
    if answer == 'Pokemon adventure' or answer == "4":
        pokemon = input("What pokemon do you want for this game, you can pick from Pikachu, Eevee, Paras, Charmander, you will unlock other pokemon later on: \n")
        name_pokemon = input("What name should your pokemon be: \n")
        name = input("What should we call you: \n")
        print(f"Okay, {name}, your pokemon is now {pokemon}, and it's name is {name_pokemon}, we will continue with our adventure.")
        print("""Here is a list of commands you can do:  
        Rewards: daily, weekly, hourly, quiz
        Pokemon: catch, upgrade, pokeballs
        General: inventory, mypokemon, """)
    """Magic eight ball"""
    if answer == 'Magic eight ball' or answer == "5":
        eight_ball_question = input("What is your question (Please only ask a yes or no question)?\n")
        answer = random.choice(["Absolutely!", "Of course not!", "Obviously yes!", "No", "Yes", "Trump (Dorito, Turnip) says NO", "Nah", "Yeah!", "YES", "NO"])
        print(f"The magic eight ball has spoken, the answer is '{answer}'")
    """Coinflip"""
    if answer == 'Coinflip' or answer == "6":
        coin_face_up = random.choice(["Heads", "Tails"])
        print(f"The coin is {coin_face_up}")

    if answer == 'Gambling' or answer == "7":
        age = int(input("How old are you?\n "))
        if age < 18:
            print(f"Hey! You are not yet 18. Do not even attempt to gamble! You will be able to play in {18 - age} years. ")
        else:
            print("Hi! I am your assistant, Alexa, your currently have 100 credits to use! ")
            print("Your options are: slots, blackjack, ")

    """Questions"""
    if answer.lower() in ["question", "question", "ask", "what is", "questions"]:
        question = input("Okay! What is your question?\n")
        answer_choices = ["The answer is ", "The answer to your question is ", "It is ", "Okay, it is ", f"The answer to {question} is ", "This is ", "Easy, the answer is "]
        answer_begin = random.choice(answer_choices)
        if question.split()[1] == "+":
            n1, n2 = int(question.split()[0]), int(question.split()[-1])
            print(f"{answer_begin}{n1 + n2}")
        if question.split()[1] == "*":
            n1, n2 = int(question.split()[0]), int(question.split()[-1])
            print(f"{answer_begin}{n1 * n2}")
        if question.split()[1] == "/":
            n1, n2 = int(question.split()[0]), int(question.split()[-1])
            print(f"{answer_begin}{n1 / n2}")
        if question.split()[1] == "-":
            n1, n2 = int(question.split()[0]), int(question.split()[-1])
            print(f"{answer_begin}{n1 - n2}")
        if question.split()[1] == "**":
            n1, n2 = int(question.split()[0]), int(question.split()[-1])
            print(f"{answer_begin}{n1 ** n2}")
        if question.split()[0].lower() == "sqrt":
            n = int(question.split()[1])
            print(f"{answer_begin}{sqrt(n)}")