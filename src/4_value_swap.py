def value_swap(x, y):
    temp = x
    x = y 
    y = temp
    return x, y

x = 10
y = 20
# 현재 출력 10, 20
print(f'x: {x}, y: {y}')

# 기대값 x=20 y=10
# 정석

# temp = x
# x = y
# y = temp 
# print(x)
# print(y)

# 트릭
# x,y = y,x 

res1,res2 = value_swap(x, y)
print(f'x: {res1}, y:{res2}')