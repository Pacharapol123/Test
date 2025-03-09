def caesarCipher(s, k):
    result = []
    for char in s:
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - ord("A") + k) % 26 + ord("A"))
                result.append(new_char)
            else:
                new_char = chr((ord(char) - ord("a") + k) % 26 + ord("a"))
                result.append(new_char)
        else:
            result.append(char)
    return "".join(result)
