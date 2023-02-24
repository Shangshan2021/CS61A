

def mobile(left, right):
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be a arm"
    assert is_arm(right), "right must be a arm"
    return ['mobile', left, right]

def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'

def left(m):
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]

def right(m):
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]

def arm(length, mobile_or_planet):
    """Construct a arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]

def is_arm(s):
    """Return whether s is a arm."""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'

def length(s):
    """Select the length of a arm."""
    assert is_arm(s), "must call length on a arm"
    return s[1]

def end(s):
    """Select the mobile or planet hanging at the end of a arm."""
    assert is_arm(s), "must call end on a arm"
    return s[2]

def planet(size):
    """Construct a planet of some size."""
    assert size > 0
    "*** YOUR CODE HERE ***"
    return ['planet',size]


def size(w):
    """Select the size of a planet."""
    assert is_planet(w), 'must call size on a planet'
    "*** YOUR CODE HERE ***"
    return w[1]

def is_planet(w):
    """Whether w is a planet."""
    return type(w) == list and len(w) == 2 and w[0] == 'planet'

def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                              arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return (t, u, v)

def total_weight(m):
    """Return the total weight of m, a planet or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    True
    """
    if is_planet(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a planet"
        return total_weight(end(left(m))) + total_weight(end(right(m)))


def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(arm(3, t), arm(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(arm(1, v), arm(1, w)))
    False
    >>> balanced(mobile(arm(1, w), arm(1, v)))
    False

    True
    """
    "*** YOUR CODE HERE ***"
    if is_planet(m):
        return True
    if is_arm(m):
        return balanced(end(m))
    flag=all([balanced(s) for s in [left(m), right(m)]])
    l, r = left(m), right(m)
    l, r = length(l) * total_weight(end(l)), length(r) * total_weight(end(r))
    return (l == r)and flag

def totals_tree(m):
    """Return a tree representing the mobile with its total weight at the root.

    >>> t, u, v = examples()
    >>> print_tree(totals_tree(t))
    3
      2
      1
    >>> print_tree(totals_tree(u))
    6
      1
      5
        3
        2
    >>> print_tree(totals_tree(v))
    9
      3
        2
        1
      6
        1
        5
          3
          2
    True
    """
    "*** YOUR CODE HERE ***"
    if is_mobile(m):
        return tree(total_weight(m),[totals_tree(left(m)),totals_tree(right(m))])
    elif is_arm(m):
        return totals_tree(end(m))
    elif is_planet(m):
        return tree(total_weight(m))




def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)
def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]
def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
def label(tree):
    """Return the label value of a tree."""
    return tree[0]
def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)
def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)
# u,v,w=examples()
# a=totals_tree(w)
# print(a)
# print_tree(a)


def replace_leaf(t, find_value, replace_value):
    if label(t)==find_value:
        if is_leaf(t):
            return tree(replace_value)
        else:
            res = []
            for i in branches(t):
                res.append(replace_leaf(i,find_value,replace_value))
            return tree(replace_value,res)
    else:
        if is_leaf(t):
            return tree(label(t))
        else:
            res = []
            for i in branches(t):
                res.append(replace_leaf(i,find_value,replace_value))
            return tree(label(t), res)

# y=tree('odin',[tree('balder',[tree('thor'),tree('freya')]),tree('frigg',[tree('thor')]),tree('thor',[tree('sif'),tree('thor')]),tree('thor')])
# x=replace_leaf(y, 'thor', 'freya')
# print(x)

def has_path(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    "*** YOUR CODE HERE ***"
    if label(t)==word[0]:
        if len(word)==1:
            return True
        elif is_leaf(t):
            return False
        else:
            for i in branches(t):
                if has_path(i,word[1:]):
                    return True
    else:
        return False
def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return [label(t)]
    else:
        res = [label(t)]
        for i in branches(t):
            res+=preorder(i)
        return res

# numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
# print(preorder(numbers))
# greetings = tree('h', [tree('i'),tree('e', [tree('l', [tree('l', [tree('o')])]),tree('y')])])
# word='hi'
# print(has_path(greetings,word))
def test():
    nonlocal a
    print(a)
test()
