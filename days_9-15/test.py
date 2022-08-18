import random
list_me = [1, 2]
while sum(list_me) < 17:
    list_me.append(random.randint(1, 5))
print(list_me)
