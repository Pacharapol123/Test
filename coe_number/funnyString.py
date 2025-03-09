def funnyString(s):
    diffs = []
    for i in range(len(s) - 1):
        diffs.append(abs(ord(s[i]) - ord(s[i + 1])))

    return "Funny" if diffs == diffs[::-1] else "Not Funny"
