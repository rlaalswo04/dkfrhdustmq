# for i in range(5):
#     print("_" * i + 1)


def add(a, b, works):
    # 함수 : 덧셈 기능
    if works:
        return a + b


result = add(1, 11, True)
print(result)


def test_list():
    my_list = [1, 2, 3, 4]
    return my_list


result = add(1, 11, False)
print(result)
list_result = test_list()
print(list_result)
