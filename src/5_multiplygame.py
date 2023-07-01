"""
설명: 구구단 게임
기능: 
1.입력 (키보드)
2.문제랜덤(2단 ~ 9단)
3.3문제
4.정답률 보이기
"""

import random
pass_count = 0
for i in range(3):
    random_value_1 = random.randint(2, 9)
    random_value_2 = random.randint(1, 9)
    print(f"{random_value_1} x {random_value_2}")
    user_input = int(input())
    print(random_value_1 * random_value_2)
    if int(user_input) == (random_value_1 * random_value_2):
        print("정답")
        pass_count = pass_count + 1
    else:
        print("정답이 아닙니다")
print(f"맞춘갯수는 : {pass_count} 개")