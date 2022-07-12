def is_palindrome_iterative(word):
    backwards = ""

    if not word:
        return False

    for letter in word:
        backwards = letter + backwards

    return True if word == backwards else False
