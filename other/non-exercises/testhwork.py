import random

nouns = ['this', 'loop', 'dirt', 'cube']
verbs = ['happy', 'mad', 'dirty', 'yeet']
spaces_between_password = ['!', '@', '#', '$', '^', '&', '*', '(', ')', '_']
words = nouns + verbs
password = spaces_between_password[random.randint(0, 9)].join(random.choices(words, k=2))
print(password)