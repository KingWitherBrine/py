book = "The dog chased the rabbit into the forest but the rabbit was too quick."
book = book.lower()
word_list = book.split()
freq_words = {}
for wrd in word_list:
    freq_words[wrd] = freq_words.get(wrd, 0) + 1

most = word_list[0]
for word in freq_words:
    if freq_words[word] > freq_words[most]:
        most = word
print(most)