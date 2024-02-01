def check_todo(sentence):
    word = "#TODO"
    if word in sentence:
        return True
    else:
        return False