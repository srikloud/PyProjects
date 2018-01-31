def dict_comprehension():
    old_dict = {'a': 1, 'c': 3, 'b': 2}
    updt_dict = {k: v * 10 for k, v in old_dict.items()}
    print(updt_dict)


dict_comprehension()