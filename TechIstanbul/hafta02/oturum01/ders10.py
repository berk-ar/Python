kume1 = {"a", "b", "c"}
kume2 = {1,2,3}

kumeBirlesim = kume1 | kume2   # Küme birleştirme
print(kume1)    # {'c', 'b', 'a'}
print(kume2)    # {1, 2, 3}
print(kumeBirlesim)    # {1, 2, 3, 'c', 'b', 'a'}

kumeBirlesim2 = kume1.union(kume2)
print(kumeBirlesim2)    # {1, 2, 3, 'b', 'c', 'a'}

