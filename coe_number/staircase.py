def staircase(n, display):
    lines = []
    for i in range(1, n + 1):
        line = " " * (n - i) + display * i
        lines.append(line)
    return "\n".join(lines)
