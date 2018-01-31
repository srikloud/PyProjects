def count_bynum_dict_cmprehension():
    n = "10 10 10 50 50 50 50 50 90 90 90 90 90 90 5 5 5 5 20 20 30 30 30"
    lst_n = list(n.split())
    d = {n:lst_n.count(n) for n in lst_n}
    print(d)

count_bynum_dict_cmprehension()