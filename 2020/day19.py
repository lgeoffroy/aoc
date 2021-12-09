import regex

def solve(input):
    (rules, messages) = parse(input)
    rules = compute_rules(rules)

    l42 = len(rules['42'][0])
    l31 = len(rules['31'][0])

    def verifies_eight(word, rec=True):
        if len(word) == l42:
            return word in rules['42']
        if len(word) == 0 or len(word) % l42 != 0:
            return False
        if rec:
            return verifies_eight(word[:l42]) and verifies_eight(word[l42:])
        return False

    def verifies_eleven(word, rec=True):
        if len(word) == l42 + l31:
            return word[:l42] in rules['42'] and word[l42:] in rules['31']
        if len(word) == 0 or len(word) % (l42 + l31) != 0:
            return False
        if rec:
            return word[:l42] in rules['42'] and word[-l31:] in rules['31'] and verifies_eleven(word[l42:-l31])
        return False

    def count_valid(rec):
        n = 0
        for m in messages:
            k = 0
            for k in range(len(m)):
                if verifies_eight(m[:k], rec) and verifies_eleven(m[k:], rec):
                    n += 1
                    break
        return n

    return (count_valid(False), count_valid(True))

def parse(input):
    rules = {}
    messages = []
    for line in input:
        match = regex.match(r'^(\d+): (.*)$', line)
        if match:
            (n, rule) = match.groups()
            rules[n] = rule
        messages.append(line)
    return (rules, messages)

def compute_rules(rules):
    rules['0'] = get_subrules(rules, rules['0'])
    return rules

def get_subrules(rules, rule):
    if isinstance(rule, list):
        return rule
    if rule == '"a"' or rule == '"b"':
        return [rule.strip('"')]
    if rule.find('|') != -1:
        return flatten([get_subrules(rules, subrule.strip()) for subrule in rule.split('|')])
    rules_indexes = regex.match(r'^((\d+)( |$))+', rule).captures(2)
    builder = get_subrules(rules, rules[rules_indexes[0]])
    rules[rules_indexes[0]] = builder
    n = len([x for x in rules.values() if not isinstance(x, list)])
    if n == 1:
        return builder
    for i in range(1, len(rules_indexes)):
        subrules = get_subrules(rules, rules[rules_indexes[i]])
        rules[rules_indexes[i]] = subrules
        builder = concat_rules(builder, subrules)
    return builder

def concat_rules(a, b):
    if len(a) == 1:
        if len(b) == 1:
            return [a[0] + b[0]]
        return [a[0] + b_elem for b_elem in b]
    if len(b) == 1:
        return [a_elem + b[0] for a_elem in a]
    all_rules = [concat_rules([x], b) for x in a]
    return flatten(all_rules)

def flatten(items):
    flat = []
    for x in items:
        if isinstance(x, list):
            for y in x:
                flat.append(y)
        else:
            flat.append(x)
    return flat
