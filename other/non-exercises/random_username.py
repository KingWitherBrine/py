import random
first_names = ["Angry", "Brainy", "Careful", "Dangerous", "Enourmous", "Fat", "Gentle",
                "Hungry", "Illogical", "Jobless", "Knowing", "Laughing", "Massive", "Narrative",
                "Obese", "Pickled", "Quick", "Ragged", "Silent", "Talented", "Unsanitary",
                "Vain", "Weak", "X-rayed", "Youngest", "Zany"]
second_names = ["Apple", "Brain", "Cat", "Duck", "Egg", "Fruit", "Glob", "Horse",
                "Igloo", "Jackalope", "Key", "Lamb", "Meat", "Nacho", "Opera-singer",
                "Paper", "Queen", "Rat", "Shark", "Taser", "Umbrella", "Vat", "War",
                "Xylophone", "Youngster", "Zebra"]
while True:
    output = []
    seperator = input("Please enter what you want your seperator to be (if you want no seperator, type nothing): ")
    num = random.randint(0, len(first_names) - 1)
    output.append(first_names[num])
    num = random.randint(0, len(first_names) - 1)
    output.append(second_names[num])
    output = seperator.join(output)
    print("Your username is:", output,)