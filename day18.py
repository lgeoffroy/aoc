def solve(input):
    sum_no_precedence = 0
    sum_addition_prio = 0
    for line in input:
        sum_no_precedence += evaluate_no_precedence(line)
        sum_addition_prio += evaluate_addition_prio(line)
    return (sum_no_precedence, sum_addition_prio)

def evaluate_no_precedence(line):
    total = 0
    i = 0
    left = None
    right = None
    while i < len(line):
        if line[i] == '(':
            j = i + 1
            balanced = 0
            while line[j] != ')' or balanced > 0:
                if line[j] == '(':
                    balanced += 1
                if line[j] == ')':
                    balanced -= 1
                j += 1
            subexpr = line[i+1:j]
            if left is None:
                left = evaluate_no_precedence(subexpr)
            else:
                right = evaluate_no_precedence(subexpr)
            i += len(subexpr) + 2
        elif line[i] in '+*':  # they are nice we only have + and * operators
            operator = line[i]
        elif line[i] != ' ' and line[i] != ')':
            if left is None:
                left = int(line[i])  # they are nice we have no number > 9
            else:
                right = int(line[i])
        if right is not None:
            total = left + right if operator == '+' else left * right
            left = total
            right = None
        i += 1
    return total if total > 0 else left

def evaluate_addition_prio(line):
    nb_of_plus = len([i for i, ltr in enumerate(line) if ltr == '+'])
    new_line = line
    for n in range(nb_of_plus):
        indexes_of_plus = [i for i, ltr in enumerate(new_line) if ltr == '+']
        i = indexes_of_plus[n]
        if new_line[i-2] == ')':
            j = i-3
            balanced = 0
            factor_left = ''
            while new_line[j] != '(' or balanced > 0:
                if new_line[j] == ')':
                    balanced += 1
                if new_line[j] == '(':
                    balanced -= 1
                factor_left = new_line[j] + factor_left
                j -= 1
            factor_left = '(' + factor_left + ')'
        else:
            j = i-2
            factor_left = new_line[j]
        if new_line[i+2] == '(':
            k = i+3
            balanced = 0
            factor_right = ''
            while new_line[k] != ')' or balanced > 0:
                if new_line[k] == '(':
                    balanced += 1
                if new_line[k] == ')':
                    balanced -= 1
                factor_right += new_line[k]
                k += 1
            factor_right = '(' + factor_right + ')'
        else:
            k = i+2
            factor_right = new_line[k]
        new_line = new_line[:j] + '(' + factor_left + ' + ' + factor_right + ')' + new_line[k+1:]
    return evaluate_no_precedence(new_line)
