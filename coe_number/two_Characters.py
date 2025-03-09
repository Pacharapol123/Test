def alternate(s):
    unique_chars = list(set(s))
    max_length = 0
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            c1, c2 = unique_chars[i], unique_chars[j]
            filtered = [ch for ch in s if ch == c1 or ch == c2]
            if len(filtered) < 2:
                continue
            valid = True
            for k in range(1, len(filtered)):
                if filtered[k] == filtered[k - 1]:
                    valid = False
                    break
            if valid:
                max_length = max(max_length, len(filtered))
    return max_length
