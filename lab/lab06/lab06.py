this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    def inc(x):
        nonlocal a
        res=a+x
        a=a+1
        return res
    return lambda x:inc(x)


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    pre_num=1
    pre_pre_num=0
    count=0
    def fib_in():
        nonlocal count
        nonlocal pre_num
        nonlocal pre_pre_num
        if count==0:
            count=count+1
            return pre_pre_num
        elif count==1:
            count=count+1
            return pre_num
        else:
            result=pre_num+pre_pre_num
            pre_pre_num=pre_num
            pre_num=result
            return result
    return lambda :fib_in()


def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    index=0
    def insert_step(lst):
        nonlocal index
        for i in range(index,len(lst)):
            if lst[i]==entry:
                lst.insert(i+1,elem)
                index=index+2
                return insert_step(lst)
            else:
                index+=1
        return lst
    return insert_step(lst)
