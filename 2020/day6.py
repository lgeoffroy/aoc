def nb_yes_for(lines):
    answers = []
    for line in lines:
        for x in line:
            if x not in answers:
                answers.append(x)
    return len(answers)

def nb_all_yes_for(lines):
    answers = []
    for x in 'abcdefghijklmnopqrstuvwxyz':
        if all([x in line for line in lines]):
            answers.append(x)
    return len(answers)

def solve(lines):
    lines.append('')
    nb_yes = 0
    nb_all_yes = 0
    buffer = []
    for line in lines:
        if line == '':
            nb_yes += nb_yes_for(buffer)
            nb_all_yes += nb_all_yes_for(buffer)
            buffer = []
        else:
            buffer.append(line)

    return (nb_yes, nb_all_yes)
