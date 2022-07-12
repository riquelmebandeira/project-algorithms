def is_anagram(first_string, second_string):
    word1 = first_string.lower()
    word2 = second_string.lower()

    if not word1 or not word2:
        return False

    for letter in word1:
        if letter not in word2:
            return False
        elif word1.count(letter) != word2.count(letter):
            return False

    return True
