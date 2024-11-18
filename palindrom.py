def verify_if_palindrome(word: str):
    temp_var = True

    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            temp_var = False
            break

    return temp_var


print(verify_if_palindrome("asasagggg"))
