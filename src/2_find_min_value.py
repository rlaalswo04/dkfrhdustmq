"""
작성날짜 : 230513
설명: 리스트 내의 최댓값 찾기
"""


def min_value(my_list):
    min_value = my_list[0]
    for i in my_list:
        if min_value > i:
            min_value = i
    return min_value

lists = [26, 27, 24, 22, 23, 20, 21, 34]
result = min_value(lists)
print(result)

lists_1 = [25, 29, 28, 32, 30, 31, 32, 33]
result_1 = min_value(lists_1)
print(result_1) 
