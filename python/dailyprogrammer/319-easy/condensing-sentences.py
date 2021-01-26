# Solution without using regex

def condense(sentence):
    """Iterates through `sentence` and returns condensed string"""
    words = sentence.split(' ')
    previous_words = [""]
    for word in words:
        condensed_word, is_condensed = condense_word(previous_words[-1], word)
        if is_condensed:
            previous_words.pop()
        previous_words.append(condensed_word)

    return ' '.join(previous_words)


def condense_word(first_word, last_word):
    """Combines overlapping strings and returns the combined string and a bool of whether or not it made any changes"""
    for i in range(len(first_word))[::-1]: # Reversed to get largest match possible first
        if first_word[-i:] == last_word[:i]:
            return first_word + last_word[i:], True

    return last_word, False

def test_sentences():
    print(condense("I heard the pastor sing live verses easily."))
    print(condense("Deep episodes of Deep Space Nine came on the television only after the news."))
    print(condense("Digital alarm clocks scare area children."))

if __name__ == '__main__':
    test_sentences()
