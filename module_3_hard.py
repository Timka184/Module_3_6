def calculate_structure_sum(data_structure):
    s = 0
    def recurse(i):
        nonlocal s
        if isinstance(i, (int, float)):
            s += i
        elif isinstance(i, str):
            s += len(i)
        elif isinstance(i, (tuple, list, set)):
            for j in i:
                recurse(j)
        elif isinstance(i, dict):
            for key, value in i.items():
                recurse(key)
                recurse(value)
        else:
            pass

    for h in data_structure:
        recurse(h)

    return s

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)
