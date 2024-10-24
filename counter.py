def count_word(text, word):
    return text.lower().count(word.lower())

def read_corpus():
    with open('corpus.txt', 'r') as file:
        return file.read()