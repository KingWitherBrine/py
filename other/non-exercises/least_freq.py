book = "The dog chased the rabbit into the forest but the rabbit was too quick."
book = book.lower()
freq_words = {}
for wrd in book.split():
    freq_words[wrd] = freq_words.get(wrd, 0) + 1

least = book.split()[0]
for word in freq_words:
    if freq_words[word] < freq_words[least]:
        least = word
print(least)