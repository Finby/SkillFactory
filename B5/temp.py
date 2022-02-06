shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])

print(id(shopping_center), id(shopping_center[-1]))
shopping_center[-1].append("Uniqlo")

print(shopping_center)
print(id(shopping_center), id(shopping_center[-1]))