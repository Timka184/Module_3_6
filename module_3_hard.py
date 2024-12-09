def calculate_structure_sum(data_structure):
    s = 0
    for i in data_structure:
        if isinstance(i, list):
            s += sum(i)
        elif isinstance(i, tuple):
            for h in i:
                if isinstance(h, dict):
                    s += sum(h.values())
                    s += sum(len(key) for key in h.keys())
                elif isinstance(h, tuple):
                    s += sum(h)
                elif isinstance(h, list):
                    for g in h:
                        for t in g:
                            for p in t:
                                if isinstance(p, str):
                                    s += len(p)
                                elif isinstance(p, tuple):
                                    for k in p:
                                        if isinstance(k, str):
                                            s += len(k)
                                        else:
                                            s += k
                                else:
                                    s += p
                else:
                    s += h
        elif isinstance(i, dict):
            s += sum(i.values())
            s += sum(len(key) for key in i.keys())
        elif isinstance(i, str):
            s += len(i)
        else:
            s += i
    return s


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)