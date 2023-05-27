"""
230513
합구하기
"""

def sum_sequence(num):    
    sum = 0
    for i in range(1, num+1):
        sum = sum + i

    return sum


result = sum_sequence(100)
print(result)

result = sum_sequence(10)
print(result)

result = sum_sequence(500)
print(result)