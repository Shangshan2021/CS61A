# def combine(guess=1,tolerance=1e-15):
#     while not abs(guess*guess-(guess+1))<tolerance:
#         guess=1+1/guess
#     return guess
# result=combine()
# print(result)


# def pingpong(n):
#     def diff(n):
#
#     if '8' in str(n) or n % 8 == 0:
#         return minus(n - 1) + 1
#     elif n == 1:
#         return 1
#     else:
#         return pingpong(n - 1) + 1
#
# print(pingpong(28))

# def change_abstraction(change):
#     change_abstraction.changed = change
# change_abstraction.changed = False
#
# def berry_finder(t):
#     result=False
#     if change_abstraction.changed:
#         if t['lable']=='berry' or t=='berry':
#             return True
#         elif t['branches']:
#             return berry_finder(t['branches'])
#     else:
#         if t[0]=='berry' or t=='berry':
#             return True
#         elif len(t)>1 :
#             for i in range(1,len(t)):
#                 result=result or berry_finder(t[i])
#     return result
#
# def tree(label, branches=[]):
#     """Construct a tree with the given label value and a list of branches."""
#     if change_abstraction.changed:
#         for branch in branches:
#             assert is_tree(branch), 'branches must be trees'
#         return {'label': label, 'branches': list(branches)}
#     else:
#         for branch in branches:
#             assert is_tree(branch), 'branches must be trees'
#         return [label] + list(branches)
#
# def is_tree(tree):
#     """Returns True if the given tree is a tree, and False otherwise."""
#     if change_abstraction.changed:
#         if type(tree) != dict or len(tree) != 2:
#             return False
#         for branch in branches(tree):
#             if not is_tree(branch):
#                 return False
#         return True
#     else:
#         if type(tree) != list or len(tree) < 1:
#             return False
#         for branch in branches(tree):
#             if not is_tree(branch):
#                 return False
#         return True
#
#
# def branches(tree):
#     """Return the list of branches of the given tree."""
#     if change_abstraction.changed:
#         return tree['branches']
#     else:
#         return tree[1:]
#
#
# def label(tree):
#     """Return the label value of a tree."""
#     if change_abstraction.changed:
#         return tree['label']
#     else:
#         return tree[0]
#
# def print_tree(t, indent=0):
#     print('  ' * indent + str(label(t)))
#     for b in branches(t):
#         print_tree(b, indent + 1)
# # scrat = tree('berry')
# # print(berry_finder(scrat))
# # scrat=sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
# # print(berry_finder(scrat))
#
#
# def sprout_leaves(t, leaves):
#     if change_abstraction.changed:
#         if t['braches']:
#             return tree(t['label'], sprout_leaves(t['branches'], leaves))
#         else:
#             return tree(t['label'], leaves)
#     else:
#         if len(t)>1:
#             l=[]
#             for i in range(1, len(t)):
#                 l.append(sprout_leaves(t[i],leaves))
#             return tree(t[0],tree(l))
#         else :
#             l=[]
#             for _ in leaves:
#                 l.append(tree(_))
#             # print(tree(t[0],tree(l)))
#             return tree(t[0],tree(l))
#
# t1 = tree(1, [tree(2), tree(3)])
# print(t1)
# new1 = sprout_leaves(t1, [4, 5])
# print_tree(new1)


# def mobile(left, right):
#     """Construct a mobile from a left arm and a right arm."""
#     assert is_arm(left), "left must be a arm"
#     assert is_arm(right), "right must be a arm"
#     return ['mobile', left, right]
#
# def is_mobile(m):
#     """Return whether m is a mobile."""
#     return type(m) == list and len(m) == 3 and m[0] == 'mobile'
#
# def left(m):
#     """Select the left arm of a mobile."""
#     assert is_mobile(m), "must call left on a mobile"
#     return m[1]
#
# def right(m):
#     """Select the right arm of a mobile."""
#     assert is_mobile(m), "must call right on a mobile"
#     return m[2]
#
# def arm(length, mobile_or_planet):
#     """Construct a arm: a length of rod with a mobile or planet at the end."""
#     assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
#     return ['arm', length, mobile_or_planet]
#
# def is_arm(s):
#     """Return whether s is a arm."""
#     return type(s) == list and len(s) == 3 and s[0] == 'arm'
#
# def length(s):
#     """Select the length of a arm."""
#     assert is_arm(s), "must call length on a arm"
#     return s[1]
#
# def end(s):
#     """Select the mobile or planet hanging at the end of a arm."""
#     assert is_arm(s), "must call end on a arm"
#     return s[2]
#
# def planet(size):
#     """Construct a planet of some size."""
#     assert size > 0
#     "*** YOUR CODE HERE ***"
#     return ['planet',size]
#
#
# def size(w):
#     """Select the size of a planet."""
#     assert is_planet(w), 'must call size on a planet'
#     "*** YOUR CODE HERE ***"
#     return w[1]
#
# def is_planet(w):
#     """Whether w is a planet."""
#     return type(w) == list and len(w) == 2 and w[0] == 'planet'
#
# def examples():
#     t = mobile(arm(1, planet(2)),
#                arm(2, planet(1)))
#     u = mobile(arm(5, planet(1)),
#                arm(1, mobile(arm(2, planet(3)),
#                               arm(3, planet(2)))))
#     v = mobile(arm(4, t), arm(2, u))
#     return (t, u, v)
#
# def total_weight(m):
#
#     if is_planet(m):
#         return size(m)
#     else:
#         assert is_mobile(m), "must get total weight of a mobile or a planet"
#         return total_weight(end(left(m))) + total_weight(end(right(m)))
# t = mobile(arm(3, planet(2)),
#             arm(2, planet(2)))
# print(total_weight(t))
# from operator import mul, truediv
# from operator import add, sub
#
#
# def make_ternary_constraint(a, b, c, ab, ca, cb):
#     """The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b) = a."""
#
#     def new_value():
#         av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
#         if av and bv:
#             c['set_val'](constraint, ab(a['val'], b['val']))
#         elif av and cv:
#             b['set_val'](constraint, ca(c['val'], a['val']))
#         elif bv and cv:
#             a['set_val'](constraint, cb(c['val'], b['val']))
#
#     def forget_value():
#         for connector in (a, b, c):
#             connector['forget'](constraint)
#
#     constraint = {'new_val': new_value, 'forget': forget_value}
#     for connector in (a, b, c):
#         connector['connect'](constraint)
#     return constraint
#
#
# def adder(a, b, c):
#     """The constraint that a + b = c."""
#     return make_ternary_constraint(a, b, c, add, sub, sub)
#
#
# def multiplier(a, b, c):
#     """The constraint that a * b = c."""
#     return make_ternary_constraint(a, b, c, mul, truediv, truediv)
#
#
# def converter(c, f):
#     """Connect c to f with constraints to convert from Celsius to Fahrenheit."""
#     u, v, w, x, y = [connector() for _ in range(5)]
#     multiplier(c, w, u)
#     multiplier(v, x, u)
#     adder(v, y, f)
#     constant(w, 9)
#     constant(x, 5)
#     constant(y, 32)
#
#
# def constant(connector, value):
#     """The constraint that connector = value."""
#     constraint = {}
#     connector['set_val'](constraint, value)
#     return constraint
#
#
# def connector(name=None):
#     """A connector between constraints."""
#     informant = None
#     constraints = []
#
#     def set_value(source, value):
#         nonlocal informant
#         val = connector['val']
#         if val is None:
#             informant, connector['val'] = source, value
#             if name is not None:
#                 print(name, '=', value)
#             inform_all_except(source, 'new_val', constraints)
#         else:
#             if val != value:
#                 print('Contradiction detected:', val, 'vs', value)
#
#     def forget_value(source):
#         nonlocal informant
#         if informant == source:
#             informant, connector['val'] = None, None
#             if name is not None:
#                 print(name, 'is forgotten')
#             inform_all_except(source, 'forget', constraints)
#
#     connector = {'val': None,
#                  'set_val': set_value,
#                  'forget': forget_value,
#                  'has_val': lambda: connector['val'] is not None,
#                  'connect': lambda source: constraints.append(source)}
#     return connector
#
#
# def inform_all_except(source, message, constraints):
#     """Inform all constraints of the message, except source."""
#     for c in constraints:
#         if c != source:
#             c[message]()
#
#
# celsius = connector('Celsius')
# fahrenheit = connector('Fahrenheit')
# converter(celsius, fahrenheit)
# celsius['set_val']('user', 25)

# class Account:
#     a=0
#     def __init__(self, account_holder):
#         self.balance = 0
#         self.holder = account_holder
#
#     def deposit(self, amount):
#         """Increase the account balance by amount and return the new balance."""
#         self.balance = self.balance + amount
#         return self.balance
#
# spock_account=Account('Spock')
# v=Account('Spock')
# v.deposit(1000)
# print(Account.deposit(spock_account, 1000)==v)

