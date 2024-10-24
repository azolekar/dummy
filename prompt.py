from .counter import count_word, read_corpus

def report_count(token):
    corpus = read_corpus()
    count = count_word(corpus, token)
    return f"The term '{token}' shows up in the corpus {count} times."