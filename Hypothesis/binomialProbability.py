def factor(num):
    f = 1
    for counter in range(1, num + 1):
        f *= counter
    return f


def binomialPR(num, k, p):
    for counter in range(0, num):
        prob = (factor(num) / (factor(k) * factor(num - k))) * (p ** k) * ((1 - p) ** (num - k))
        if prob <= 0.001:
            prob = 0
        return round(prob, 3)


n = 14
for cnt in range(0, n + 1):
    print(f'{cnt} - {binomialPR(n, cnt, 0.5)}')
