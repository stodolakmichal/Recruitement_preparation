def verify_if_anagram(first_word: str, second_word: str):
    first_word = first_word.lower()
    second_word = second_word.lower()
    first_word_list = list(first_word)
    first_word_list.sort()
    second_word_list = list(second_word)
    second_word_list.sort()
    if first_word_list == second_word_list:
        return True
    else:
        return False


print(verify_if_anagram("ananas", "sanaan"))
