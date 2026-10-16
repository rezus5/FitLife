
# Знакомство с пользователем.
print("Здравствуйте, как вас зовут?")
user_name = input("Введите ваше имя: ").title()

print("Добро пожаловать,", user_name)

# Запрос данных пользователя.
print("Введите ваш возраст, вес и рост.")

user_age = int(input("Ваш возраст: "))
user_weight = float(input("Ваш вес (в кг): "))
user_height = float(input("Ваш рост (в метрах, например 1.67): "))

# Рассчитываем ИМТ.
bmi = user_weight / (user_height ** 2)
rounded_bmi = round(bmi, 1)

# Рассчитываем норму воды в миллилитрах.
water_ml = user_weight * 30
water_l = water_ml / 1000

# Выводим результат для пользователя.
print(f"Отчет для пользователя: {user_name} ({user_age} лет)")
print(f"Твой индекс массы тела: {rounded_bmi}")
print(f"Рекомендуемая норма воды: {water_l} л в день")

print()
print("Расчет окончен. Будьте здоровы!")
