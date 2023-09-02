# 9_class_prac.py
class User:
    def __init__(self, user_name, user_age):
        self.name = user_name
        self.age = user_age
        self.address = "경기도 화성시 동탄반석로"
        self.my_image = ""
        self.goal = "서비스 만들기"
        self.favorite_food = ["고기", "마라탕"]

    def age_plus(self):
        """
        나이를 한 살 먹음
        """
        self.age = self.age +1

    def change_address(self, changed_address):
        self.address = changed_address

    def add_favorite_food(self, food):
        self.favorite_food.append(food)

    def eat_my_food(self):
        for food in self.favorite_food:
            print(f"good my food{food}")

    