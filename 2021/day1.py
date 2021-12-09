def solve(lines):
    liste = [int(x) for x in lines]

    i = j = k = 0
    old_sum = None
    while True:
        try:
            current_sum = sum(liste[i:i+3])
            if old_sum and current_sum > old_sum:
                k = k + 1
            old_sum = current_sum
            if liste[i] < liste[i+1]:
                j = j + 1
            i = i + 1
        except IndexError:
            return (j, k)
