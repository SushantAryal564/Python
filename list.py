# my_items = ['sushant', "ayral", "is", "best", "in", "the", "world"]
# print(my_items[0:3])
# print("sushant" in my_items)
# print(len(my_items))

# Nesting List in another list
q = [2, 3]
p = [1, q, 4]
p[1].append('xtra')
print(p)

# Different List type method:
my_list = ['Lithium', 'Something in the way', 'In Bloom', 'All Apologies',
           'Heart-shaped Box', 'Come as you are', 'Polly', 'Smells like Teen spirit']

my_list.append('school')
my_list.extend(['Aneurysm', 'Rape Me'])
my_list.insert(0, "know nothing")
my_list.remove("know nothing")
my_list.index("Lithium")
print(my_list.count("Lithium"))
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)

del my_list[-1]
print(my_list)
print("***********************")
prashant_list = my_list[:]
print(prashant_list)
