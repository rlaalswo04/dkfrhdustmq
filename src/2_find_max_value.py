"""
작성날짜 : 230513
설명: 리스트 내의 최댓값 찾기
"""

lists = [-13983, -1576823, -162314 , -5466735, -10, -345725, -54534662, -383656792]
max_value = lists[0]
for i in lists:
    if max_value < i:
        max_value = i

print(max_value)