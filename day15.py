def solve(input):
    return (calc(input, 2020), calc(input, 30000000))

def calc(input, nth):
    numbers = [int(x) for x in input[0].split(',')]
    dic = {}

    for i in numbers:
        dic[i] = [numbers.index(i)]

    n = numbers[-1]
    for i in range(len(numbers), nth):
        j = i - 2
        n = 0 if len(dic[n]) == 1 else dic[n][-1] - dic[n][-2]
        if not n in dic:
            dic[n] = []
        dic[n].append(i)

    return n
