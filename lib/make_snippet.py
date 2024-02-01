def make_snippet(sentence):
    words = sentence.split()

    snippet_word = words[:5]
    if len(words) > 5:
        snippet_word.append('...')

    snippet = ' '.join(snippet_word)
    return snippet