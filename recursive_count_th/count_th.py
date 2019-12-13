def count_th(word):
    if len(word) == 2:
        if word == "th":
            return 1
        else:
            return 0
    elif len(word) < 2:
        return 0

    else:
        return count_th(word[-2:]) + count_th(word[:-1])