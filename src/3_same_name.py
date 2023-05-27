#230527 동명이인 찾기

names = ["Tom", "Jerry", "Mike", "Jerry"]

for idx, name in enumerate(names):
    if name in names[idx + 1:]:
        print(name)
    
    