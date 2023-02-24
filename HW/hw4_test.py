def repeated(t, k):
    assert k > 1
    lst=t
    count=0
    pre_num=1/3
    def repeat():
        nonlocal lst
        nonlocal pre_num
        nonlocal count
        now_num=next(lst)
        if now_num==pre_num:
            count+=1
            if count==k-1:
                count=0
                return now_num
        else:
            pre_num=now_num
            count=0
        return repeat()
    return repeat()

s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
print(repeated(s2, 3))

