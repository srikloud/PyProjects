def recur_sum_n_ints(n):
    while(n>=1):
        yield eval("n") + recur_sum_n_ints(eval("n")-1)


x = recur_sum_n_ints(10)
for i in x:
    print(i)

