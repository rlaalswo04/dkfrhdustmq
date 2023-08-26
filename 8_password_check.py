# my_words = "Hello Python11"
# print(len(my_words))
# is_valid = True

# if len(my_words) < 8:
#     is_valid = False

# for word in my_words:
#     print(f"{word}: {word.isupper()}")
#     print(f"{word}: {word.islower()}")
#     print(f"{word}: {word.isnumeric()}")
#     print(f"{word}: {word.isspace()}")


#     if is_valid:
#         print("패스워드 유효")
#     else:
#         print("패스워드")
def password_count(my_password):
    count_lower = 0
    count_upper = 0
    count_number = 0
    count_space = 0
    for word in my_password:
        if word.isupper():
            count_upper = count_upper + 1
        if word.islower():
            count_lower = count_lower + 1
        if word.isnumeric():
            count_number = count_number + 1
        if word.isspace():
            count_space = count_space + 1

    print(f"total_length: {len(my_password)}")
    print(f"count_upper: {(count_upper)}")
    print(f"count_lower: {(count_lower)}")
    print(f"count_number: {(count_number)}")
    print(f"count_space: {(count_space)}")


my_words = "hello Python11"
password_count(my_words)

# user1_password = "idlksbtsss1"


def password_valid(user_password):
    is_valid = True
    for word in user_password:
        print(word)
        if word.isspace():
            is_valid = False
    if len(user_password) < 8:
        is_valid = False
    return is_valid


my_words = "Hello Python 11"
