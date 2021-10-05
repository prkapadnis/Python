gen_exp = (x*x for x in range(5))
for i in gen_exp:
    print(i)

print(sum(x*x for x in range(5)))

even_num = (x for x in range(1,11) if x % 2 == 0)
for num in even_num:
    print(num)
