"""
    For Loop implementation
"""
def for_loop(sample):
    it = iter(sample)
    while True:
        try:
            item = next(it)
            print(item)
        except StopIteration:
            break
a_list = [1, 2, 3]
for_loop(a_list)
a_tuple = (1, 2, 3)
print()
for_loop(a_tuple)
print()
a_set = {1,2,3}
print()
for_loop(a_set)