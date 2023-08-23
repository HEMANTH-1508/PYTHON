# permutations(no of ways a number can be displayed)

import itertools
a=input("ENTER A NUMBER : ")
p=list(itertools.permutations(a))

res=[' '.join(x) for x in p]
print(res)

