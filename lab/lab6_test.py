def make_adder_inc(a):
    def inc(x):
        nonlocal a
        res=a+x
        a=a+1
        return res
    return lambda x:inc(x)
adder1 = make_adder_inc(5)
print([adder1(x) for x in [1, 2, 3]])