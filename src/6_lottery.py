# my_values = []
# my_values.append(1)
# my_values.append(4)
# my_values.append(3)
# print(my_values)
# for value in my_values:
#     print(value)

# if 2 in my_values:
#     print("값이 존재합니다")
# else:
#     print("값 x")


import random 

# my_value = []

# for i in range(6):
#   value = random.randint(1, 45)
#   if value in my_value:
#     break
#   my_value.append(value)

# print(my_value)

lotto_numbs = []
my_num = 1
is_ok = True
while is_ok:
    
    value = random.randint(1, 45)
    if value in lotto_numbs:
        continue
    lotto_numbs.append(value)
    if len(lotto_numbs) == 6:
        break
    
print(lotto_numbs)